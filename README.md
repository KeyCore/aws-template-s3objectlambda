# S3 Object Lambda Sample Template
## An example cloudformation template for S3 Object lambda deployment

Based on the sample from an AWS blog post: https://aws.amazon.com/blogs/aws/introducing-amazon-s3-object-lambda-use-your-code-to-process-data-as-it-is-being-retrieved-from-s3/

This template will create the following resources:
- S3 Bucket
- S3 Bucket Policy
- S3 Access Point
- S3 Object Lambda Access Point
- Lambda Function
- IAM Role


### Step-by-step
1. Deploy the yaml template on AWS, using either the cli or console
2. Upload a sample txt file to the newly created S3 bucket
3. Modify the s3ObjectLambda-test.py with your bucket name, object key and your access point ARN
4. Run python script and observe the print outs