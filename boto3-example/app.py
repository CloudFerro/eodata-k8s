import boto3
import time

access_key='anystring'
secret_key='anystring'
key='Landsat-5/TM/L1T/2011/11/11/LS05_RKSE_TM__GTC_1P_20111111T093819_20111111T093847_147313_0191_0025_1E1E/LS05_RKSE_TM__GTC_1P_20111111T093819_20111111T093847_147313_0191_0025_1E1E.BP.PNG'
host='http://data.cloudferro.com'

s3=boto3.resource('s3',aws_access_key_id=access_key,
aws_secret_access_key=secret_key, endpoint_url=host,)

bucket=s3.Bucket('DIAS')
bucket.download_file(key, '/app/image.png')

time.sleep(300)
