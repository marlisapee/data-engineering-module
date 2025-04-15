from auth import auth
from pathlib import Path

def upload_file(object_key, filename):
  s3_resource, s3_bucket = auth('config.ini')
  print(filename)
  try:
    bucket = s3_resource.Bucket(s3_bucket)
    bucket.upload_file(filename, object_key)
    return True
  except Exception as e:
    print(f'Error uploading file to s3: {str(e)}')
    return False
    