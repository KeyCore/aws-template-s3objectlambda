import boto3

s3 = boto3.client('s3')

# Your bucket
my_bucket = ''
# The file you have uploaded
my_object_key = ''
# my_object_lambda_ap is the full ARN of the AP
my_object_lambda_ap='' 

print('Original object from the S3 bucket:')
original = s3.get_object(
  Bucket=my_bucket,
  Key=my_object_key)
print(original['Body'].read().decode('utf-8'))

print('Object processed by S3 Object Lambda:')
transformed = s3.get_object(
  Bucket=my_object_lambda_ap,
  Key=my_object_key)
print(transformed['Body'].read().decode('utf-8'))