from utils.credentials import Credentials
import boto3
import yaml
from requests import get

print("Starting DHCP auto updater")

# Program start
ip = get('https://api.ipify.org').text
session = boto3.Session()
credentials = Credentials().get_credentials()


print('Public IP address is: {}'.format(ip))

