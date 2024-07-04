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
