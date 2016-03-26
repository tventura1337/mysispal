import sys
import requests
import json
from twilio.rest import TwilioRestClient

def req_grades(email, passwd):

    login_url = "https://www.uml.edu/sso/Auth/Login?returnUrl=/student-dashboard"
    url = "https://www.uml.edu/student-dashboard/api/Enrollment/Classes?term=2510&career=1"

    payload = {"EmailAddress" : email, "Password" : passwd}

    s = requests.Session()
    s.post(login_url, data=payload)

    r = requests.get(url, auth=(email, passwd))
    j = json.loads(r.content)

    my_grades = {}
    for data in j['data']['Classes']:
        my_grades[data["CourseName"]] = data["Grade"]

    current_grades = ""
    for class_name, grade in my_grades.items():
        current_grades += class_name + " : " + grade + "\n"
    return current_grades

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
    message = client.messages.create(to=to_phone, from_= phone_num,
                                                 body=my_str)

def main():
    # takes a json path with username, password, phone number as cmd line args
    # takes current semester (spring 2016 in our case, fall 2015 for test case.)
    # login to student account using username & password.
    # if there is a new grade then updates through twilio text to phone number
    # if they've gotten all their grades then stop checking for the student.

    if len(sys.argv) != 2:
        print "Invalid command line argument count, get_grade only accepts one arg."
        sys.exit(1)

    info = parse_json(sys.argv[1])
    email = info["email"]
    passwd = info["passwd"]
    phone = info["phone"]

    current_grades = req_grades(email, passwd)
    send_text(current_grades, phone)

if __name__ == '__main__':
    main()