from google.cloud import storage
import os


class CloudBucket:

    def __init__(self, credentials, bucket_name):
        self.storage_client = storage.Client.from_service_account_json(
                credentials)
        self.bucket = self.storage_client.get_bucket(bucket_name)
        print(self.bucket)

    def list_blobs(self):
        """Lists all the blobs in the bucket."""
        blobs = self.bucket.list_blobs()

        for blob in blobs:
            print(blob.name)

    def upload_blob(self, source_file_name, destination_blob_name):
        """Uploads a file to the bucket."""
        blob = self.bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
        print('File {} uploaded to {}.'.format(
            source_file_name,
            destination_blob_name))

    def upload_directory(self, path):
        for root, dirs, files in os.walk(path, topdown=False):
            # Get each file in the directory
            for file in files:
                print(os.path.join(root, file))
                self.upload_blob(
                    os.path.join(root, file),
                    # To create folders in cloud replace \ with /
                    os.path.join(root, file).replace('\\', '/') \
                    .replace('../', '')
                    )
            # For each directory recursively call this function
            for dir in dirs:
                self.upload_directory(os.path.join(root, dir))
