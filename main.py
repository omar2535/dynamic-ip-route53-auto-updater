from utils.credentials import Credentials
import boto3
from requests import get

print("Starting DHCP auto updater")

# Program start
ip = get('https://api.ipify.org').text
credentials = Credentials()
session = boto3.Session(
    aws_access_key_id=credentials.get_aws_access_key_id,
    aws_secret_access_key=credentials.get_aws_secret_access_key
)
route53_client = session.client('route53')


print("Complete")

