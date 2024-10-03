
# -------------
# prerequisites

import os
import sys


def getTimeNumber(string):
	milli = int(string[-3:])
	sec = int(string[6:8])
	minutes = int(string[3:5])
	hours = int(string[0:2])
	return (3600*hours + 60*minutes + sec + milli/1000)

def getTimeString(number):
	numberDixiemes = int((number%1)*10)%10
	numberInt = int(number)
	numberSec = numberInt%60
	numberMinutes = int(numberInt/60)%60
	numberHours = int(numberInt/3600)
	s=''
	if(numberHours>0):
		s+=format(numberHours, '02d')+':'
	s+=format(numberMinutes, '02d')+':'
	s+=format(numberSec, '02d')+','
	s+=format(round(numberDixiemes), '01d')
	return s

class PhraseFromMovie:
	def __init__(self, start, original, end, romanized='', style=''):
		self.start = start
		self.end = end
		self.original = original
		self.romanized = romanized
		self.style = style
	def __str__(self) -> str:
		debut = getTimeString(self.start)
		fin = getTimeString(self.end)
		return (f'[{debut} --> {fin}] : {self.original} ({self.romanized}) [style:{self.style}]')

# -----------------
# Input : .VTT

import webvtt

def mafonction_VTT(phraseOld):
	start=getTimeNumber(phraseOld.start)
	end=getTimeNumber(phraseOld.end)
	text=phraseOld.text
	return PhraseFromMovie(start, text, end)

def getSub_VTT(fileName):
	phrasesOld=webvtt.read(fileName)
	phrases=list(map(mafonction_VTT, phrasesOld))
	return phrases

# fileName = '/Users/nicolas/Desktop/coucou.vtt'
# phrases = getSub_VTT(fileName)
# print(phrases[10])

# -----------------
# Input : .XML

from lxml import etree

def getTimeFloatForXML(timeString):
	timeString2=timeString[:-1]
	return int(timeString2)/1e7

def mafonction_XML(truc):
	start = getTimeFloatForXML(truc.values()[0])
	end = getTimeFloatForXML(truc.values()[1])
	text=' '.join(truc.itertext())
	return PhraseFromMovie(start, text, end)

def getSub_XML(fileName):
	text = open(fileName,'r').read()
	if text.startswith('<?xml'):
		index = text.find('?>\n')
		text = text[(index+3):]
	tree = etree.fromstring(text)
	root = tree.getchildren()[1].getchildren()[0].getchildren()
	phrases=list(map(mafonction_XML, root))
	return phrases

# fileName = '/Users/nicolas/Desktop/coucou.xml'
# phrases = getSub_XML(fileName)
# print(phrases[10])


# -----------------
# Input : .ASS

import pysubs2

def mafonction_ASS(phraseOld):
	start=phraseOld.start/1000
	end=phraseOld.end/1000
	text=phraseOld.text
	style=phraseOld.style
	return PhraseFromMovie(start, text, end, style=style)

def getSub_ASS(fileName):
	phrasesOld=pysubs2.load(fileName, encoding="utf-8")
	phrases=list(map(mafonction_ASS, phrasesOld))
	return phrases

# fileName = '/Users/nicolas/Desktop/japanese/movies/horsNetflixTodos/mirai no mirai/Mirai[AnimeKaizoku][dedsec].ja-en.ass'
# phrases = getSub_ASS(fileName)
# print(phrases[10])


# -----------------
# Input : .SRT

import srt
from datetime import timedelta

def mafonction_SRT(phraseOld):
	start=phraseOld.start.total_seconds()
	end=phraseOld.end.total_seconds()
	text=phraseOld.content
	return PhraseFromMovie(start, text, end)

def getSub_SRT(fileName):
	file = open(fileName, 'r', encoding='UTF-8')
	text=file.read()
	phrasesOld = list(srt.parse(text))
	phrases=list(map(mafonction_SRT, phrasesOld))
	return phrases

def saveSub_SRT(subList, fileName):
	liste=[]
	for i in range(len(subList)):
		sub=subList[i]
		start=timedelta(sub.start/24/3600)
		end=timedelta(sub.end/24/3600)
		content=sub.text
		liste.append(srt.Subtitle(index=i, start=start, end=end, content=content, proprietary=''))
	with open(fileName, 'w+') as file:
		file.write(srt.compose(liste))

def ass2srt(fileName):
	newFileName=fileName[:-3]+'srt'
	subs = getSub_ASS(fileName)
	saveSub_SRT(subs, newFileName)


# ---------------------
# Input : all formats

def getSub(fileName):
	finMot=fileName[-3:]
	if(finMot=='vtt'):
		return getSub_VTT(fileName)
	elif(finMot=='xml'):
		return getSub_XML(fileName)
	elif(finMot=='ass'):
		return getSub_ASS(fileName)
	elif(finMot=='srt'):
		return getSub_SRT(fileName)
	raise ValueError('Format unknown:', finMot)


