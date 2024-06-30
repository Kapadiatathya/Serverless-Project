import json
import boto3

def lambda_handler(event, context):
    # Initialize the DynamoDB client
    dynamodb_client = boto3.client('dynamodb')

    # Iterate over the messages in the event
    for record in event['Records']:
        # Parse messages
        booking_request = json.loads(record['body'])

        room_id = booking_request['room_id']
        user_id = booking_request['user_id']
        start_date = booking_request['start_date']
        end_date = booking_request['end_date']

        # Check and confirm approval logic
        approved = True

        if approved:
            # Save the booking to DynamoDB
            dynamodb_client.put_item(
                TableName='Bookings',
                Item={
                    'room_id': {'S': room_id},
                    'user_id': {'S': user_id},
                    'start_date': {'S': start_date},
                    'end_date': {'S': end_date},
                    'status': {'S': 'approved'}
                }
            )
        else:
            # Handle booking rejection
            pass

    return {
        'statusCode': 200,
        'body': json.dumps('Booking processed successfully')
    }
