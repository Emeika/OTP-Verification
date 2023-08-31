
#  https://www.twilio.com/docs/python/install
import os

account_sid = "ACab63003efa220ec00aecd5d58f7f5201"
auth_token = "df9029bb0b6089f9f555f0a15b831f00"
verify_sid = "VA8498a04cd2fe15e4a00b20e3ed9eb0f3"
verified_number = "+923104382249"

client = Client(account_sid, auth_token)

verification = client.verify.v2.services(verify_sid) \
  .verifications \
  .create(to=verified_number, channel="sms")
print(verification.status)

otp_code = input("Please enter the OTP:")

verification_check = client.verify.v2.services(verify_sid) \
  .verification_checks \
  .create(to=verified_number, code=otp_code)
print(verification_check.status)




# Your Account SID from twilio.com/console
account_sid = "ACab63003efa220ec00aecd5d58f7f5201"
# Your Auth Token from twilio.com/console
auth_token  = "df9029bb0b6089f9f555f0a15b831f00"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+923104382249", 
    from_="+923104382249",
    body="Hello from Python!")

print(message.sid)