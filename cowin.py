import requests
import json
from datetime import datetime,timedelta

today = datetime.today()
pin = ["481001"]
num_day = 7
all_dates =[]
for i in range(num_day):
    all_dates.append(today+timedelta(i))

final_dates =[]
for i in all_dates:
    final_dates.append(i.strftime("%d%m%y"))

while True:
    for p in pin:
        for d in final_dates:
            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(p,d)
            result = requests.get(URL)
            result_json = result.json()
            if result_json["centers"]:
                for center in result_json["centers"]:
                    for session in center["sessions"]:
                        if session["vaccine"] == "COVAXIN" and session["available_capacity_dose2"] >0:
                            print("pincode:"+p)
                            print("date: "+d)
                            print("Center name "+center["name"])
                            print("center add "+center["address"])
                            print("No. of vaccine ", session["available_capacity"])
                            print("Vaccine Type : ", session["vaccine"])


