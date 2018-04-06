#sample python script
import json
import datetime
from pprint import pprint
from dateutil.parser import parse

data = json.load(open('data.json'))
totalTime = []

def getInfoByDeviceId(id):
	for i in data:
		if i['deviceId'] == id:
			print "Found: "+id
			print i["createdAt"]
			break

def isDeviceOn(id):
	if id["previousData"] == 0:
		return True
	else:
		return False

def calTime(id):
	time = 0
	last = 0
	for i in data:
		if i['deviceId'] == id:
			# Check whether on or off
			if isDeviceOn(i):
				# print "Device switched ON"
				last = parse(i["createdAt"])
			else:
				# print "Device switched OFF"
				stop = parse(i["createdAt"])
				diff = stop - last
				time += diff.seconds
	return time

for i in data:
	mm = i['deviceId']
	if mm not in totalTime:
		totalTime.append(mm)

for i in totalTime:
	secs = calTime(i)
	delta = datetime.timedelta(seconds=secs)
	print i + " " + str(delta)

# print len(totalTime)