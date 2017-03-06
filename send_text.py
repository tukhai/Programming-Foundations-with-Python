from twilio.rest import TwilioRestClient

account_sid = "AC2de67a7f95e28c75917155162f501f19" # Your Account SID from www.twilio.com/console
auth_token  = "738495af11a164546a03ad98c421327d"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+6591228258",    # Replace with your phone number
    from_="+19493914168") # Replace with your Twilio number

print(message.sid)
