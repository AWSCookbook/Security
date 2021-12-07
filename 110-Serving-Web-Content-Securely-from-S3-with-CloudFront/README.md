# Serving Web Content Securely from S3 with CloudFront
## Preparation
### Create an index.html file
```
echo AWSCookbook > index.html
```

### Set a unique suffix to use for the S3 bucket name:
```
RANDOM_STRING=$(aws secretsmanager get-random-password \
--exclude-punctuation --exclude-uppercase \
--password-length 6 --require-each-included-type \
--output text \
--query RandomPassword)
```

### Create a S3 bucket:
```
aws s3api create-bucket --bucket awscookbook110-$RANDOM_STRING
```

### Copy the previously created file to the bucket:
```
aws s3 cp index.html s3://awscookbook110-$RANDOM_STRING/
```

### Set the public access block for your bucket:
```
aws s3api put-public-access-block \
     --bucket awscookbook110-$RANDOM_STRING \
     --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
```

## Clean up 
### Disable the CloudFront distribution by logging into the console and clicking the Disable button for the distribution that you created (this process can take up to 15 minutes)

### Delete the CloudFront distribution:
```
aws cloudfront delete-distribution --id $DISTRIBUTION_ID --if-match $(aws cloudfront get-distribution --id $DISTRIBUTION_ID --query ETag --output text)
```

### Delete the Origin Access Identity:
```
aws cloudfront delete-cloud-front-origin-access-identity --id $OAI --if-match $(aws cloudfront get-cloud-front-origin-access-identity --id $OAI --query ETag --output text)
```

### Clean up the bucket:
```
aws s3 rm s3://awscookbook110-$RANDOM_STRING/index.html
```

### Delete the S3 bucket:
```
aws s3api delete-bucket --bucket awscookbook110-$RANDOM_STRING
```

Unset your manually created environment variables:
```
unset DISTRIBUTION_ID
unset DOMAIN_NAME
unset OAI
unset RANDOM_STRING
unset BUCKET_NAME
```
