from twilio.rest import Client
from datetime import datetime
import time

account_sid = "AC3f9ad355c421fc9257b3b5b1e84fe4be"
auth_token = "31184f2aeae66f4a44bd55df4182c203"

def send_sms(to,text,tw_mobile="+13307087414"):
    client=Client(account_sid, auth_token)
    try:
        message=client.messages.create(
                                        body=text,
                                        from_=tw_mobile,
                                        to=to)
        print("message status:",message.status)
        return True
    except Exception as e:
        print (e)
        return False

if __name__=="__main__":
    greetings={"8":"早上好，该起床了","13":"中午好，该吃午饭啦",
               "15":"傍晚好，该吃晚饭了","20":"晚上好，该睡觉啦"}
    print("Script running")
    while True:
        now=datetime.now()
        print("time:",now)
        for key in greetings.keys():
            if now.hour==int(key):
                message=greetings.get(key,"This is a test message")
                res=send_sms(to="+8618059201043",text=message)
                if res:
                    print("Message send ok at:",
                          datetime.strftime(now,"%Y-%m-%d %H:%M:%S"))
                    time.sleep(60*60)
                else:
                    print("Message send failed!")
        time.sleep(5)
            
