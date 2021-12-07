# Blocking Public Access for an S3 Bucket
## Preparation
### Set a unique suffix to use for the S3 BucketName:
```
RANDOM_STRING=$(aws secretsmanager get-random-password \
--exclude-punctuation --exclude-uppercase \
--password-length 6 --require-each-included-type \
--output text \
--query RandomPassword)
```

### Create a S3 Bucket:
```
aws s3api create-bucket --bucket awscookbook109-$RANDOM_STRING
```

### Apply a bucket policy that grants public read to objects in your bucket by following the next steps.

### Create a file named  public-read-template.json to create a bucket policy that you will apply to your S3 bucket (File provided in this chapter’s repo): 
```
{
  "Version":"2012-10-17",
  "Statement":[
    {
      "Sid":"PublicRead",
      "Effect":"Allow",
      "Principal": "*",
      "Action":["s3:GetObject","s3:GetObjectVersion"],
      "Resource":["arn:aws:s3:::BUCKET_NAME/*"]
    }
  ]
}
```

### Use the sed command to replace the values in public-read-template.json:
```
sed -e "s/BUCKET_NAME/awscookbook109-$RANDOM_STRING/g" \
public-read-template.json > public-read.json
```

### Add the S3 Bucket Policy to your S3 bucket: 
```
aws s3api put-bucket-policy \
--bucket awscookbook109-$RANDOM_STRING \
--policy file://public-read.json
```


## Clean up 
### Delete the S3 bucket:
```
aws s3api delete-bucket --bucket awscookbook109-$RANDOM_STRING
```

### Delete the Access Analyzer:
```
aws accessanalyzer delete-analyzer --analyzer-name awscookbook109
```

### Unset the environment variables that you created manually:
```
unset RANDOM_STRING
unset ANALYZER_ARN
```

    
