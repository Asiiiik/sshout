import requests,time,json,os,sys
from requests.structures import CaseInsensitiveDict


#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
purple="\033[0;35m"



#1


api1 = str(input (green+"Enter 1st Lkey : "+red))

message1  = str(input(green+"Enter Message : "+cyan))

#2


api2 = str(input (green+"Enter 2nd Lkey : "+blue))

message2  = str(input(lightblue+"Enter Message : "+red))

#3

api3 = str(input (purple+"Enter 3rd Lkey : "+blue))

message3  = str(input(green+"Enter Message : "+red))

#4

api4 = str(input (green+"Enter 4th Lkey : "+red))

message4  = str(input(cyan+"Enter Message : "+end))


#5

api5 = str(input (yellow+"Enter 5th Lkey : "+green))

message5  = str(input(red+"Enter Message : "+blue))

#6

api6 = str(input (red+"Enter 6th Lkey : "+green))

message6 = str(input(cyan+"Enter Message : "+yellow))

#7

api7 = str(input (purple+"Enter 7th Lkey : "+green))
message7 = str(input(red+"Enter Message : "+cyan))

#8

api8 = str(input (red+"Enter 8th Lkey : "+green))

message8  = str(input(yellow+"Enter Message : "+purple))

#9

api9 = str(input (blue+"Enter 9th Lkey : "+green))

message9  = str(input(white+"Enter Message : "+end))

#10

api10 = str(input (red+"Enter 10th Lkey : "+green))

message10  = str(input(cyan+"Enter Message : "+red))



i=0


#MainTools


#amount = int(input(green+'[>] Enter Your Target Amount:'+red))



headers1 = CaseInsensitiveDict()

headers1["Content-Type"] = "application/json; charset=UTF-8"
headers1["User-Agent"] = "gzip"
headers1["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
headers1["x-api-key"] = api1

url1 = "https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&action=kast&message="+message1

#2



headers2 = CaseInsensitiveDict()

headers2["Content-Type"] = "application/json; charset=UTF-8"
headers2["User-Agent"] = "gzip"
headers2["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
headers2["x-api-key"] = api2

url2 = "https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&action=kast&message="+message2

#3

headers3 = CaseInsensitiveDict()

headers3["Content-Type"] = "application/json; charset=UTF-8"
headers3["User-Agent"] = "gzip"
headers3["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
headers3["x-api-key"] = api3

url3 = "https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&action=kast&message="+message3

#4


headers4 = CaseInsensitiveDict()

headers4["Content-Type"] = "application/json; charset=UTF-8"
headers4["User-Agent"] = "gzip"
headers4["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
headers4["x-api-key"] = api4

url4 = "https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&action=kast&message="+message4


#5


headers5 = CaseInsensitiveDict()

headers5["Content-Type"] = "application/json; charset=UTF-8"
headers5["User-Agent"] = "gzip"
headers5["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
headers5["x-api-key"] = api5

url5 = "https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&action=kast&message="+message5


#6

headers6 = CaseInsensitiveDict()

headers6["Content-Type"] = "application/json; charset=UTF-8"
headers6["User-Agent"] = "gzip"
headers6["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
headers6["x-api-key"] = api6

url6 = "https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&action=kast&message="+message6

#7

headers7 = CaseInsensitiveDict()

headers7["Content-Type"] = "application/json; charset=UTF-8"
headers7["User-Agent"] = "gzip"
headers7["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
headers7["x-api-key"] = api7

url7 = "https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&action=kast&message="+message7

#8


headers8 = CaseInsensitiveDict()

headers8["Content-Type"] = "application/json; charset=UTF-8"
headers8["User-Agent"] = "gzip"
headers8["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
headers8["x-api-key"] = api8

url8 = "https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&action=kast&message="+message8

#9


headers9 = CaseInsensitiveDict()

headers9["Content-Type"] = "application/json; charset=UTF-8"
headers9["User-Agent"] = "gzip"
headers9["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
headers9["x-api-key"] = api9

url9 = "https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&action=kast&message="+message9


#10


headers10 = CaseInsensitiveDict()

headers10["Content-Type"] = "application/json; charset=UTF-8"
headers10["User-Agent"] = "gzip"
headers10["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
headers10["x-api-key"] = api10

url10 = "https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&action=kast&message="+message10


#actionLoop


while 1:
	try:
		#1
		resp1 = requests.post(url1, headers=headers1)
		response= resp1.text 
		json_object = json.loads(response)
		json_formatted_str = json.dumps(json_object, indent=1)
		print(json_formatted_str)
		#2
		resp2 = requests.post(url2, headers=headers2)
		response= resp2.text 
		json_object = json.loads(response)
		json_formatted_str = json.dumps(json_object, indent=1)
		print(json_formatted_str)
		#3
		resp3 = requests.post(url3, headers=headers3)
		response= resp3.text 
		json_object = json.loads(response)
		json_formatted_str = json.dumps(json_object, indent=1)
		print(json_formatted_str)
		#4
		resp4 = requests.post(url4, headers=headers4)
		response= resp4.text 
		json_object = json.loads(response)
		json_formatted_str = json.dumps(json_object, indent=1)
		print(json_formatted_str)
		#5
		resp5 = requests.post(url5, headers=headers5)
		response= resp5.text 
		json_object = json.loads(response)
		json_formatted_str = json.dumps(json_object, indent=1)
		print(json_formatted_str)
		#6
		resp6 = requests.post(url6, headers=headers6)
		response= resp6.text 
		json_object = json.loads(response)
		json_formatted_str = json.dumps(json_object, indent=1)
		print(json_formatted_str)
		#7
		resp7 = requests.post(url7, headers=headers7)
		response= resp7.text 
		json_object = json.loads(response)
		json_formatted_str = json.dumps(json_object, indent=1)
		print(json_formatted_str)
		#8
		resp8 = requests.post(url8, headers=headers8)
		response= resp8.text 
		json_object = json.loads(response)
		json_formatted_str = json.dumps(json_object, indent=1)
		print(json_formatted_str)
		#9
		resp9 = requests.post(url9, headers=headers9)
		response= resp9.text 
		json_object = json.loads(response)
		json_formatted_str = json.dumps(json_object, indent=1)
		print(json_formatted_str)
		#10
		resp10 = requests.post(url10, headers=headers10)
		response= resp10.text 
		json_object = json.loads(response)
		json_formatted_str = json.dumps(json_object, indent=1)
		print(json_formatted_str)
		#print(str(i+1)+' Shout\n')
		i=i+1
	except:
		print("Server Connection  Error!")
		#print(str(i+1)+' Shout not sent\n')