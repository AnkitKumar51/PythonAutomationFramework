from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = 'ACead897b8e1b205bad36f2cda138beadb'
auth_token = '4bae7055bc72e496ea19a39455946e8f'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Make a call
call = client.calls.create(
    to='+91 ',  # Replace with the recipient's phone number
    from_='+12294045536',  # Replace with your Twilio phone number
    url='http://demo.twilio.com/docs/voice.xml'  # Replace with the URL of TwiML XML or Bin containing call instructions
)

print("Call SID:", call.sid)
