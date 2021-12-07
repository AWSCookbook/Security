# Storing, Encrypting, and Accessing Passwords Using Secrets Manager
## Preparation
### This recipe requires some “prep work” which deploys resources that you’ll build the solution on. You will use the AWS CDK to deploy these resources 

### In the root of this Chapter’s repo cd to the “108-Storing-Encrypting-Accessing-Passwords/cdk-AWS-Cookbook-108” directory and follow the subsequent steps: 

```
cd 108-Storing-Encrypting-Accessing-Passwords/cdk-AWS-Cookbook-108
test -d .venv || python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cdk deploy
```

### Wait for the cdk deploy command to complete. 

### We created a helper.py script to let you easily create and export environment variables to make subsequent commands easier. Run the script, and copy the output to your terminal to export variables:

`python helper.py`

### Navigate up to the main directory for this recipe (out of the “cdk-AWS-Cookbook-207” directory):

`cd ..`


## Clean up 

### Delete the Secret:

`aws secretsmanager delete-secret --secret-id AWSCookbook108/Secret1 --recovery-window-in-days 7`

### Detach the IAM Policy that you created from the IAM Role associated with EC2 Instance: 
```
aws iam detach-role-policy --role-name $ROLE_NAME --policy-arn arn:aws:iam::$AWS_ACCOUNT_ID:policy/AWSCookbook108SecretAccess
```

### Delete the IAM Policy you created:
```
aws iam delete-policy --policy-arn arn:aws:iam::$AWS_ACCOUNT_ID:policy/AWSCookbook108SecretAccess
```

### Go to the cdk-AWS-Cookbook-108 directory:

`cd cdk-AWS-Cookbook-108/`

### To clean up the environment variables, run the helper.py script in this recipe’s cdk- directory with the --unset flag, and copy the output to your terminal to export variables:

`python helper.py --unset`

### Unset your manually created environment variables:

```
unset RANDOM_STRING
unset SECRET_ARN
```

### Use the AWS CDK to destroy the resources, deactivate your Python virtual environment, and go to the root of the chapter:

`cdk destroy && deactivate && rm -r .venv/ && cd ../..`
