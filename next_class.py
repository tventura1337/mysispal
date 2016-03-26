import sys
import requests
import json
import datetime
from twilio.rest import TwilioRestClient

def req_next_class(email, passwd):
    login_url = "https://www.uml.edu/sso/Auth/Login?returnUrl=/student-dashboard"
    url = "https://www.uml.edu/student-dashboard/api/Enrollment/Classes?term=2530&career=1"
    payload = {"EmailAddress" : email, "Password" : passwd}
    s = requests.Session()
    s.post(login_url, data=payload)
    r = requests.get(url, auth=(email, passwd))
    j = json.loads(r.content)
    def is_past(t):
        c_time = datetime.datetime.strptime(t, '%H:%M:%S').time()
        if c_time > datetime.datetime.now().time():
            return True
        else:
            return False
    upcoming = {}
    for c in j['data']['Classes']:
        for q in c['Sections']:
            for r in q['Meetings']:
                #if r['IsToday'] and not is_past(r['StartTime']):
                if is_past(r['StartTime']):
                    upcoming[c['CourseName']] = r['StartTime']
    my_next_class = min(upcoming, key=upcoming.get)
    return {my_next_class : upcoming[my_next_class]}

#parse_json goes from json file to hashmap
def parse_json(data):
    with open('data.json') as data_file:
        j = json.loads(data_file.read())
    d = {}
    d["email"] = j["account"]
    d["passwd"] = j["password"]
    d["phone"] = j["phoneNumber"]
    return d

def send_text(my_str, to_phone):
    phone_num = "+19782777642"
    account_sid = "AC8809125b1779b4fc3b272e334ce5c05c"
    auth_token = "41b42845c2ccf8556b1041342092d6d6"
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to=to_phone, from_= phone_num, body=my_str)

def main():
    if len(sys.argv) != 2:
        print "Invalid command line argument count, get_grade only accepts one arg."
        sys.exit(1)

    info = parse_json(sys.argv[1])
    email = info["email"]
    passwd = info["passwd"]
    phone = info["phone"]

    next_class = req_next_class(email, passwd)
    for class_name, time in next_class.items():
        msg = "Your next class is " + str(class_name) + " at " + str(next_class[class_name])
        send_text(msg, phone)

if __name__ == '__main__':
    main()
