from flask import Flask, request, Response
import requests
import re
import json


#Comandos de interação com a API do Telegram

# https://api.telegram.org/bot1340265163:AAFcWrGSFvksnifXziCxYT9sGVjRbuMEwfI/setWebhook?url=https://llmf-bot.herokuapp.com
#https://api.telegram.org/bot1340265163:AAFcWrGSFvksnifXziCxYT9sGVjRbuMEwfI/setWebhook?url=https://03059e341845.ngrok.io
#https://api.telegram.org/bot1340265163:AAFcWrGSFvksnifXziCxYT9sGVjRbuMEwfI/getMe
#https://api.telegram.org/bot1340265163:AAFcWrGSFvksnifXziCxYT9sGVjRbuMEwfI/deleteWebhook
#https://api.telegram.org/bot1340265163:AAFcWrGSFvksnifXziCxYT9sGVjRbuMEwfI/getUpdates
#https://api.telegram.org/bot1340265163:AAFcWrGSFvksnifXziCxYT9sGVjRbuMEwfI/sendMessage?chat_id=61212817&text=laureano-respondendo

TOKEN = "1340265163:AAFcWrGSFvksnifXziCxYT9sGVjRbuMEwfI"

#URL = "https://llmf-bot.herokuapp.com"
URL = "https://03059e341845.ngrok.io"

app = Flask(__name__)


def parse_message(message):
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    pattern = r'/[a-zA-Z]{2,5}'
    ticker = re.findall(pattern, txt)
    if(ticker):
        #symbol = ticker[0][1:].upper()
        symbol = ticker[0][1:].lower()
    else:
        symbol = ''
    return chat_id, symbol

def send_message(chat_id, text='bla bla bla...'):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=payload)
    return r



@app.route("/", methods=['GET','POST'])
def index():
    if (request.method=='POST'):
        msg = request.get_json()
        chat_id, symbol = parse_message(msg)
        if(not symbol):
            send_message(chat_id, 'Comando não reconhecido!')
            return Response("Ok", status=200)
        # aqui trato o comando específico
        send_message(chat_id, f'Comando recebido:{symbol}')
       
        #with open('telegram_request.json', 'w', encoding='utf-8') as f:
        #    json.dump(msg, f, ensure_ascii=False, indent=4)
        return Response("Ok", status=200)
    else:
        return '<h1>Aplicação preparada para trabalhar apenas com Http Post</h1>'


if __name__ == "__main__":
    app.run(host="localhost", port=8443, debug=True)
    
