import twilio
from twilio.rest import Client
#下面认证信息的值在你的twilio 账户里可以找到
account_sid="AC3f9ad355c421fc9257b3b5b1e84fe4be"
auth_token="31184f2aeae66f4a44bd55df4182c203"
client=Client(account_sid, auth_token)
message=client.messages.create(to="+8618059201043",#区号+你的手机号码
                                from_="+13307087414",#你的twilio电话号码
                                body="cs")
