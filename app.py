from flask import Flask, render_template
#from flask_bootstrap import Bootstrap
import boto3
import os
# Set environment variables
# Get environment variables
#S3_KEY = os.environ.get('S3_KEY')
#S3_SECRET = os.environ.get('S3_SECRET')
app = Flask(__name__)
#Bootstrap(app)
@app.route('/')
def files():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print(response)
    for bucket in response['Buckets']:
        s3 = boto3.resource("s3")
        bucket_name=bucket["Name"]
        my_bucket = s3.Bucket(bucket_name)
        res=''
        for file in my_bucket.objects.all():
            res = res+ str(file.key) +"</p><br>"
            print(file)
            print(res)
        return res
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085)
