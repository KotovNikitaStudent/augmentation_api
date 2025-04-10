from io import BytesIO
import boto3

from app.base_settings import get_settings


settings = get_settings()


s3 = boto3.client(
    "s3",
    endpoint_url=settings.MINIO_ENDPOINT_URL,
    aws_access_key_id=settings.MINIO_ACCESS_KEY,
    aws_secret_access_key=settings.MINIO_SECRET_KEY,
)

bucket_name = settings.S3_BUCKET_NAME


def upload_to_s3(image: BytesIO, file_name: str):
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=image)


def download_from_s3(file_name: str) -> BytesIO:
    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    return response["Body"].read()
