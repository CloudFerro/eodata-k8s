### Note
- This is experimental, tested only with the Alpine 3.16.2 base image.
- Requires running the container in privileged mode.
- Docker image published in cfro/direct-mount-test DockerHub repo.

### How to run?

Apply configmap with the bucket name, endpoint and mountpoint:
```
kubectl apply -f configmap.yaml
```

Create S3 secret (for EODATA access within the cloud any key will work from within CloudFerro cloud):
```
kubectl create secret generic awssecret --from-literal=AWSACCESSKEYID='anykey' --from-literal=AWSSECRETACCESSKEY='anykey'
```

Deploy the pod (called `test-direct-mount`) which will mount EODATA:
```
kubectl apply -f pod.yaml
```

Verify the mount:
```
$ kubectl exec --tty --stdin test-direct-mount -- sh
/ # cd /test
/test # ls
C3S             CAMS            CEMS            CLMS            CMEMS           Envisat         Envisat-ASAR    Jason-3         Landsat-5       Landsat-7       Landsat-8       SMOS            Sentinel-1      Sentinel-1-COG  Sentinel-1-RTC  Sentinel-2      Sentinel-3      Sentinel-5P     Sentinel-6      auxdata
```


