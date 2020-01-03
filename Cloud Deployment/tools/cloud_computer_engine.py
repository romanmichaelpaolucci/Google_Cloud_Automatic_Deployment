from google.auth import compute_engine
import googleapiclient.discovery


class CloudEngine:

    def __init__(self, credentials):
        self.engine_client = compute_engine.Client.from_service_account_json(
                credentials)
        print(self.engine_client)


def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items'] if 'items' in result else None
