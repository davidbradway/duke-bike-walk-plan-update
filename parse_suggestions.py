# Python program to read json file
import json
# Opening JSON file
f = open('suggestions.json')
# returns JSON object as a dictionary
data = json.load(f)
# Closing file
f.close()
counter = 0
# Iterating through the json list
for i in data['suggestions']:
    # print(i)
    if data['suggestions'][i] != []:    
        for j in data['suggestions'][i]:
            counter = counter + 1
            print(counter, ":", j['properties']['suggestion']['comment'])
