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

