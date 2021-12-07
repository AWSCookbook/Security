# Enforcing IAM User Password Policies in Your AWS Account

## Clean up 
### Delete the login profiles that you created (including the validation step user):
```
aws iam delete-login-profile --user-name awscookbook103user
aws iam delete-login-profile --user-name awscookbook103user2
```

### Remove the user from the group:
```
aws iam remove-user-from-group --user-name awscookbook103user \
--group-name AWSCookbook103Group
```

### Detach the policy from the group:
```
aws iam detach-group-policy --group-name AWSCookbook103Group \
--policy-arn arn:aws:iam::aws:policy/AWSBillingReadOnlyAccess
```

### Delete the group:
`aws iam delete-group --group-name AWSCookbook103Group`

### Delete the users that you created (including the validation step user):
```
aws iam delete-user --user-name awscookbook103user
aws iam delete-user --user-name awscookbook103user2
```

### Delete the account password policy that you configured:
`aws iam delete-account-password-policy`

### Unset the local variables you created:
```
unset RANDOM_STRING
unset RANDOM_STRING2
```
