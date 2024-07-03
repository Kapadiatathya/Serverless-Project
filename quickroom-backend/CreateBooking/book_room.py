import boto3
import json

# Initialize the SQS client
sqs_client = boto3.client('sqs')

#  Queue URL Format
# 'https://sqs.<region>.amazonaws.com/<account_id>/<queue_name>'
queue_url = 'https://sqs.us-east-1.amazonaws.com/761577439658/Booking'

def send_booking_request(room_id, user_id, start_date, end_date):
    # Booking request payload
    booking_request = {
        'room_id': room_id,
        'user_id': user_id,
        'start_date': start_date,
        'end_date': end_date
    }

    # Send the message to the SQS
    response = sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(booking_request)
    )

    return response