import requests

url = 'https://srelab-prov.apps.appviewx.io/avxapi/visualworkflow-submit-request?gwsource=WEB&gwkey=f000ca01'

payload = '{"payload":{"header":{"workflowName":"DB_Collection_Hari"},"data":{"input":{"requestData":[{"sequenceNo":1,"scenario":"scenario","fieldInfo":{"tenant_id":"testfw1","collections":"usergroup,saas_agent_meta"}}]},"globalData":{},"task_action":1}}}'

headers = {
  "Content-Type" : "application/json",
  "username" : "hari",
  "password" : "Appviewx@123"
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)