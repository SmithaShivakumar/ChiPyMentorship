from twilio.rest import TwilioRestClient

account_sid = "AC0cf3f69bfe837323a5d98bf4231faa8b" # Your Account SID from www.twilio.com/console
auth_token  = "015f69974b48c793d9c03b3435ec3a4f"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+13129180437",    # Replace with your phone number
    from_="+13475149550") # Replace with your Twilio number

print(message.sid)