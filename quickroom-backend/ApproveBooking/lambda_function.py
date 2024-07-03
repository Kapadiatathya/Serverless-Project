import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    
    # Initialize the DynamoDB client
    dynamodb_client = boto3.client('dynamodb')

    # Iterate over messages in events
    for record in event['Records']:
        booking_request = json.loads(record['body'])
        logger.info(f"Parsed booking request: {json.dumps(booking_request)}")

        room_id = booking_request['room_id']
        user_id = booking_request['user_id']
        start_date = booking_request['start_date']
        end_date = booking_request['end_date']

        # Check For Approval Conditions
        approved = True

        if approved:
            try:
                # Save the booking to DynamoDB
                response = dynamodb_client.put_item(
                    TableName='Bookings',
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

    return {
        'statusCode': 200,
        'body': json.dumps('Booking processed successfully')
    }
