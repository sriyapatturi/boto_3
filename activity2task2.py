import configparser
import boto3

# Load AWS credentials
config = configparser.ConfigParser()
config.read('aws.cfg')

aws_access_key = config['AWS']['aws_access_key_id']
aws_secret_key = config['AWS']['aws_secret_access_key']


# Initialize the S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key
)

# Define the file to upload and the target bucket and key
bucket_name = 'sriya-techcatalyst-lab'  # Replace with your bucket name
key = 'cute_cat.jpg'  # Replace with your file key in S3

# Upload the file to S3 using file-like object
with open(key, "rb") as f:
    s3.upload_fileobj(f, bucket_name, key)

# Print a confirmation message
print(f'File uploaded to bucket {bucket_name} with key {key}.')