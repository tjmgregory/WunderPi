import wunderpy2
import json
from imaging import draw
from papirus import Papirus
from papirus import PapirusImage

api = wunderpy2.WunderApi()

# Collects the API keys from a json file, which you will need to create yourself in this format:
#	{
#		"token": "YOUR ACCESS TOKEN HERE",
#		"clientid": "YOUR CLIENT ID HERE"
#	}
apikeys = ""
with open('apikeys.json') as data:
	apikeys = json.load(data)
token = apikeys["token"]
clientid = apikeys["clientid"]

# Sets up the client so requests can be made.
client = api.get_client(token, clientid)

# Compiles the title of all the tasks into a list.
def getAllTasks():
	allTasks = []
	lists = client.get_lists()
	for list in lists:
		tasks = client.get_tasks(list["id"])
		for task in tasks:
			allTasks.append(task["title"])

	return allTasks

# Performs necessary methods.
tasks = getAllTasks()
draw(tasks, "test")

imageScreen = PapirusImage()
imageScreen.write('test.jpg')
