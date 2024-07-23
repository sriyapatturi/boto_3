import configparser
import boto3

# Load AWS credentials
config = configparser.ConfigParser()
config.read('aws.cfg')

aws_access_key = config['AWS']['aws_access_key_id']
aws_secret_key = config['AWS']['aws_secret_access_key']

# Initialize the S3 client
# Initialize the S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key
)


# Define the file to upload and the target bucket and key
filename = 'cute_dogs.jpg'  # Replace with your file path
bucket_name = 'sriya-techcatalyst-lab'  # Replace with your bucket name
key = 'cute_dogs.jpg'  # Replace with your file key in S3

# Upload the file to S3
s3.upload_file(filename, bucket_name, key)

# Print a confirmation message
print(f'File {filename} uploaded to bucket {bucket_name} with key {key}.')