#! /bin/bash

set -x

apt-get update

BUCKET=$(curl http://metadata/computeMetadata/v1/instance/attributes/bucket -H "Metadata-Flavor: Google")
ZONE=$(curl http://metadata/computeMetadata/v1/instance/attributes/zone -H "Metadata-Flavor: Google")
INSTANCE_NAME=$(curl http://metadata/computeMetadata/v1/instance/attributes/instance_name -H "Metadata-Flavor: Google")
FILE_NAME=$(curl http://metadata/computeMetadata/v1/instance/attributes/file_name -H "Metadata-Flavor: Google")
DELETE_INSTANCE=$(curl http://metadata/computeMetadata/v1/instance/attributes/delete -H "Metadata-Flavor: Google")
PROJECT_ID=$(gcloud config list --format 'value(core.project)')

cat > ~/delete_instance.sh <<EOF
PROJECT_ID=$(gcloud config list --format 'value(core.project)')
ZONE=$(curl http://metadata/computeMetadata/v1/instance/attributes/zone -H "Metadata-Flavor: Google")
INSTANCE_NAME=$(curl http://metadata/computeMetadata/v1/instance/attributes/instance_name -H "Metadata-Flavor: Google")

curl -X POST "[url function]" -H "Content-Type:application/json" \
--data '{"project": "'$PROJECT_ID'","zone": "'$ZONE'","name": "'$INSTANCE_NAME'"}'
EOF

chmod +x ~/delete_instance.sh

sleep 60

bash ~/delete_instance.sh
