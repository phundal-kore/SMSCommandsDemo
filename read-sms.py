import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# Sim to send message to communicate with (sid or unique_name)
sid = "HSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

sms_commands = client.supersim.v1.sms_commands.list(limit=20)

count = 1
print("Messages for (newest first): ", sid)
for record in sms_commands:
    if (record.sim_sid == sid):
        print("Record: ", count)
        print("\t Direction: ", record.direction)
        print("\t Message: ", record.payload)
        print("\t Status: ", record.status)
        count += 1