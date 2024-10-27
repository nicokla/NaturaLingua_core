import glob
import os.path
import os


def createNecessaryFolders(output):
	machins = output.split('/')
	path=''
	for machin in machins[:-1]:
		path+=machin+'/'
		if not os.path.isdir(path):
			os.mkdir(path)

import pickle
def save_object(obj, filename):
	createNecessaryFolders(filename)
	with open(filename, 'wb') as output:  # Overwrites any existing file.
		pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def get_object(filename):
	with open(filename, 'rb') as input:
		return pickle.load(input)


def getListFiles(patterns):
	listeFiles=[]
	for aaa in patterns:
		files=glob.glob(aaa)
		listeFiles += files
	newListe=[]
	for a in listeFiles:
		if not(('readme' in a) or ('_old' in a)):
			newListe.append(a)
	return newListe

languagesLatines = ['french', 'spanish', 'portuguese', 'italian', 'turkish', 'vietnamese', 'english']
languagesNonLatines = ['japanese', 'russian', 'hebrew', 'arabic', 'korean', 'chinese', 'thai', 'persian', 'greek',  'hindi']
languages = languagesLatines + languagesNonLatines




# -------------


from dataclasses import dataclass, asdict, fields # ---> asdict
from typing import List
import json
import os
os.chdir('/Users/nicolas/Desktop')


def dataclass_from_dict(klass, d):
    try:
        fieldtypes = {f.name:f.type for f in fields(klass)}
        return klass(**{f:dataclass_from_dict(fieldtypes[f],d[f]) for f in d})
    except:
        return d # Not a dataclass field


# ----------------

def saveListOfObjectsAsJson(objectList, fileName="myfile.json"):
	jsonList = []
	for o in objectList:
		o_json = asdict(o)
		jsonList.append(o_json)
	out_file = open(fileName, "w")
	json.dump(jsonList, out_file, indent = 2)
	out_file.close()

def loadJsonToListOfObjects(classe, fileName="myfile.json"):
	f = open(fileName, "r")
	text = f.read()
	myJsonList = json.loads(text)
	objectList=[]
	for o_json in myJsonList:
		o=dataclass_from_dict(classe, o_json)
		objectList.append(o)
	return objectList


# saveListOfObjectsAsJson(jeux, 'jeux.json')
# jeux2 = loadJsonToListOfObjects(Jeu, fileName="jeux.json")


# ------------------------

def saveObjectAsJson(o, fileName="myfile.json"):
	o_json = asdict(o)
	out_file = open(fileName, "w")
	json.dump(o_json, out_file, indent = 2)
	out_file.close()

def loadJsonToObject(classe, fileName="myfile.json"):
	f = open(fileName, "r")
	text = f.read()
	o_json = json.loads(text)
	o=dataclass_from_dict(classe, o_json)
	return o


# -----------------


def saveVariableAsJson(o, fileName="myfile.json"):
	out_file = open(fileName, "w")
	json.dump(o, out_file, indent = 2)
	out_file.close()

def loadJsonToVariable(fileName="myfile.json"):
	f = open(fileName, "r")
	text = f.read()
	o = json.loads(text)
	return o
