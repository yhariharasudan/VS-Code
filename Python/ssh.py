import paramiko

def ssh():
    try:
        # Create an SSH client
        client = paramiko.SSHClient()
       
        # Automatically add the remote server's SSH key
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the remote server
        client.connect(hostname="192.168.151.21", username="sreadmin", password="appviewx@123")
        
        username = "hariharasudan.y"
        filename = "collection-SiriusXMProd.zip"
        password = "appviewx@123"
        commands = [f"cp {filename} /home/{username}",f"chown {username}: /home/{username}/{filename}",f"rm {filename}"]
        # Execute the bash script
        #stdin, stdout, stderr = client.exec_command("pwd")
        #stdin, stdout, stderr = client.exec_command("echo 'appviewx@123' | sudo -S cp collection-next.zip /home/hariharasudan.y")
        for command in commands:
            stdin, stdout, stderr = client.exec_command(f"sudo -S {command}", get_pty=True)
            stdin.write(password + "\n")
            stdin.flush()
        # Get the output and errors
            output = stdout.read().decode()
            error = stderr.read().decode()
        if output:
            print(f"Output:\n{output}")
        if error:
            print(f"Error:\n{error}")

    except Exception as e:
        print(f"Error occurred: {e}")
    
    finally:
        # Close the SSH connection
        client.close()

   
if __name__ == "__main__":
    ssh()