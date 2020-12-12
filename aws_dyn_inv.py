#!/usr/bin/python
import sys
import json
try:
    import boto3
except Exception as e:
    ptint(e)
    print("please rectify above exception and try again")
    sys.exit(1)

def get_hosts(ec2_obj,a):
    b={"Name":"tag:tag" , "Values": [a]}
    hosts=[]
    for each_in in ec2_obj.instances.filter(Filters=[b]):
        hosts.append(each_in.private_ip_address)
    return hosts 

def main():
    ec2_obj=boto3.resource("ec2","us-east-2")
    db_group=get_hosts(ec2_obj,'db')
    app_group=get_hosts(ec2_obj,'app')
    all_groups={ 'db': db_group, 'app': app_group}
    print(json.dumps(all_groups))

if __name__=="__main__":
    main()
