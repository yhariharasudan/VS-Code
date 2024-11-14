from configobj import ConfigObj
import json, os
import zipfile
import urllib3
from datetime import datetime
import pymongo
from pymongo import MongoClient , errors
from bson.json_util import dumps
import paramiko
from scp import SCPClient
import shutil

http = urllib3.PoolManager()
tenant_name = "<%tenant_id%>"
tenant_id="<%tenant_id%>" + ".appvx.com"
collections = "<%collections%>"
collections = collections.strip().split(",") if collections != '' else None
AVX::LOG("tenant_id = " + tenant_id)
output_dir = 'json_collections'
os.makedirs(output_dir, exist_ok=True)
zip_file=f'{tenant_name}_collections-' + datetime.now().strftime("%d_%m_%y") + '.zip'

username = "<%username%>"
#AVX::LOG(zip_file)
#os.chdir(output_dir)
'''Get Gateway URL'''
pwd = os.path.dirname(os.path.abspath(__file__))
properties_path = os.path.join(pwd, "../properties/appviewx.properties")
avx_properties = ConfigObj(properties_path)
gw_url = avx_properties['GATEWAY_BASE_URL']
gw_key = avx_properties['GATEWAY_KEY']
gw_url = gw_url if gw_url.endswith('/') else gw_url + "/"

url = gw_url + "avxapi/saas-get-all-snapshot-by-clustername-region?gwkey=f000ca01&gwsource=external&region=<%region%>&clusterName=<%mongoCluster%>&validateThreshold=true"
headers = {
	"Content-Type": "application/json",
	"sessionId": "<%sessionId%>",
	"Accept": "application/json"
}


def decyrpt_process(pwd):
    """
    Helps to decrpt the password using the jar files
    """
    header_data = {"Content-Type": "application/json"}
    url = "http://localhost:9090/services/decrypt?gwsource=test"
    pwd = pwd.get("encryptedValue", "")
    data = {"payload": pwd}
    method = "POST"
    encoded_data = json.dumps(data).encode("utf-8")
    http = urllib3.PoolManager(cert_reqs="CERT_NONE")
    try:
        response = http.request(method, url=url, body=encoded_data, headers=header_data)
        if response.status == 200:
            response = json.loads(response.data.decode("utf-8"))
            return response.get("response")
        else:
            raise Exception(
                "Error while getting password : "
                + str(json.loads(response.data.decode("utf-8")))
            )
    except Exception as e:
        raise Exception("Error while getting password : " + str(e))

#########################################################################
def get_mongo_details(tag_name):
	try:
		url = gw_url + "avxapi/saas-get-paired-cluster-by-tagname?gwkey=f000ca01&gwsource=external&tagName=" + tag_name
		
		headers = {
			"Content-Type": "application/json",
			"sessionId": "<%sessionId%>",
			"Accept": "application/json"
		}

		response = http.request("GET", url, headers=headers)
		#AVX::LOG(reponse.data[0]["response"])
		if response and response.status == 200:
			for i in json.loads(response.data)["response"]:
				if i["clusterType"] == "DB":
					mongoUserName = i["accessDetails"]["username"]
					mongoPwd = decyrpt_process(i["accessDetails"]["password"])
				
		return mongoUserName, mongoPwd
	except Exception as e:
		AVX::LOG("Error in DB Cluster details")
		AVX::LOG(repr(e))
		return None
#################################################################################

def get_tenant_by_id():
	url = gw_url + "avxapi/saas-tenant-get-by-id?gwkey=f000ca01&gwsource=external"
	payload = {
	    "payload":
	        {
				"tenantId": tenant_id
		}
	    
	}
		

	headers = {
		"Content-Type": "application/json",
		"sessionId": "<%sessionId%>",
		"Accept": "application/json"
	}

	response = http.request("POST", url, headers=headers, body=json.dumps(payload))
	if response and response.status == 200:
		return json.loads(response.data)["response"]
	return []



###########################################################


