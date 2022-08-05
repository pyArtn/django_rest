# import requests

# def send_telegram(text: str):
#     token = "5500002240:AAHMhZA0m6DSS3OafPkEP_RTlXIVF8CwACo"
#     url = "https://api.telegram.org/bot"
#     channel_id = "@it_асаdеmу"
#     url += token
#     method = url + "/sendMessage"

#     r = requests.post(method, data={
#          "chat_id": channel_id,
#          "text": text
#           })

#     if r.status_code != 200:
#         raise Exception("post_text error")

# if __name__ == '__main__':
#   send_telegram("Билли харинктон")



from ast import While
from urllib import response
import requests


def send_telegram(text: str) -> response:
    try:
        token = "5500002240:AAHMhZA0m6DSS3OafPkEP_RTlXIVF8CwACo"
        url = "https://api.telegram.org/bot"
        channel_id = "-613105778"
        url += token    
        method = url + "/sendMessage"
        r = requests.post(method, data={
            "chat_id": channel_id,
            "text": text
        })
        if r.status_code == '200':
            return 'eeee'
        else:
            return r.status_code
    except Exception as ex:
        print(ex)
