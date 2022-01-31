# Connecting to EC2 Instances Using AWS SSM Session Manager
## Preparation
### This recipe requires some “prep work” which deploys resources that you’ll build the solution on. You will use the AWS CDK to deploy these resources 

### In the root of this Chapter’s repo cd to the “106-Connecting-to-EC2-Instances-Using-Session-Manager/cdk-AWS-Cookbook-106/” directory and follow the subsequent steps: 

```
cd 106-Connecting-to-EC2-Instances-Using-Session-Manager/cdk-AWS-Cookbook-106/
test -d .venv || python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cdk deploy
```

### Wait for the cdk deploy command to complete. 

### We created a helper.py script to let you easily create and export environment variables to make subsequent commands easier. Run the script, and copy the output to your terminal to export variables:

`python helper.py`

### Navigate up to the main directory for this recipe (out of the “cdk-AWS-Cookbook-106” directory):

`cd ..`


## Clean up 

### Terminate the EC2 Instance:

```
aws ec2 terminate-instances --instance-ids $INSTANCE_ID
```

### Detach the policy from the role:

```
aws iam detach-role-policy --role-name AWSCookbook106SSMRole --policy-arn arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
```

### Remove the role from the instance profile:

```
aws iam remove-role-from-instance-profile --instance-profile-name AWSCookbook106InstanceProfile --role-name AWSCookbook106SSMRole
```

### Delete the instance profile:

```
aws iam delete-instance-profile --instance-profile-name AWSCookbook106InstanceProfile
```

### Delete the role:

```
aws iam delete-role --role-name AWSCookbook106SSMRole
```

### Go to the cdk-AWS-Cookbook-106 directory:

`cd cdk-AWS-Cookbook-106/`

### To clean up the environment variables, run the helper.py script in this recipe’s cdk- directory with the --unset flag, and copy the output to your terminal to export variables:

`python helper.py --unset`

### Unset your manually created environment variables:

```
unset ROLE_ARN
unset AMI_ID
unset INSTANCE_ID
```

### Use the AWS CDK to destroy the resources, deactivate your Python virtual environment, and go to the root of the chapter:

`cdk destroy && deactivate && rm -r .venv/ && cd ../..`
