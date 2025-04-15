from configparser import ConfigParser
from boto3 import resource

def auth(config_filename):
  # Grab config var access
  config = ConfigParser()
  config.read(config_filename)

  # Store vars
  service_name = config.get('aws_s3', 'service_name')
  region_name = config.get('aws_s3', 'region_name')
  access_key_id = config.get('aws_s3', 'access_key_id')
  secret_access_key = config.get('aws_s3', 'secret_access_key')
  s3_bucket = config.get('aws_s3', 's3_bucket')

  # Create var for accessing aws
  s3_resource = resource(
    service_name=service_name,
    region_name=region_name,
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key
  )

  return s3_resource, s3_bucket

test = auth('config.ini')
print(test[0])
print(test[1])