def Connect_db(username,password,url,snap_id):
    try:
        client = MongoClient(f"mongodb+srv://{username}:{password}@{url}/admin")
    except:
        try:
            client = MongoClient(f"mongodb://{username}:{password}@{url}/?authSource=admin")
        except Exception as err:
            err = str(err).replace(password,"")
            AVX::LOG(f"Unable to connect to DB. Error - {err}")
            AVX::OUTPUT({},2)
    #AVX::LOG(client)
    db=client[snap_id]
    for collect in collections:
        collection=db[collect]
        files=collection.find()
        if files.count() == 0:
            AVX::LOG(f"No files found in the {collect} collection.")
        else:
            with open(os.path.join(output_dir, f"{collect}.json"), 'w') as json_file:
                json_file.write('[')
                for i, file in enumerate(files):
                     json_file.write(dumps(file))
                     if i < files.count() - 1:
                        json_file.write(',')
                json_file.write(']')
            
            with zipfile.ZipFile(zip_file, 'w') as zipf:
                for root, _, files in os.walk(output_dir):
                    for file in files:
                        zipf.write(os.path.join(root, file), arcname=file)
            AVX::LOG("All collections have been saved and zipped successfully.")
####################################################################
def ssh():
    try:
        # Create an SSH client
        client = paramiko.SSHClient()
       
        # Automatically add the remote server's SSH key
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the remote server
        client.connect(hostname="192.168.151.21", username="sreadmin", password="appviewx@123")

        # Execute the bash script
        stdin, stdout, stderr = client.exec_command("cd collections")
        # Get the output and errors
        
     
        #current_directory = os.getcwd()
        #AVX::LOG(os.listdir(current_directory))
        password = "appviewx@123"    
        #AVX::LOG(os.path.join(output_dir))
        local =zip_file
        #AVX::LOG(local)
        remote="/home/sreadmin/collections"
        #AVX::LOG(remote)
        #AVX::LOG("SSH Current Working Directory:"+ os.getcwd())
        #AVX::LOG(os.listdir(output_dir))
        with SCPClient(client.get_transport()) as scp:
            scp.put(local , remote)
            AVX::LOG(f'File {zip_file} copied to node 192.168.151.21 Path {remote}')
        
        
        commands = [f"cp {zip_file} /home/{username}",f"chown {username}: /home/{username}/{zip_file}"]
        
        for command in commands:
            stdin, stdout, stderr = client.exec_command(f"sudo -S {command}", get_pty=True)
            stdin.write(password + "\n")
            stdin.flush()
            #output = stdout.read().decode()
            #error = stderr.read().decode()
            #if output:
                #AVX::LOG(f"Output:\n{output}")
            #if error:
               # AVX::LOG(f"Error:\n{error}")
    
    except Exception as e:
        AVX::LOG(f"Error occurred: {e}")
    
    finally:
        # Close the SSH connection
        
        client.close()


###########################################################3
if __name__ == '__main__':
    try:
        
        output = get_tenant_by_id()
        if len(output) == 0:
            AVX::LOG("Check tenant name")
        #AVX::LOG(output)
        dbinfo=output["dbInfo"]
        #AVX::LOG(dbinfo)
        
        mongoUserName, mongoPwd = get_mongo_details(dbinfo["tagName"])
        #AVX::LOG("mongoUserName = " + str(mongoUserName))
        #AVX::LOG("mongoPwd = " + str(mongoPwd))
        #AVX::LOG("clusterurl= " + dbinfo["url"])
        snap_id=dbinfo["dbSnapshotId"] + "@appviewx"
        tenant_name=output["tenantName"]
        AVX::LOG("tenantName = " + tenant_name)
        AVX::LOG("snapshotId = " + snap_id)
        AVX::LOG("tagname= " + dbinfo["tagName"])
        Connect_db(mongoUserName,mongoPwd, dbinfo["url"],snap_id)
        
        
        ssh()
        
        #AVX::LOG("Current Working Directory:"+ os.getcwd())
        
        
        
       
    except Exception as e:
        AVX::LOG(str(e))
        AVX::OUTPUT({}, 2)
