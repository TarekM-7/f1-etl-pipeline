import os
from dotenv import load_dotenv
import boto3

def load(df, local_path, s3_key):
    load_dotenv()
    bucket_name = os.getenv('AWS_BUCKET_NAME')
    df.to_csv(local_path, index=False)
    s3 = boto3.client('s3')
    s3.upload_file(local_path, bucket_name, s3_key)