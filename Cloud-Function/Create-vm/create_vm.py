from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
from random import randint
import yaml


# [START create_instance]
def main(event, context):
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('compute', 'v1', credentials=credentials)
    
   with open("config.yaml", 'r') as yamlfile:
        cfg = yaml.full_load(yamlfile)

    project_configs = cfg['project']
    project = project_configs.get('project-id')
    region = project_configs.get('region')
    zone = project_configs.get('zone')

    bucket_configs = cfg['bucket']
    bucket = bucket_configs.get('bucket-name')

    instance_configs = cfg['instance']
    instance_prefix_name = instance_configs.get('instance-prefix-name')
    instance_name = instance_prefix_name + str(randint(0, 100))
    machine_type = instance_configs.get('machine-type')

    startup_script = instance_configs.get('startup-script')
    startup_script = open(startup_script, 'r')
    sst = startup_script.read()
    
    config = {
        "kind": "compute#instance",
        "name": instance_name,
        "zone": "projects/"+project+"/zones/"+zone,
        "machineType": "projects/"+project+"/zones/"+zone+"/machineTypes/"+machine_type,
        "displayDevice": {
            "enableDisplay": False
        },
        "disks": [
            {
                "kind": "compute#attachedDisk",
                "type": "PERSISTENT",
                "boot": True,
                "mode": "READ_WRITE",
                "autoDelete": True,
                "deviceName": instance_name,
                "initializeParams": {
                    "sourceImage": "projects/debian-cloud/global/images/debian-9-stretch-v20190916",
                    "diskType": "projects/"+project+"/zones/"+zone+"/diskTypes/pd-standard",
                    "diskSizeGb": "10"
                },
            }
        ],
        "metadata": {
            "kind": "compute#metadata",
            "items": [
                {
                    "key": "startup-script",
                    "value": sst
                },
                {
                    "key": "bucket",
                    "value": bucket
                },
                {
                    "key": "zone",
                    "value": zone
                },
                {
                    "key": "instance_name",
                    "value": instance_name
                },
                {
                    "key": "file_name",
                    "value": event['name']
                }
            ]
        },
        "canIpForward": False,
        "networkInterfaces": [
            {
                "kind": "compute#networkInterface",
                "subnetwork": "projects/"+project+"/regions/"+region+"/subnetworks/default",
                "accessConfigs": [
                    {
                        "kind": "compute#accessConfig",
                        "name": "External NAT",
                        "type": "ONE_TO_ONE_NAT",
                        "networkTier": "PREMIUM"
                    }
                    ],
                "aliasIpRanges": []
            }
        ],
        "description": "",
        "labels": {},
        "scheduling": {
            "preemptible": False,
            "onHostMaintenance": "MIGRATE",
            "automaticRestart": True,
            "nodeAffinities": []
        },
        "deletionProtection": False,
        "reservationAffinity": {
            "consumeReservationType": "ANY_RESERVATION"
        },
        "serviceAccounts": [
            {
                "email": "924398889903-compute@developer.gserviceaccount.com",
                "scopes": [
                    "https://www.googleapis.com/auth/servicecontrol",
                    "https://www.googleapis.com/auth/service.management.readonly",
                    "https://www.googleapis.com/auth/logging.write",
                    "https://www.googleapis.com/auth/monitoring.write",
                    "https://www.googleapis.com/auth/trace.append",
                    "https://www.googleapis.com/auth/devstorage.full_control"
                ]
            }
        ]
    }

    request = service.instances().insert(project=project, zone=zone, body=config)
    print(request)
    return request.execute()
# [END create_instance]
