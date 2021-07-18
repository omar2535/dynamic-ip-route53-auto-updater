from utils.HostedZone import HostedZone
from utils.Credentials import Credentials
import boto3
from requests import get

print("Starting DHCP auto updater")

# Program start
ip = get('https://api.ipify.org').text
credentials = Credentials()
hosted_zones = HostedZone()

session = boto3.Session(
    aws_access_key_id=credentials.get_aws_access_key_id,
    aws_secret_access_key=credentials.get_aws_secret_access_key
)

route53_client = session.client('route53')

change_batch = {
    'Comment': 'Update A-records from dynamic IP',
    'Changes': []
}

for record in hosted_zones.get_records():
    change = {}
    change['Action'] = 'UPSERT'
    change['ResourceRecordSet'] = {}
    change['ResourceRecordSet']['Name'] = record['record_name']
    change['ResourceRecordSet']['Type'] = record['record_type']
    change['ResourceRecordSet']['ResourceRecords'] = [{'Value': ip}]
    change_batch['Changes'].append(change)



print("Complete")
