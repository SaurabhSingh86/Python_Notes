with open("72.json", "r") as j_file:
  read_json = json.load(j_file)

for i, value in enumerate(read_json["textAnnotations"]):
    if i != 0:
        bbox_vertices = value['boundingPoly']['vertices']        
        bbox = [bbox_vertices[0]['x'], bbox_vertices[0]['y'],
                bbox_vertices[1]['x'], bbox_vertices[1]['y'],
                bbox_vertices[2]['x'], bbox_vertices[2]['y'],
                bbox_vertices[3]['x'], bbox_vertices[3]['y']]
        # print(bbox)


json_file = open("72.json")
read_json = json.load(json_file)
json_file_i = 0
for i, value in enumerate(read_json["textAnnotations"]):
    if i != 0:
        bbox_vertices = value['boundingPoly']['vertices']        
        bbox = [bbox_vertices[0]['x'], bbox_vertices[0]['y'],
                bbox_vertices[1]['x'], bbox_vertices[1]['y'],
                bbox_vertices[2]['x'], bbox_vertices[2]['y'],
                bbox_vertices[3]['x'], bbox_vertices[3]['y']]
        # print(bbox)

# -------------------------------------------------------------------------------------------
with open("replayScript.json", "r") as jsonFile:
    data = json.load(jsonFile)

data["location"] = "NewPath"

with open("replayScript.json", "w") as jsonFile:
    json.dump(data, jsonFile)


with open("replayScript.json", "r+") as jsonFile:
    data = json.load(jsonFile)

    data["location"] = "NewPath"

    jsonFile.seek(0)  # rewind
    json.dump(data, jsonFile)
    jsonFile.truncate()


def updateJsonFile():
    jsonFile = open("replayScript.json", "r") # Open the JSON file for reading
    data = json.load(jsonFile) # Read the JSON into the buffer
    jsonFile.close() # Close the JSON file

    ## Working with buffered content
    tmp = data["location"] 
    data["location"] = path
    data["mode"] = "replay"

    ## Save our changes to JSON file
    jsonFile = open("replayScript.json", "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()
# -------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------