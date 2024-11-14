import paramiko
from scp import SCPClient

def create_ssh_client(server, port, user, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port=port, username=user, password=password)
    return client

def transfer_file(ssh_client, local_file, remote_file):
    with SCPClient(ssh_client.get_transport()) as scp:
        scp.put(local_file, remote_file)

def execute_command(ssh_client, command):
    stdin, stdout, stderr = ssh_client.exec_command(command)
    return stdout.read().decode(), stderr.read().decode()

def main():
    server = '3.111.166.145'
    port = 22  # Default SSH port
    user = 'appviewx'
    password = 'appviewx@123'  # or use a private key

    # Create SSH client
    ssh_client = create_ssh_client(server, port, user, password)

    # Transfer a file to the remote node
    local_file = '/home/sreadmin/collection-spark-nz-prod.zip'
    remote_file = '/home/appviewx'
    transfer_file(ssh_client, local_file, remote_file)

    # Execute a command on the remote node
    command = 'ls -l'  # Example command
    output, error = execute_command(ssh_client, command)

    print("Output:", output)
    print("Error:", error)

    # Close the SSH connection
    ssh_client.close()

if __name__ == "__main__":
    main()