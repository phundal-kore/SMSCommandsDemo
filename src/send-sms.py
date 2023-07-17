import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# Sim to send message to communicate with (sid or unique_name)
sid = "HSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

message = input("Message to send: ")

message_payload = message

sms_command = client.supersim.v1.sms_commands.create(
                                                  sim=sid,
                                                  payload=message_payload
                                              )

print ("SMS sid: ",sms_command.sid)
print ("Status: ",sms_command.status)
print ("Direction: ", sms_command.direction)
print ("URL to check status: ", sms_command.url)