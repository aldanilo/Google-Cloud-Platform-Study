from googleapiclient import discovery
from oauth2client.client import GoogleCredentials


def delete_instance(compute, project, zone, name):
    return compute.instances().delete(
        project=project,
        zone=zone,
        instance=name).execute()


def main(request):
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('compute', 'v1', credentials=credentials)
    request_json = request.get_json()
    if (request_json and 'project' in request_json and 'zone' in request_json and 'name' in request_json):
        project = request_json['project']
        zone = request_json['zone']
        name = request_json['name']
        delete_instance(service, project, zone, name)
