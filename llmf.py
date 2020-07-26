from flask import Flask, request
import requests
import json
import logging
import telegram
#from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                    level=logging.INFO)

#logger = logging.getLogger(__name__)

global bot
global TOKEN
TOKEN = "1340265163:AAFcWrGSFvksnifXziCxYT9sGVjRbuMEwfI"
bot = telegram.Bot(token=TOKEN)
URL = "https://llmf-bot.herokuapp.com"
#URL = "http://localhost:5000"
#URL = "https://893e4c2528a1.ngrok.io"
#URL = "https://bb61b29222fa.ngrok.io"

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def hello():
    return "Hello World!"

@app.route('/llmf', methods=['POST'])
def llmf():
    return "Laureano..."

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    print("iniciou...")
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    # get the chat_id to be able to respond to the same user
    chat_id = update.message.chat.id
    # get the message id to be able to reply to this specific message
    msg_id = update.message.message_id
    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8').decode()
    print("got text message :", text)
    # here we call our super AI
    response = "Uma resposta simples..."
    # now just send the message back
    # notice how we specify the chat and the msg we reply to
    bot.sendMessage(chat_id=chat_id, text=response, reply_to_message_id=msg_id)
    return 'ok'


@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    # we use the bot object to link the bot to our app which live
    # in the link provided by URL
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    # something to let us know things work
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"   

if __name__ == "__main__":
    app.run(host="localhost", port=8443, debug=True)
    
