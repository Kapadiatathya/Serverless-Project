import json
import boto3
import os

sns_client = boto3.client('sns')

def lambda_handler(event, context):
    '''
    Sends an email to a newly registered user
    '''
    
    # Get the email from the request body
    try:
        body = json.loads(event['body'])
        email = body['email']
    except (KeyError, json.JSONDecodeError) as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f'Email not found: {str(e)}')
        }
    
    # Create SNS topic
    try:
        tokens = email.split('@')
        user_name = tokens[0]
        
        remaining_tokens = tokens[1].split('.')
        mail_server, domain = remaining_tokens[0], remaining_tokens[1]
        
        response = sns_client.create_topic(
            Name=f'user_registered_{user_name}_at_{mail_server}_dot_{domain}')
        topic_arn = response['TopicArn']
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error creating SNS topic: {str(e)}')
        }
    
    # Subscribe email to the SNS topic
    try:
        sns_client.subscribe(
            TopicArn=topic_arn,
            Protocol='email',
            Endpoint=email
        )
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error subscribing email: {str(e)}')
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps('Registration email sent successfully')
    }
    