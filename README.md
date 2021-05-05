### Billing Report
![Billing_Report](https://user-images.githubusercontent.com/82746623/116860032-8e389000-ac1e-11eb-8938-bf0250f3e600.PNG)
### EC2 Instance
![Ec2_Browser](https://user-images.githubusercontent.com/82746623/116860086-a27c8d00-ac1e-11eb-98c0-e4eded7bb03b.PNG)
### S3 Bucket 
![s3_Bucket_screenshot](https://user-images.githubusercontent.com/82746623/116860106-ac05f500-ac1e-11eb-8305-941bb7b81269.PNG)
# AWS-Training
Launch EC2 instance and choose AMI as "Ubuntu server"
select instance type "t2.micro" free tier
select Add storage size 8 GiB
Tag key name and configure security group TCP and port number 8085
Screen shot of Billing Report.

### Virtual Environment
Ubuntu 20.04LTS
$ sudo apt-get update

### AWS Installation and Configuration
$ sudo apt install awscli
$ aws --version:
aws-cli/1.18.69 Python/3.8.5 Linux/4.4.0-19041-Microsoft botocore/1.16.19 
$ sudo chmod 400 pranita.pem 
$ ssh -i pranita.pem ubuntu@ec2-3-6-40-36.ap-south-1.compute.amazonaws.com
$ aws configure
AWS Access Key ID [****************VMDF]: "AKIAQ4IWYKPL6AWTVMDF"
AWS Secret Access Key [****************V7HP]: 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
Default region name [Asia Pacific (Mumbai)ap-south-1]: ap-south-1
Default output format [JSON]: json

$ sudo apt install pipenv
$ pipenv install --three

$ pipenv shell
$ pipenv install flask
$ pipenv install boto3
$ pipenv flask_bootstrap
$ sudo nano app.py
$ python app.py

