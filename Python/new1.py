import certifi
import ssl

ssl_context = ssl.create_default_context(cafile=certifi.where())

import requests

response = requests.get(
    'https://api.twilio.com',
    headers={'User-Agent': 'Mozilla/5.0'},
    verify=certifi.where()
)
print(response.status_code)
