import os
import boto3

def run():
    
    bucket_name = os.environ.get('INPUT_BUCKET')
    region_name = os.environ.get('INPUT_REGION_NAME')
    folder_path = os.environ.get('INPUT_FOLDER_PATH')

    session = boto3.client('s3', region_name=region_name)

    if folder_path is None:
        raise ValueError("INPUT_FOLDER_PATH environment variable is not set.")
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            key = os.path.relpath(file_path, folder_path)
            session.upload_file(file_path, bucket_name, f"vibish/{key}")
max_tries = 3
run()