import sys
import datetime
import json
from twilio.rest import TwilioRestClient

def main():
    time = importlib.import_module('time')
    if len(sys.argv) != 2:
        print "Invalid command line argument count, get_grade only accepts one arg."
        sys.exit(1)

    info = parse_json(sys.argv[1])
    phone = info["phone"]

    today = datetime.date.today()
    today = datetime.datetime.combine(today, datetime.time(0, 0))
    advising_date = datetime.datetime(2016, 04, 04)

    year = advising_date.year
    month = advising_date.month
    day = advising_date.day
    date = str(year) + '/' + str(month) + '/' + str(day)

    if today < advising_date:
        advising_message = "Advising started on " + date + " get on top of that!"
    else:
        advising_message =  "Advising starts on " + date + "."

    send_text(advising_message, phone)

def parse_json(data):
    with open('data.json') as data_file:
        j = json.loads(data_file.read())
    d = {}
    d["phone"] = j["phoneNumber"]
    return d

def send_text(my_str, to_phone):
    phone_num = "+19782777642"
    account_sid = "AC8809125b1779b4fc3b272e334ce5c05c"
    auth_token = "41b42845c2ccf8556b1041342092d6d6"
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to=to_phone, from_= phone_num,
                                                 body=my_str)
if __name__ == '__main__':
    main()
