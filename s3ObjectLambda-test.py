import boto3

s3 = boto3.client('s3')

print('Original object from the S3 bucket:')
original = s3.get_object(
  Bucket='s3objectlambda-stack-s3bucket-jle6pwe39kyq',
  Key='aws_pro_notes.txt')
print(original['Body'].read().decode('utf-8'))

print('Object processed by S3 Object Lambda:')
transformed = s3.get_object(
  Bucket='arn:aws:s3-object-lambda:eu-west-1:124246457893:accesspoint/my-object-lambda-ap',
  Key='aws_pro_notes.txt')
print(transformed['Body'].read().decode('utf-8'))