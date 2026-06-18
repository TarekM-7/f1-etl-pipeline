import os
from dotenv import load_dotenv
import boto3
import logging

logging.basicConfig(
    format='[{levelname}] {asctime} | {message}',
    style='{',
    datefmt='%H:%M:%S',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def load(df, local_path, s3_key):
    try:
        logger.info("Starting data load stage")
        load_dotenv()
        bucket_name = os.getenv('AWS_BUCKET_NAME')
        logger.info("Writing processed dataset to local storage")
        df.to_csv(local_path, index=False)
        logger.info("Uploading processed dataset to S3")
        s3 = boto3.client('s3')
        s3.upload_file(local_path, bucket_name, s3_key)
        logger.info("Data load stage completed successfully")
    except Exception as e:
        logger.error(f"Error loading the data: {e}")
        raise