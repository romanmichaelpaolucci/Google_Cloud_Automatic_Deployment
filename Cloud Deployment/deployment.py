from tools.cloud_storage import CloudBucket

if __name__ == '__main__':
    CloudBucket(
        'owner.json', 'bucket_name'
    ).upload_directory('directory_to_upload')
