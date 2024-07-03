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
  "text": "Google Cloud Functions are disgusting! They are the worst thing I have ever seen so bad",
  "rating": 0.0
}
```

The result will look like this:

```
{
    "document_sentiment": {
        "magnitude": 1.7,
        "score": -0.8
    },
    "language": "en",
    "sentences": [
        {
            "sentiment": {
                "magnitude": 0.8,
                "score": -0.8
            },
            "text": {
                "beginOffset": 0,
                "content": "Google Cloud Functions are disgusting!"
            }
        },
        {
            "sentiment": {
                "magnitude": 0.8,
                "score": -0.8
            },
            "text": {
                "beginOffset": 39,
                "content": "They are the worst thing I have ever seen so bad."
            }
        }
    ],
    "sentiment_category": "negative",
    "sentiment_score": -4.0,
    "total_review_score": -1.6,
    "user_rating": 0.0
}
```
Get the required result for the test or combined with ratings.