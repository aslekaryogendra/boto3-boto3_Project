import boto3

# get vpc info: https://hands-on.cloud/boto3-vpc-python-tutorial/



ec2_Client = boto3.client('ec2')
response=ec2_Client.describe_regions()
# print(response['Regions'])
# print('===============================================')
regionList=[]
for region in response['Regions']:
    regionList.append(region['RegionName'])

serviceList=['ec2','s3','vpc','subnet','rds','elb']
for region in regionList:
    # print("\n Region: ",region)
    # session=boto3.Session(region_name=region)
    # print("\n Session_Region_Name: ",session.region_name)
    # print(session.get_available_services() )
    for service in serviceList:
        session=boto3.Session(region_name=region)
        # print("\n Session_Region_Name: ",session.region_name)
        if service in ['ec2']:
            client=boto3.client(service,region_name=region)
            Myec2=client.describe_instances()
            for pythonins in Myec2['Reservations']:
                for printout in pythonins['Instances']:
                        print(printout['InstanceId'])
                        print(printout['InstanceType'])
                        print(printout['State']['Name'])






