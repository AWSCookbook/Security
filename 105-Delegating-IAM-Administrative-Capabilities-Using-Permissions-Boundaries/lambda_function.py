import json
import os
import sys

def lambda_handler(event, context):

   return {
      'statusCode': 200,
      'body': json.dumps('Hello AWSCookbook Reader!')
   }
