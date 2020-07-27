from flask import Flask, request
import requests
import json
import logging
import telegram
#import telegram.bot
#import telegram.ext.
#from telegram.ext import Updater
#from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
#                    level=logging.INFO)
#logger = logging.getLogger(__name__)

#logger = logging.getLogger(__name__)
#
# https://api.telegram.org/bot1340265163:AAFcWrGSFvksnifXziCxYT9sGVjRbuMEwfI/setWebhook?
# url=https://llmf-bot.herokuapp.com
# {"ok":true,"result":true,"description":"Webhook was set"}

#$path = "https://api.telegram.org/bot<yourtoken>
#Since we’ll be receiving updates by means of the webhook, let’s create and populate an array
#  with that update data: $update = json_decode(file_get_contents("php://input"), TRUE)

#Now, for the sake of convenience later on, let’s extract two crucial pieces of data from 
# that update — the chat ID and message (if the update is not caused by a new message, this 
# field might be empty, and we’ll code for that later):
#$chatId = $update["message"]["chat"]["id"];
#$message = $update["message"]["text"];


global bot
global TOKEN
TOKEN = "1340265163:AAFcWrGSFvksnifXziCxYT9sGVjRbuMEwfI"
bot1 = telegram.Bot(token=TOKEN)
URL = "https://llmf-bot.herokuapp.com"


app = Flask(__name__)


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    
    update = telegram.Update.de_json(request.get_json(force=True), bot1)
    print('I am still alive.')
    # retrieve the message in JSON and then transform it to Telegram object
    #update = telegram.Update.de_json(request.get_json(force=True), bot)
    # get the chat_id to be able to respond to the same user
    chat_id = update.message.chat.id
    # get the message id to be able to reply to this specific message
    msg_id = update.message.message_id
    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8').decode()
    
    response = "Uma resposta simples..."
    # now just send the message back
    # notice how we specify the chat and the msg we reply to
    bot1.sendMessage(chat_id=chat_id, text=response, reply_to_message_id=msg_id)
    
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

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route('/llmf', methods=['POST'])
def llmf():
    return "Laureano..."



if __name__ == "__main__":
    app.run(host="localhost", port=8443, debug=True)
    
