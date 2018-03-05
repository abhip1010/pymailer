!/bin/bash

# Exit on any error
set -e
DI=gcr.io/high-service-196906/pymailer
sudo /opt/google-cloud-sdk/bin/gcloud docker push $DI
sudo chown -R ubuntu:ubuntu /home/ubuntu/.kube
kubectl patch deployment pymailer -p '{"spec":{"template":{"spec":{"containers":[{"name":"pymailer","image":"gcr.io/high-service-196906/pymailer:'"$CIRCLE_SHA1"'"}]}}}}'
