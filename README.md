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

After a user books a room, send a request for both successful and failed booking.

If booking was successful:
- set `email` to the user's email
- set`success` to `true`
- set `reference_code` to the booking reference code.

```
POST https://8hzds97iz5.execute-api.us-east-1.amazonaws.com/prod/notifications/booking
{
    "email": "String",
    "success": "Boolean",
    "reference_code": "String"
}
```

If booking failed:
- set `email` to the user's email
- set `success` to`false`
- set `reference_code` to null.

```
POST https://8hzds97iz5.execute-api.us-east-1.amazonaws.com/prod/notifications/booking
{
    "email": "String",
    "success": "Boolean",
    "reference_code": null
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

ROOM BOOKING SYSTEM WORKFLOW-
1. Frontend calls SQS Url with the booking information as payload.
2. SQS automatically triggers Lambda Function as soon as it receives message.
3. Lambda Function checks for approval conditions and makes an entry to DynamoDb Table if approval conditions are met.

## Reservations APIs 

### Create Reservation

Call this API after the user clicks the Create Reservation button. All JSON objects are mandatory:

```
POST https://b2111el3sj.execute-api.us-east-1.amazonaws.com/v1/createReservation

{
  "BookingID": "A6",
  "CheckInDate": "Jul 1",
  "CheckOutDate": "Jul 5",
  "Currency": "CAD",
  "FirstName": "Test",
  "LastName": "User",
  "RoomNumber": "707",
  "RoomPricePerDay": "220",
  "RoomType": "King",
  "TotalGuests": "4",
  "TotalNights": "5",
  "TotalPrice": "1100"
}
```

### Read Reservation

Call this API to fetch a Reservation based on BookingID:

```
POST https://b2111el3sj.execute-api.us-east-1.amazonaws.com/v1/readReservation

{
  "BookingID": "A6"
}
```

### Update Reservation

Call this API when a user modifies the Reservation. Booking ID mandatory, everything else optional:

```
POST https://b2111el3sj.execute-api.us-east-1.amazonaws.com/v1/updateReservation

{
  "BookingID": "A6",
  "CheckInDate": "Jul 1",
  "CheckOutDate": "Jul 5",
  "Currency": "CAD",
  "FirstName": "Brand New",
  "LastName": "User",
  "RoomNumber": "707",
  "RoomPricePerDay": "220",
  "RoomType": "King",
  "TotalGuests": "4",
  "TotalNights": "5",
  "TotalPrice": "1100"
}
```

### Delete Reservation

Call this API to delete a Reservation based on BookingID:

```
POST https://b2111el3sj.execute-api.us-east-1.amazonaws.com/v1/deleteReservation

{
  "BookingID": "A6"
}
```