def enleverSautDeLigne(text):
	return text.replace('\n',' ').strip()


# -----------------------
# Output

def myCondition2(jap, ang):
	return (jap.start - 0.3 < ang.start)

def myCondition3(jap, ang):
	return (jap.start - 0.3 < ang.start) or\
		((jap.start > ang.start) and (jap.end - 0.3 < ang.end))



def writeOutput(fileName, phrasesJaponaises, phrasesAnglaises, printOriginal=True, printRomanized=True):
	print('writeOutput')
	file2=open(fileName, 'w+')
	i = 0
	j = 0
	phraseJap = phrasesJaponaises[i]
	phraseAng = phrasesAnglaises[j]
	while (True):
		if((i>=len(phrasesJaponaises)) and (j>=len(phrasesAnglaises)) ):
			break
		if((j >= len(phrasesAnglaises) or\
			myCondition3(phraseJap, phraseAng))\
			and (i < len(phrasesJaponaises)) ):
			timeString=getTimeString(phraseJap.start)
			if(printOriginal):
				file2.write(f'* {phraseJap.original}	 [{timeString}]\n')
			if(printRomanized):
				file2.write(f'- {phraseJap.romanized}	 [{timeString}]\n')
			i += 1
			if(i < len(phrasesJaponaises)):
				phraseJap = phrasesJaponaises[i]
		elif j < len(phrasesAnglaises):
			file2.write(f'    {phraseAng.original}	 [{getTimeString(phraseAng.start)}]\n')
			if(j < (len(phrasesAnglaises) - 1)):
				duree=(phrasesAnglaises[j+1].start - phraseAng.end)
				if(duree >= 6):
					file2.write('\n')
				if(duree >= 10):
					file2.write('\n')
			j += 1
			if(j < len(phrasesAnglaises)):
				phraseAng = phrasesAnglaises[j]
	file2.close()


# import sys
# sys.path.append('/Users/nicolas/Desktop/NaturaLingua/SubsToBilingualText')
# from transliteratePerso import transliterate, transliterate2, getCode
# from transliterateHebrew import transliterateListHebrew
# transliterate("知识就是力量", 'zh')
# transliterate2("知识就是力量", 'chinese')

import sys
# sys.path.append('/Users/nicolas/Desktop/NaturaLingua/SubsToBilingualText/transliterate')
from transliterateHehe.transliterateAll import transliterate, transliterate2
from transliterateHehe.languageCodes import getCode
from transliterateHehe.transliterateList import transliterateList
from transliterateHehe.postProcessing import postProcessing


def enleverSautDeLigneAll(listeDePhrases):
	for phrase in listeDePhrases:
		phrase.original=enleverSautDeLigne(phrase.original)

# -----------------------------------------------
# from charset_normalizer import from_path
# results = from_path(pathJap)
# print(str(results.best()))

from charset_normalizer import normalize

# pathJap = normalizeFile(pathJap)
def normalizeFile(pathJap):
	aaa={}
	try:
		aaa=normalize(pathJap) # should write to disk my_subtitle-***.srt
		pathJap2 = f'{pathJap[:-4]}-{aaa.encoding}.{pathJap[-3:]}'
		return pathJap2
	except IOError as e:
		raise ValueError('Sadly, we are unable to perform charset normalization.', str(e))



def enleverParenthesesPourJaponais(text):
	openPars=['（','(']
	closePars=['）',')']
	lvl=0
	s=''
	for c in text:
		if c in openPars:
			lvl += 1
		elif c in closePars:
			if lvl > 0:
				lvl -= 1
		elif(lvl == 0):
			s+=c
		else:
			continue
	return s

def getListWithoutParenthesesProblems(subs):
	newListe=[]
	for a in subs:
		a.original=enleverParenthesesPourJaponais(a.original)
		if(a.original!=''):
			newListe.append(a)
	return newListe

def printOriginalOrRomanized(alphabetId):
	printOriginal=True
	printRomanized=True
	if(alphabetId=='roman'):
		printOriginal = False
	elif(alphabetId=='original'):
		printRomanized = False
	return printOriginal, printRomanized

def subsToText(pathJap, pathEng, pathOutput, language, doThePresync=True, printOriginal=True, printRomanized=True, normalize=False):
	print('subsToText')
	if(normalize):
		pathJap=normalizeFile(pathJap)
	if(doThePresync):
		pathEng2=f'{pathEng}_syncronizedEng.srt'
		os.system(f'ffsubsync "{pathJap}" -i "{pathEng}" -o "{pathEng2}" --gss --max-offset-seconds 120')
		pathEng=pathEng2
	phrasesAnglaises=getSub(pathEng)
	phrasesJaponaises=getSub(pathJap)
	enleverSautDeLigneAll(phrasesAnglaises)
	enleverSautDeLigneAll(phrasesJaponaises)
	if(language[:2]=='ja'):
		phrasesJaponaises = getListWithoutParenthesesProblems(phrasesJaponaises)
	transliterateList(phrasesJaponaises, language)
	writeOutput(pathOutput, phrasesJaponaises, phrasesAnglaises, printOriginal=printOriginal, printRomanized=printRomanized)
	postProcessing(pathOutput, language)


