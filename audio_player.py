from pygame import mixer
import os.path
import json

print("Loading data.json")
dataFile = open('data.json', 'r')
audioMap = json.loads(dataFile.read())
dataFile.close()

mixer.init()

while True:
	key = raw_input('Enter keyword (exit to quit): ')
	if key == 'exit':
		break

	if not key in audioMap:
		print('Could not find ' + key + ' in data.json')
		continue
	fname = audioMap[key]
	fileExists = os.path.isfile(fname)
	if fileExists:
		mixer.music.load(fname)
		mixer.music.play()
	else:
		print("File " + fname + " not found.")