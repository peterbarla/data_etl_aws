import boto3
import os.path

# CREATE S3 CLIENT
s3_client = boto3.client('s3')

def upload(obj)-> None:
    try:
        # UPLOAD ZIP FILE TO S3
        s3_client.upload_file(obj, 'my-etl-bucket2', os.path.basename(obj))
    except Exception as e:
        print(e)
        return False
    return True