# -----------------
# https://www.alchemysoftware.com/livedocs/ezscript/Topics/Catalyst/Language.htm

def subsToTextNotNetflix(pathJap, pathEng, pathOutput, language, printOriginal, printRomanized):
	subsToText(pathJap, pathEng, pathOutput, language, printOriginal=printOriginal, printRomanized=printRomanized, normalize=True, doThePresync=True)

def subsToTextNetflix(pathJap, pathEng, pathOutput, language, printOriginal, printRomanized):
	subsToText(pathJap, pathEng, pathOutput, language, printOriginal=printOriginal, printRomanized=printRomanized, normalize=False, doThePresync=False)

# def subsToTextNetflix_original(pathJap, pathEng, pathOutput, language):
# 	subsToText(pathJap, pathEng, pathOutput, language, printOriginal=False, printRomanized=True, normalize=False, doThePresync=False)


# pathEng='/Users/nicolas/Desktop/interets/SubsToBilingualText/movies/italian/pourri/il sorpasso/anglais.srt'
# pathJap='/Users/nicolas/Desktop/interets/SubsToBilingualText/movies/italian/pourri/il sorpasso/japonais.srt'
# pathOutput='/Users/nicolas/Desktop/interets/SubsToBilingualText/movies/italian/pourri/il sorpasso/result.txt'
# language='it'
# subsToTextNotNetflix(pathJap, pathEng, pathOutput, language)



# ==================================
#				 whole directories
# ==================================

# path = path of directory
# langue connue : path/anglais.srt (ou autre format)
# langue inconnue : path/japonais.srt (ou autre format)
# resultat ecrit dans path/result.txt 
def subsToTxt(path, languageCode, alphabetId):
	dico={'anglais':'','japonais':''}
	for bla in os.scandir(path):
		if bla.is_file():
			liste=bla.name.split('.')
			dico[liste[0]]=(liste[1],bla.path)
	pathOutput = path + '/result.txt'
	print('\n'+pathOutput)
	printOriginal, printRomanized = printOriginalOrRomanized(alphabetId)
	try:
		if dico['anglais'][0]=='vtt' or dico['anglais'][0]=='xml':
			print('	 netflix\n')
			subsToTextNetflix(dico['japonais'][1], dico['anglais'][1], pathOutput, languageCode, printOriginal, printRomanized)
		else: # .srt, .ass ---> not netflix (need to synchronize)
			print('	 not netflix\n')
			subsToTextNotNetflix(dico['japonais'][1], dico['anglais'][1], pathOutput, languageCode, printOriginal, printRomanized)
	except Exception as e:
		print(e)
		return pathOutput
	return pathOutput


# def allMoviesInDir(dir, languageCode):
#	 obj = os.scandir(dir)
#	 for entry in obj :
#		 if entry.is_dir():
#			 subsToTxt(entry.path, languageCode)


# dir = '/Users/nicolas/Desktop/NaturaLingua/SubsToBilingualText/movies/Japanese/subfiles/'
# languageCode='ja'
# allMoviesInDir(dir, languageCode)


# def allMoviesOfLanguage(language):
#	 code=getCode(language)
#	 cap=language.capitalize()
#	 dir = f'/Users/nicolas/Desktop/NaturaLingua/SubsToBilingualText/movies/{cap}/'
#	 allMoviesInDir(dir, code)



# ===================


# parent='/Users/nicolas/Desktop/NaturaLingua/SubsToBilingualText/movies/'
# dirs = [parent+'arabe/', parent+'grec/', parent+'turkish/', parent+'italian/',
# parent+'espanol/', parent+'korean/', parent+'chinese/', parent+'russe/',
# parent+'persian/', parent+'portuguese/', parent+'hindi/', parent+'viet/']
# dirsLanguages=['arabe','grec', 'turkish', 'italian',
# 'espanol', 'korean', 'chinese', 'russe',
# 'persian', 'portuguese', 'hindi', 'viet']
# languages={'arabe':'ar','grec':'el','korean':'ko','chinese':'zh',
# 'russe':'ru', 'persian':'fa', 'portuguese':'pt', 'turkish':'tr',
# 'espanol':'es', 'italian':'it', 'hindi': 'hi', 'viet':'vi'}

# for index, dir in enumerate(dirs):
# 	languageCode=languages[dirsLanguages[index]]
# 	allMoviesInDir(dir, languageCode)
