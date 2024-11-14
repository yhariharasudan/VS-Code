import base64

message = "30795e0f-2d48-4498-b419-ce82df955754:1gaXViDS4Y$z@ohSE&UhgHRgQhPYPrJM"
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print(base64_message)