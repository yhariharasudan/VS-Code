import requests , json

url = "https://srelab-prov.apps.appviewx.io/avxapi/collection-operations?gwkey=f000ca01&gwsource=external"

payload = '{"payload":{"collection":"cc-alert","action":"add","documents":[{"tenant_id":"testfw3","cc-name":"newcc3","status":"true"}] } }'
headers = {
    "Content-Type": "application/json",
    "username": "hari",
    "password": "Appviewx@123"
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
#data = json.loads(response.text)