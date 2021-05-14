#!/usr/bin/env python3
#import requests

print("Content-type: text/html")
print()
#print("Content-type: text/html")
#print()
#print("	<meta charset='UTF-8'>")
#print("	<title>page</title>")

import json

print("<form id='pole' action = '/cgi-bin/script2.py'>")
print("День <input type='text' name='day'/>")
print("	<br>")
print("<select name='num' form='pole'>")
with open('C:\\Users\\mkhol\\Desktop\\site\\cgi-bin\\duty.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)
for todo in json_data:
    print("<option value='" + str(todo["groupId"]) + "'>" + todo["groupName"] + "</option>")
print("</select>")
print("<button type='sumbit'>Показать дежурного.</button>")
print("</form><br><br>")


print("<form id='pole1' action = '/cgi-bin/script3.py'>")
print("День <input type='text' name='day1'/>")
print("  <br>")
print("<button type='sumbit'>Показать дежурных в этот день.</button>")
print("</form><br><br>")

print("<form id='pole1' action = '/cgi-bin/script4.py'>")
print("<button type='sumbit'>Построить таблицу.</button>")
print("</form><br><br>")