# This example requires the requests library be installed.  You can learn more
# about the Requests library here: http://docs.python-requests.org/en/latest/
from requests import get

print("Starting DHCP auto updater")

# Program start
ip = get('https://api.ipify.org').text
print('Public IP address is: {}'.format(ip))



