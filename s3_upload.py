# pip install boto3 

import boto3 

s3_resource = boto3.resource( 
				's3', 
                aws_access_key_id='AKIAX24HGBAXYY4RBMWU', 
                aws_secret_access_key='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', 
                region_name='us-east-1', 
) 

# get image file 
data = open('images/test.png', 'rb') 
image_name = 'test.png'
region = 'us-east-1'
bucket_name = 'clothes-photo'

# save image to S3 bucket as public 
s3_resource.Bucket(bucket_name).put_object(Body=data, Key=image_name, ACL='public-read') 

# get public image url 
url = "https://s3-%s.amazonaws.com/%s/%s" % (region, bucket_name, image_name)