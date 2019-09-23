from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
from random import randint


# [START create_instance]
def main(event, context):
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('compute', 'v1', credentials=credentials)
    
    project = 'refreshing-mark-252714'
    zone = 'us-central1-a'
    bucket = 'refreshing-mark-252714'
    instance_name = "big-image-processing-" + str(randint(0, 100))
    startup_script = open("startup-script.sh", 'r')
    sst = startup_script.read()
    
    config = {
        "kind": "compute#instance",
        "name": instance_name,
        "zone": "projects/refreshing-mark-252714/zones/us-central1-a",
        "machineType": "projects/refreshing-mark-252714/zones/us-central1-a/machineTypes/n1-standard-1",
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
                "deviceName": "instance-1",
                "initializeParams": {
                    "sourceImage": "projects/debian-cloud/global/images/debian-9-stretch-v20190916",
                    "diskType": "projects/refreshing-mark-252714/zones/us-central1-a/diskTypes/pd-standard",
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
                "subnetwork": "projects/refreshing-mark-252714/regions/us-central1/subnetworks/default",
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
