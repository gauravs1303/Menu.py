import os
print("\t"+40*"-")
print("\t\t\tWelcome To AWS Menu")
print("\t"+40*"-")
while True:
    print("\n\t"+34*"*")
    print("\tselect one option")
    print("\t"+34*"*")
    print("\n\tIf AWS CLI is NOT Installed : Press 1")
    print("\n\tFor AWS Menu : Press 2")
    print("\n\tTo Exit : Press 3")
    ah=int(input("Enter Your Choice : "))

    if ah==1:
        os.system("curl 'https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.0.30.zip' -o 'awscliv2.zip'")
        os.system('unzip awscliv2.zip')
        os.system('sudo ./aws/install')
        os.system('aws configure')
    elif ah==2:
         while True:
            print("AWS is Configured")
            print('To create a Key-Pair : Press 1')
            print('To Create a Security Group : Press 2')
            print('To allow a port no. in the SG : Press 3')
            print('To Launch EC2 Instance with a Key-Pair & SG : Press 4')
            print('To Create an EBS Volume : Press 5')
            print('To Attach an EBS Volume To an EC2 Instance : Press 6')
            print('To Create a S3 bucket : Press 7')
            print('To Upload a object in S3 bucket : Press 8')
            aws=int(input("Enter Your Choice :"))

            if aws==1:
                key=input("Name Of Key :")
                op=input("File Name To save PEM key locally :")
                os.system(f'aws ec2 create-key-pair  --key-name {key}  --query KeyMaterial --output text > {op}.pem')
            elif aws==2:
                sg=input("Name of S.G. :")
                description=input("Description :")
                os.system(f'aws ec2 create-security-group --group-name {sg} --description {description}')
            elif aws==3:
                authsg=input("Name of S.G. :")
                ptocol=input("Protocol :")
                pn=input("Port no. :")
                os.system(f'aws ec2 authorize-security-group-ingress --group-name {authsg}  --protocol {ptocol}  --port {pn}  --cidr 0.0.0.0/0')
            elif aws==4:
                img=input("AMI ID :")
                cnt=input("No. of Instance You want to Launch :")
                itype=input("Instance Type :")
                ikey=input("Name of key pair which we want to attach to the Instance :")
                isg=input("Name of S.G. which we want to attach to the Instance :")
                os.system(f'aws ec2 run-instances --image-id {img}  --count {cnt} --instance-type {itype}')
            elif aws==5:
                az=input("Availability Zone :")
                vsize=int(input("Size of Volume in GiB :"))
                os.system(f'aws ec2 create-volume --availability-zone {az} --size {vsize}')
            elif aws==6:
                denm=input("Device Name(like /dev/sdf) :")
                insid=input("Instance ID :")
                vid=input("Volume ID :")
                os.system(f'aws ec2 attach-volume --device {denm} --instance-id {insid} --volume-id {vid}')
            elif aws==7:
                bname=input("Name of Bucket :")
                bregn=input("Region :")
                os.system(f'aws s3api create-bucket  --bucket {bname}  --region {bregn}  --create-bucket-configuration LocationConstraint={bregn}')
            elif aws==8:
                bname=input("Bucket Name :")
                path=input("Path of the Object :")
                key=input("Key Name :")
                os.system(f'aws s3api put-object  --acl public-read  --bucket {bname} --body {path}  --key {key}')

    elif ah==3:
        exit()
