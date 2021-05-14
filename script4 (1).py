#!/usr/bin/env python3
import cgi
import json

form = cgi.FieldStorage()

print("Content-type: text/html")
print()

with open('C:\\Users\\mkhol\\Desktop\\site\\cgi-bin\\duty.json', 'r', encoding='utf-8') as f:
	json_data = json.load(f)
print("<table border=2 align='center'>")
#print("<tr> <td>Имя</td><td>День</td> <td>Дежурный по администрированию 1С (1С админ)</td> <td>Дежурный по виртуализации (VM)</td> <td> Дежурный по инфраструктуре ЦОД (dc)</td> <td>Дежурный по мониторингу (skm)</td> <td>Дежурный по СУБД PostgreSQL (pgSQL)</td> <td>Дежурный по телефонии и КЦ</td> <td>Мониторинг УЦОД 24/7</td></tr>")
print("<tr><td>День</td>")

for todo in json_data:
	print("<td>" + todo["groupName"] + "</td>")
print("</tr>")
i=1
while i<31:
	print("<tr><td>" + str(i) + "</td>")
	for todo in json_data:
		print("<td>&nbsp")
		z=""
		for each in todo["usersDutyList"]:
			z = each["userFullname"]
			for each2 in each["dutyDays"]:
				if each2["day"] == str(i) and each2["isDuty"] == "true":
					print(z)
		print("</td>")
	print("</tr>")
	i=i+1
print("</table>")


#	for each in todo["usersDutyList"]:
#		name = each["userFullname"]
#		for each2 in each["dutyDays"]:
#			day = each2["day"]
#			if each2["isDuty"] == "true":
#				if gr == "Дежурный по администрированию 1С (1С админ)":
#					print("<tr> <td>" + name + "</td>" + "<td>" + day + "</td>" + "<td> + </td> </tr>")
#				elif gr == "Дежурный по виртуализации (VM)":
#					print("<tr> <td>" + name + "</td>" + "<td>" + day + "</td>" + "<td>  </td> <td> + </td> </tr>")
#				elif gr == "Дежурный по инфраструктуре ЦОД":
#					print("<tr> <td>" + name + "</td>" + "<td>" + day + "</td>" + "<td>  </td> <td>  </td> <td> + </td> </tr>")
#				elif gr == "Дежурный по мониторингу (skm)":
#					print("<tr> <td>" + name + "</td>" + "<td>" + day + "</td>" + "<tr>  </td> <td>  <td> </td> </td> <td> + </td> </tr>")
#				elif gr == "Дежурный по СУБД PostgreSQL (pgSQL)":
#					print("<tr> <td>" + name + "</td>" + "<td>" + day + "</td>" + "<td>  </td> <td>  </td> <td>  </td> <td> </td> <td> + </td> </tr>")
#				elif gr == "Дежурный по телефонии и КЦ":
#					print("<tr> <td>" + name + "</td>" + "<td>" + day + "</td>" + "<td>  </td> <td>  </td> <td>  </td> <td> </td> <td>  </td> <td> + </td> </tr>")
#				elif gr == "Мониторинг УЦОД 24/7":
#					print("<tr> <td>" + name + "</td>" + "<td>" + day + "</td>" + "<td>  </td> <td>  </td> <td>  </td> <td> </td> <td>  </td> <td> </td> <td> + </td> </tr>")