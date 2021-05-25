Example TrackingServer Custom Resource

```
apiVersion: ai.mlflow.org/v1alpha1
kind: TrackingServer
metadata:
  name: zak-tracking-server
spec:
  # Add fields here
  size: 1
  Image: "quay.io/zmhassan/mlflow:0.8.2"
  # S3 info when deployed with ODH ceph-nano component
  s3_endpoint_url: "http://ceph-nano-0"
  aws_cred_secret: ceph-nano-credentials
```
