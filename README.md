# serverless-team-33
## DALVacationHome

## Notifications API 

### User Registration API

After a user registers, call this endpoint with the user's email:

```
POST https://a93iyas0tk.execute-api.us-east-1.amazonaws.com/prod/user-registration/notify
{
    "email": "String"
}
```

The user will receive an email after registration.

### User Login API

After a user logs in, call this endpoint with the user's email:

```
POST https://a93iyas0tk.execute-api.us-east-1.amazonaws.com/prod/user-login/notify
{
    "email": "String"
}
```

The user will receive an email after login.