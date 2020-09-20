# AWS_Scripts: Consists of AWS python scripts.

S3-PresignedURL generator data signature is as follows:
{
    "bucket_name": "<your-bucket-name>",
    "file_key": "<file-name>",
    "expiry_time": <enpiry-time-in-integer>, #example: 3600
    "action" : "upload/download"
}
