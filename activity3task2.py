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


# Define the file to download and the target local path
filename = '/workspaces/boto_3/downloads/cute_koala.jpg'  # Replace with your file path
bucket_name = 'sriya-techcatalyst-lab'  # Replace with your bucket name
key = 'cute_koala.jpg'  # Replace with your file key in S3

# download the file: 
with open(filename, 'wb') as f:
    s3.download_fileobj(bucket_name, key, f)

# Print a confirmation message
print(f'File {key} downloaded from bucket {bucket_name} to {filename}.')