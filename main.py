from requests import get
import boto3

print("Starting DHCP auto updater")

# Program start
ip = get('https://api.ipify.org').text
sts_client = boto3.client('sts')


print('Public IP address is: {}'.format(ip))


