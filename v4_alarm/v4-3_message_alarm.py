from twilio.rest import Client
account_sid = 'sid'
auth_token = 'token'
client = Client(account_sid, auth_token)
message = client.messages.create(
    to='phonenumber',
    from_='number',
    body='Hello'
)
print(message.sid)
print("SUCCESS")