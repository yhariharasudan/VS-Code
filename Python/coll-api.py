import requests , json

url = "https://srelab-prov.apps.appviewx.io/avxapi/collection-get-details?gwkey=f000ca01&gwsource=external"

payload = '{"payload":{"collectionName" : "cc-alert","queryParam" :{"collectionName" : "cc-alert"},"filterValue" : "testfw1"}}'
headers = {
    "Content-Type": "application/json",
    "username": "hari",
    "password": "Appviewx@123"
}

response = requests.request("POST", url, headers=headers, data=payload)
data = json.loads(response.text)
data1 = data['response']['data']
print(data1)
data1[0]['status'] = 'false'
data2 = json.dumps(data1,indent=4)
print(data1)


