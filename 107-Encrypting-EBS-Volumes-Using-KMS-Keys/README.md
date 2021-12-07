# Encrypting EBS Volumes Using KMS Keys

## Clean up 

### Set the KMS Key used for EBS Encryption back to the
```
aws ec2 modify-ebs-default-kms-key-id \
     --kms-key-id alias/aws/ebs
```

OR Disable default EBS Encryption: 
```
aws ec2 disable-ebs-encryption-by-default
```

### Disable the KMS Key: 

`aws kms disable-key --key-id $KMS_KEY_ID`

### Scheduled the KMS Key for deletion:
```
aws kms schedule-key-deletion \
--key-id $KMS_KEY_ID \
--pending-window-in-days 7
```

### Delete the Key Alias: 

`aws kms delete-alias --alias-name alias/AWSCookbook107Key`

