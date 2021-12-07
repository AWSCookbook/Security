# Delegating IAM Administrative Capabilities Using Permissions Boundaries

## Clean up 

### Unset the variables you set to assume the AWSCookbook105 role in your terminal:
```
unset AWS_ACCESS_KEY_ID
unset AWS_SECRET_ACCESS_KEY
unset AWS_SESSION_TOKEN
```

### Detach the AmazonDynamoDBFullAccess and CloudWatchFullAccess policy from the role:
```
aws iam detach-role-policy --role-name AWSCookbook105test1 \
--policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess

aws iam detach-role-policy --role-name AWSCookbook105test1 \
--policy-arn arn:aws:iam::aws:policy/CloudWatchFullAccess
```

### Delete the IAM Role you used to test:
```
aws iam delete-role --role-name AWSCookbook105test1
```

### Detach the Policy you created from the role:
```
aws iam detach-role-policy --role-name AWSCookbook105Role \
--policy-arn arn:aws:iam::$AWS_ACCOUNT_ID:policy/AWSCookbook105Policy
```

### Delete the policy:
```
aws iam delete-policy --policy-arn \
arn:aws:iam::$AWS_ACCOUNT_ID:policy/AWSCookbook105Policy
```

### Delete the permissions boundary:
```
aws iam delete-policy --policy-arn \
arn:aws:iam::$AWS_ACCOUNT_ID:policy/AWSCookbook105PB
```

### Delete the IAM Role:
```
aws iam delete-role --role-name AWSCookbook105Role
```

### Unset the variables you set:
```
unset PRINCIPAL_ARN
unset ROLE_ARN
unset TEST_ROLE_1
unset creds
```

