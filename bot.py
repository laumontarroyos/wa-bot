from flask import Flask, request
import requests
import json
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '')
    #print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    
    if 'Hi' in incoming_msg or 'Hey' in incoming_msg or 'Heya' in incoming_msg or 'Menu' in incoming_msg:
        text = f'Hello 🙋🏽‍♂, \nThis is a Covid-Bot.'
        msg.body(text)
        responded = True

    if 'A' in incoming_msg:
        # return total cases
        r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
        if r.status_code == 200:
            data = r.json()
            text = f"""_Covid-19 Cases Worldwide_ \n\nConfirmed Cases : *{data["cases"]}* \n\nDeaths : *{data["deaths"]}*
             \n\nRecovered : *{data["recovered"]}*  \n\n 👉 Type *B* to check cases in *India* \n 👉 
             Type *B, C, D* to see other options \n 👉 Type *Menu* to view the Main Menu"""
            print(text)
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True

    if 'B' in incoming_msg or 'India' in incoming_msg:
        # return cases in india
        r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/india')
        if r.status_code == 200:
            data = r.json()
            text = f"""_Covid-19 Cases in India_ \n\nConfirmed Cases : *{data["cases"]}* \n\nToday Cases :
             *{data["todayCases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}* \n\n 👉 
             Type *C* to check cases in *China* \n 👉 Type *A, C, D* to see other options \n 👉 Type 
             *Menu* to view the Main Menu"""
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True

    if 'C' in incoming_msg or 'China' in incoming_msg:
        # return cases in china
        r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/china')
        if r.status_code == 200:
            data = r.json()
            text = f"""_Covid-19 Cases in China_ \n\nConfirmed Cases : *{data["cases"]}* \n\nToday Cases :
             *{data["todayCases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}* 
             \n\nActive Cases : *{data["active"]}* \n\n 👉 Type *D* to check cases in *USA* \n 👉 
             Type *A, B, D* to see other options \n 👉 Type *Menu* to view the Main Menu"""
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True
    
    if 'D' in incoming_msg or 'USA' in incoming_msg:
        # return cases in usa
        r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/usa')
        if r.status_code == 200:
            data = r.json()
            text = f"""_Covid-19 Cases in USA_ \n\nConfirmed Cases : *{data["cases"]}* \n\nToday Cases : 
            *{data["todayCases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}* 
            \n\nActive Cases : *{data["active"]}*  \n\n 👉 Type *E* to check cases in *Italy* \n 👉
             Type *A, B, C* to see other options \n 👉 Type *Menu* to view the Main Menu"""
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True
  
    if responded == False:
        msg.body('I only know about corona, sorry!')

    return str(resp)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
