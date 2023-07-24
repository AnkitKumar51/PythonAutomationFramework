from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = 'ACead897b8e1b205bad36f2cda138beadb'
auth_token = '4bae7055bc72e496ea19a39455946e8f'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Replace 'your_twilio_phone_number' with your Twilio phone number
twilio_phone_number = '+12294045536'

# Replace 'recipient_phone_number' with the recipient's phone number
recipient_phone_number = '+91 '

# The message you want to send
message_body = "Hello from Twilio! This is a test SMS message."

try:
    # Send the SMS message
    message = client.messages.create(
        body=message_body,
        from_=twilio_phone_number,
        to=recipient_phone_number
    )
    print("SMS sent successfully!")
    print("Message SID:", message.sid)
except Exception as e:
    print("Error occurred while sending the SMS:", str(e))
