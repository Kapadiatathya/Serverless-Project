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