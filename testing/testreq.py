import wunderpy2
import json
from papirus import PapirusText

api = wunderpy2.WunderApi()

apikeys = ""
with open('apikeys.json') as data:
	apikeys = json.load(data)
print apikeys

token = apikeys["token"]
clientid = apikeys["clientid"]

client = api.get_client(token, clientid)

def getAllTasks():
	allTasks = []
	lists = client.get_lists()
	for list in lists:
		tasks = client.get_tasks(list["id"])
		for task in tasks:
			allTasks.append(task["title"])

	return allTasks

tasks = getAllTasks()

def toBullets(items):
	final = ""
	for item in items:
		final += " - " + item + "\n"
	return final

screenOutput = toBullets(tasks)
print screenOutput

textScreen = PapirusText()
textScreen.write(screenOutput)
