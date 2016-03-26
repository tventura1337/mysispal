from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
import time

SERVER_NUMBER = "+19782777642"
SID = "AC8809125b1779b4fc3b272e334ce5c05c"
TOKEN = "8809125b1779b4fc3b272e334ce5c05c"

app = Flask(__name__)

@app.route("/")
def sms_echo():
    client = TwilioRestClient(SID, TOKEN)
    clientNumber = request.args.get('From')
    clientTextContent = request.args.get('Body').lower()
    client.sms.messages.create(to=clientNumber, from_=SERVER_NUMBER, body = clientTextContent)
    return "HelloWorld"

if __name__ == "__main__":
    app.run(debug=True)