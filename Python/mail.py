import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
body = str({'agentName': 'AVX', 'dataCenter': 'cbe', 'healthCode': 'RED', 'hostName': 'sre-cc-n1.lab.appviewx.net', 'logs': [{'message': 'sre-cc-n1.lab.appviewx.net is added', 'time': 1729890461171, 'type': 'INFO', 'user': 'system'}, {'message': 'Installer update process is completed. Version: 24.0.0.1', 'time': 1729890580744, 'type': 'INFO', 'user': 'system'}, {'message': 'Device added successfully. Response: sre-cc-n1.lab.appviewx.net', 'time': 1729890581613, 'type': 'INFO', 'user': 'SYSTEM'}, {'message': 'sre-cc-n1.lab.appviewx.net status has been updated. Status: Approve', 'time': 1729891105279, 'type': 'INFO', 'user': 'hariharasudan.yogasamy_ext@appviewx.com'}, {'message': 'Cloud Connector is DOWN', 'time': 1729891106437, 'type': 'INFO', 'user': 'SYSTEM'}, {'message': 'Cloud Connector is Up and Running', 'time': 1729891621308, 'type': 'INFO', 'user': 'SYSTEM'}, {'message': 'Cloud Connector is DOWN', 'time': 1729897866745, 'type': 'INFO', 'user': 'SYSTEM'}, {'message': 'Cloud Connector is Up and Running', 'time': 1729898046421, 'type': 'INFO', 'user': 'SYSTEM'}, {'message': 'Cloud Connector is DOWN', 'time': 1730242200757, 'type': 'INFO', 'user': 'SYSTEM'}], 'tenantId': 'internal-saas-ca-prod', 'version': '24.0.0.1'}
)
def send_text_email(to_email, subject, body):
    from_email = "hariharasudan.yogasamy_ext@appviewx.com"
    password = "ohrp pdki hxbo uuim"

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
    
    # Create SMTP session for sending the mail
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Enable security
            server.login(from_email, password)  # Login with email and password
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Usage
send_text_email("pavish.kannadasan@appviewx.com", "Subject of the Email", body)
