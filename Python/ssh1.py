from paramiko import SSHClient, AutoAddPolicy
from sshtunnel import SSHTunnelForwarder

def ssh_via_jump(jump_host, jump_username, jump_password, target_host, target_username, target_password):
    with SSHTunnelForwarder(
        (jump_host, 22),  # Jump server hostname and SSH port
        ssh_username=jump_username,
        ssh_password=jump_password,
        remote_bind_address=(target_host, 22)  # Target server and its SSH port
    ) as tunnel:
        print(f"Tunnel connected via {jump_host} to {target_host}...")
        
        # SSH into the target server via the tunnel
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())

        client.connect(
            '127.0.0.1',  # The SSH connection goes through the local side of the tunnel
            port=tunnel.local_bind_port,
            username=target_username,
            password=target_password
        )

        print(f"Connected to {target_host}")

        # Execute a command on the target server
        stdin, stdout, stderr = client.exec_command('./GangaGA/PROVISIONING/bastion.sh')  # Replace with your command
        output = stdout.read().decode()
        error = stderr.read().decode()

        if output:
            print(f"Output:\n{output}")
        if error:
            print(f"Error:\n{error}")

        client.close()

if __name__ == "__main__":
    # Jump server credentials
    jump_host = 'jump1.appviewx.net'        # Replace with your jump server IP
    jump_username = 'hariharasudan.y'     # Replace with your jump server SSH username
    jump_password = 'Hari@123'     # Replace with your jump server SSH password

    # Target server credentials
    target_host = 'sre-jump-n1.appviewx.net'    # Replace with your target server IP
    target_username = 'sre' # Replace with your target server SSH username
    target_password = '5xR|v4l2O#' # Replace with your target server SSH password

    ssh_via_jump(jump_host, jump_username, jump_password, target_host, target_username, target_password)
