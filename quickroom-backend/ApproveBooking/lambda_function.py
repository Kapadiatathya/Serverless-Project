import json
import boto3
import logging
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize the DynamoDB client
dynamodb_client = boto3.client('dynamodb')

# Initialize the SNS client for notifications
sns_client = boto3.client('sns')

# Define DynamoDb Table
table_name = 'Bookings'

def check_booking_availability(room_id, start_date, end_date):
    try:
        response = dynamodb_client.scan(
            TableName=table_name,
            FilterExpression="(#room_id = :room_id AND end_date >= :start_date AND start_date <= :end_date) AND #status = :status",
            ExpressionAttributeNames={
                "#room_id": "room_id",
                "#status": "status"
            },
            ExpressionAttributeValues={
                ":room_id": {"S": room_id},
                ":start_date": {"S": start_date},
                ":end_date": {"S": end_date},
                ":status": {"S": "approved"}
            }
        )
        return response['Items']
    except Exception as e:
        logger.error(f"Error checking booking availability: {e}")
        raise e

def lambda_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    
    for record in event['Records']:
        # Parse the message body
        booking_request = json.loads(record['body'])
        logger.info(f"Parsed booking request: {json.dumps(booking_request)}")

        # Extract booking details
        room_id = booking_request['room_id']
        user_id = booking_request['user_id']
        start_date = booking_request['start_date']
        end_date = booking_request['end_date']

        # Convert dates to datetime objects for comparison
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')

        # Perform approval checks
        approved = True

        # Check room availability using the new function
        try:
            overlapping_bookings = check_booking_availability(room_id, start_date, end_date)
            if overlapping_bookings:
                approved = False
                logger.info(f"Room {room_id} is not available from {start_date} to {end_date}. Overlapping bookings: {overlapping_bookings}")
            else:
                logger.info(f"Room {room_id} is available from {start_date} to {end_date}.")
        except Exception as e:
            logger.error(f"Error checking room availability: {e}")
            return {
                'statusCode': 500,
                'body': json.dumps(f"Error: {str(e)}")
            }

        # Check for user existence and access permissions, if applicable

        if approved:
            try:
                # Save the booking to DynamoDB
                response = dynamodb_client.put_item(
                    TableName=table_name,
                    Item={
                        'room_id': {'S': room_id},
                        'user_id': {'S': user_id},
                        'start_date': {'S': start_date},
                        'end_date': {'S': end_date},
                        'status': {'S': 'approved'}
                    }
                )
                logger.info(f"Successfully inserted item: {response}")
            except dynamodb_client.exceptions.ResourceNotFoundException as e:
                logger.error(f"DynamoDB table not found: {e}")
                return {
                    'statusCode': 500,
                    'body': json.dumps(f"Error: {str(e)}")
                }
            except Exception as e:
                logger.error(f"Unexpected error: {e}")
                return {
                    'statusCode': 500,
                    'body': json.dumps(f"Error: {str(e)}")
                }
        else:
            try:
                sns_client.publish(
                    # SNS TopicArn needs to be integrated
                    TopicArn='arn:aws:sns:<region>:<account_id>:<topic_name>',
                    Message=f"Booking request for room {room_id} by user {user_id} from {start_date} to {end_date} was rejected.",
                    Subject='Booking Rejected'
                )
            except Exception as e:
                logger.error(f"Error sending SNS notification: {e}")

    return {
        'statusCode': 200,
        'body': json.dumps('Booking processed successfully')
    }
