#!/usr/bin/env python3
import cgi
import json

form = cgi.FieldStorage()
day = form.getfirst("day1")

print("Content-type: text/html")
print()

with open('C:\\Users\\mkhol\\Desktop\\site\\cgi-bin\\duty.json', 'r', encoding='utf-8') as f:
	json_data = json.load(f)
for todo in json_data:
	gr = todo["groupName"]
	for each in todo["usersDutyList"]:
		i = each["userFullname"]
		i2 = each["userEmail"]
		i3 = each["userPhone"]
		for each2 in each["dutyDays"]:
			if each2["day"] == day and each2["isDuty"] == "true":
				print(gr + " " + i + " " + i2 + " " + i3 + "<br>")