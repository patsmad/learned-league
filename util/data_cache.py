import json
import os

file_path = os.path.dirname(os.path.realpath(__file__))
data_path = '{}/../'.format(file_path)

def openJson(fname):
    with open(data_path + fname, 'r') as f:
        return json.load(f)

def saveJson(data, fname):
    with open(data_path + fname, 'w') as f:
        json.dump(data, f)