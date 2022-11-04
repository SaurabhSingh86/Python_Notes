import numpy as np
import cv2
import matplotlib.pyplot as plt
import json

def bbox_rotation(bbox, degree, p_height, p_width):
    h, w = p_height, p_width
    cx, cy = (int(w / 2), int(h / 2))

    bbox_tuple = [
            (bbox[0], bbox[1]),
            (bbox[2], bbox[3]),
            (bbox[4], bbox[5]),
            (bbox[6], bbox[7]),
        ] # put x and y coordinates in tuples, we will iterate through the tuples and perform rotation

    rotated_bbox = []

    for i, coord in enumerate(bbox_tuple):
        M = cv2.getRotationMatrix2D((cx, cy), degree, 1.0)
        cos, sin = abs(M[0, 0]), abs(M[0, 1])
        newW = int((h * sin) + (w * cos))
        newH = int((h * cos) + (w * sin))
        M[0, 2] += (newW / 2) - cx
        M[1, 2] += (newH / 2) - cy
        v = [coord[0], coord[1], 1]
        adjusted_coord = np.dot(M, v)
        rotated_bbox.insert(i, (adjusted_coord[0], adjusted_coord[1]))

    func_result = [int(x) for t in rotated_bbox for x in t]
    # xmin, ymin, xmax, ymax = result[0], result[1], result[4], result[5]
    return func_result

degree = -90
p_height, p_width = 210, 297  # measurement unit in 'mm'

with open("72.json", "r") as j_file:
  read_json = json.load(j_file)

# json_file_i = 0
for i, value in enumerate(read_json["textAnnotations"]):
    if i != 0 and value['boundingPoly']['vertices'] :
      bbox_vertices = value['boundingPoly']['vertices']        
      bbox = [bbox_vertices[0]['x'], bbox_vertices[0]['y'],
              bbox_vertices[1]['x'], bbox_vertices[1]['y'],
              bbox_vertices[2]['x'], bbox_vertices[2]['y'],
              bbox_vertices[3]['x'], bbox_vertices[3]['y']]
      # print(bbox)
      result = bbox_rotation(bbox, degree, p_height, p_width)
      new_vertices = [
      {
          "x": result[0],
          "y": result[1]
        },
        {
          "x": result[2],
          "y": result[3]
        },
        {
          "x": result[4],
          "y": result[5]
        },
        {
          "x": result[6],
          "y": result[7]
        }
  ]

      # reading & writing json file
      # if i != 0:    # json_file_i
      with open("72.json", "r") as json_file:
          read_json = json.load(json_file)
      read_json["textAnnotations"][i]['boundingPoly']['vertices'] = new_vertices

      with open("72.json", "w") as json_file:
          json.dump(read_json, json_file)   
  # json_file_i += 1