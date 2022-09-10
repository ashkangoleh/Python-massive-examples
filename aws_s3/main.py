import boto3


s3 = boto3.resource('https://0.0.0.0:4510')

print("==>> conn: ", s3.buckets.all())