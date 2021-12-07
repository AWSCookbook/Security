# Testing IAM Policies with the IAM Policy Simulator

## Clean up 
### Step Text
Detach the AmazonEC2ReadOnlyAccess policy from the role:
```
aws iam detach-role-policy --role-name AWSCookbook104IamRole \
--policy-arn arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess
```

Delete the IAM Role for the proxy: 

`aws iam delete-role --role-name AWSCookbook104IamRole`
