import pymongo
from pymongo import MongoClient
import paramiko
import json
import os

# MongoDB Atlas connection details
ATLAS_CONNECTION_STRING = "your_atlas_connection_string"
DB_NAME = "your_database_name"
COLLECTION_NAME = "your_collection_name"

# Remote machine details
REMOTE_HOST = "your_remote_host"
REMOTE_USER = "your_remote_username"
REMOTE_PASSWORD = "your_remote_password"
REMOTE_FILE_PATH = "/path/to/remote/file.json"

# Connect to MongoDB Atlas
client = MongoClient(ATLAS_CONNECTION_STRING)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Fetch data from MongoDB Atlas
data = list(collection.find({}))

# Remove ObjectId fields (they're not JSON serializable)
for doc in data:
    doc.pop('_id', None)

# Convert data to JSON
json_data = json.dumps(data, indent=2)

# Set up SSH client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote machine using password
ssh_client.connect(
    hostname=REMOTE_HOST,
    username=REMOTE_USER,
    password=REMOTE_PASSWORD
)

# Open an SFTP session
sftp = ssh_client.open_sftp()

# Write the JSON data to a file on the remote machine
with sftp.file(REMOTE_FILE_PATH, 'w') as remote_file:
    remote_file.write(json_data)

# Close the SFTP session and SSH connection
sftp.close()
ssh_client.close()

print(f"Data successfully copied to {REMOTE_FILE_PATH} on the remote machine.")