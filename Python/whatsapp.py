from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'ACc38097be29b1526bb45aae98b5520c83'
auth_token = '7080b30d0848ceab2fdf8b78a4caad97'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Your Twilio WhatsApp sandbox number and the recipient's number
twilio_whatsapp_number = '+18167590226'  # This is Twilio's sandbox number
recipient_whatsapp_number = '+919942860606'  # Replace with the recipient's number

# Message to send
message_body = 'Hello, this is a message sent from Python using Twilio!'

# Send the message
message = client.messages.create(
    body=message_body,
    from_=twilio_whatsapp_number,
    to=recipient_whatsapp_number
)

# Print the SID of the message
print(f"Message sent with SID: {message.sid}")
