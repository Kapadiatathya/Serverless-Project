# serverless-team-33
## DALVacationHome

## Notifications API 

### User Registration Notify API

After a user registers, call this endpoint with the user's email:

```
POST https://8hzds97iz5.execute-api.us-east-1.amazonaws.com/notifications/registration
{
    "email": "String"
}
```

The user will receive an email after registration.

### User Login Notify API

After a user logs in, call this endpoint with the user's email:

```
POST https://8hzds97iz5.execute-api.us-east-1.amazonaws.com/prod/notifications/login
{
    "email": "String"
}
```

The user will receive an email after login.

### Booking Notify API

After a user books a room, send a request with 
- `success` set to `true` for booking success
- `success` set to`false` for booking failure.

```
POST https://8hzds97iz5.execute-api.us-east-1.amazonaws.com/prod/notifications/booking
{
    "email": "String",
    "success": "Boolean"
}
```

The user will receive an email with their booking status.

### Get Sentiment Analysis result

To get the sentiment analysis result of any sentence or sentences send the text to the following API:

```
POST https://us-central1-sharp-avatar-428014-f8.cloudfunctions.net/sentiment-analysis
{
    "text": "I love working with Google Cloud Functions! They are the best."
}
```

The result will look like this:

```
{
    "documentSentiment": {
        "magnitude": 1.9,
        "score": 0.9
    },
    "language": "en",
    "sentences": [
        {
            "sentiment": {
                "magnitude": 0.9,
                "score": 0.9
            },
            "text": {
                "beginOffset": 0,
                "content": "I love working with Google Cloud Functions!"
            }
        },
        {
            "sentiment": {
                "magnitude": 0.9,
                "score": 0.9
            },
            "text": {
                "beginOffset": 44,
                "content": "THey are the best."
            }
        }
    ]
}
```
Get the required result for each sentence or the text as a whole.