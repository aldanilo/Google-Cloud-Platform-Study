#! /bin/bash
PROJECT_NAME=$(gcloud config list --format 'value(core.project)')

gsutil mb -c regional -l us-east1 gs://$PROJECT_NAME/

gcloud compute instances create teste-1 --machine-type f1-micro \
                                        --zone=us-central1-a \
                                        --metadata=lab-logs-bucket=gs://$PROJECT_NAME/ \
                                        --metadata-from-file startup-script=worker-startup-script.sh \
                                        --scopes cloud-platform
