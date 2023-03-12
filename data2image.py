from flask import Flask
from flask import send_file
import cv2
import numpy as np
import os
import datetime as dt

app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')
def index():
    return app.send_static_file('index.html')

def conv_data2color(data):
    color = [0, 0, 0]
    weight = [
        [20,10,0],
        [0,10,20],
        [20,30,0],
        [0,10,0],
        [0,30,0],
        [0,10,10],
        [0,40,0],
        [20,10,0],
        [10,20,0],
        [20,10,30]
    ]
    for i in range(len(data)):
        for j in range(3):
            color[j] += (data[i] - 3) * weight[i][j]
    
    for c in color:
        np.clip(c, 0, 255)

    return color

@app.route('/generate/<answer_data>')
def generate(answer_data):
    height = 200
    width = 300

    img = np.zeros((height, width, 3), np.uint8)
    answer_data = list(map(int, list(answer_data)))
    color = conv_data2color(answer_data)
    for w in range(0, width):
        img[:, w] = color

    now = dt.datetime.now()
    time = now.strftime('%Y%m%d-%H%M%S')
    filename = 'color_{}.jpg'.format(time)
    filepath = "temp/" + filename
    cv2.imwrite(filepath, img)

    return filepath

@app.route('/remove/<filename>')
def remove(filename):
    if os.path.isfile('temp/'+filename) == True:
        os.remove('temp/'+filename)
        return True
    else:
        return "file does not exist"


app.run(port=8000, debug=True)