

class Phrase:
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

class YoutubeVideo:
	def __init__(self, title, id, phrasesAnglaises, phrasesJaponaises, language):
		self.title = title
		self.id = id
		self.phrasesAnglaises = phrasesAnglaises
		self.phrasesJaponaises = phrasesJaponaises
		self.language = language

class YoutubeChannel:
	def __init__(self, name, id, videos=[]):
		self.name = name
		self.id = id
		self.videos = videos

import sys
sys.path.append('/Users/nicolas/Desktop/NaturaLingua')
from utils.utils import save_object, get_object, createNecessaryFolders

# ----------------------------------------------
# 1) 
# https://developers.google.com/youtube/v3/docs/search/list
# https://github.com/rhayun/python-youtube-api
# https://console.cloud.google.com/apis

from youtube.youtube_api import YoutubeAPI
import os
from dotenv import load_dotenv
load_dotenv('/Users/nicolas/Desktop/NaturaLingua/youtube/.env')

youtubeKey=os.environ['YOUTUBE_KEY']
youtube = YoutubeAPI({'key': youtubeKey})

# https://www.youtube.com/watch?v=VIDEO_ID_HERE
# onomappu, kemushi chan, miku real japanese, ask japanese
# suchi ramen, tokyo veg life, kan et aki
def getChannelId(channelName):
	params = {
		'q':channelName,
		'part':"snippet",
		'type':"channel",
	}
	search = youtube.search_advanced(params, True)
	return search['results'][0]['id']['channelId']

def getAllVideosFromChannel(channelName):
  channelId = getChannelId(channelName)
  params = {
      'q':'',
      'part':"snippet",
      'channelId':channelId,
      'type':"video",
      'maxResults':"50"
  }
  search = youtube.search_advanced(params, True)
  results=search['results']
  myToken = search['info']
  while(True):
    canContinue = 'nextPageToken' in myToken and myToken['nextPageToken'] != None
    if(canContinue):
      params['pageToken'] = myToken['nextPageToken']
      # print(myToken)
      newVideos=youtube.search_advanced(params, True)
      myToken = newVideos['info']
      results+=newVideos['results']
      # len(results)
    else:
      break
  return channelId, results

# liste1[0]['id']['videoId']
def getVideoIdAndName(elem):
  return (elem['id']['videoId'], elem['snippet']['title'])

def getAllVideoIdsAndNames(channelName):
  id, liste1=getAllVideosFromChannel(channelName)
  answer=list(map(getVideoIdAndName, liste1))
  return id, answer

# --------------------------------------------------------------
# 2) Get transcripts (japanese kanji, and english)
# https://pypi.org/project/youtube-transcript-api/

from youtube_transcript_api import YouTubeTranscriptApi

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

# -----------------------------

# import sys
# sys.path.append('/Users/nicolas/Desktop/NaturaLingua')
from transliterateHehe.transliterateList import transliterateList
from transliterateHehe.languageCodes import languageToCodes
from transliterateHehe.postProcessing import postProcessing


def youtubeToPhraseJap(youtubeSub):
	original = youtubeSub['text'].replace('\n',' ').strip()
	start = youtubeSub['start']
	duration = youtubeSub['duration']
	end = start + duration
	return Phrase(start, original, end)

# https://testdriven.io/blog/flask-async/
# async
def youtubeToPhraseJap_all(youtubeSubs, language):
	l = list(map(youtubeToPhraseJap, youtubeSubs))
	# import pdb; pdb.set_trace()
	transliterateList(l, language) # await
	return l

# ====================


def isJapanese(mychar):
  number=ord(mychar)
  return number >= 0x3000 and number <= 0xffef

def phraseRemoveJapaneseCharacters(sentence):
  newSentence=''
  for c in sentence:
    if(not isJapanese(c)):
      newSentence+=c
  return newSentence

def isHebrew(mychar):
  number=ord(mychar)
  return ((number >= 0x500) and (number <= 0x5FF))

def phraseRemoveHebrewCharacters(sentence):
  newSentence=''
  for c in sentence:
    if(not isHebrew(c)):
      newSentence+=c
  return newSentence

def youtubeToPhraseAng(youtubeSub, language):
	duration = youtubeSub['duration']
	start = youtubeSub['start']
	text = youtubeSub['text']
	end = start + duration
	text = text.replace('\n',' ').strip()
	if(language=='ja'):
		text = phraseRemoveJapaneseCharacters(text)
	elif(language in ['he','he-IL','heb','iw']):
		text = phraseRemoveHebrewCharacters(text)
	return Phrase(start, text, end)

def youtubeToPhraseAng_all(youtubeSubs, language):
	return list(map(lambda sub: youtubeToPhraseAng(sub, language), youtubeSubs))

# ------------------------------

def myCondition2(jap, ang):
  return (jap.start - 0.3 < ang.start)

def myCondition3(jap, ang):
  return (jap.start - 0.3 < ang.start) or\
    ((jap.start > ang.start) and (jap.end - 0.3 < ang.end))

def printOriginalOrRomanized(alphabetId):
	printOriginal=True
	printRomanized=True
	if(alphabetId=='roman'):
		printOriginal = False
	elif(alphabetId=='original'):
		printRomanized = False
	return printOriginal, printRomanized


def writeFileGeneral(file2, myYoutubeVideo, alphabetId):
	phrasesAnglaises=myYoutubeVideo.phrasesAnglaises
	phrasesJaponaises=myYoutubeVideo.phrasesJaponaises
	# file2.write('\n-------------------------\n')
	# file2.write(myYoutubeVideo.title+'\n')
	# file2.write(f'https://youtu.be/{myYoutubeVideo.id}\n')
	# file2.write('-------------------------\n')
	printOriginal, printRomanized = printOriginalOrRomanized(alphabetId)
	i = 0
	j = 0
	phraseJap = phrasesJaponaises[i]
	phraseAng = phrasesAnglaises[j]
	while (True):
		if((i>=len(phrasesJaponaises)) and (j>=len(phrasesAnglaises)) ):
			break
		if((j >= len(phrasesAnglaises) or myCondition3(phraseJap, phraseAng)) and (i < len(phrasesJaponaises)) ):
			timeString=getTimeString(phraseJap.start)
			if(printOriginal):
				file2.write(f'* {phraseJap.original}	 [{timeString}]\n')
			if(printRomanized):
				file2.write(f'- {phraseJap.romanized}	 [{timeString}]\n')
			i += 1
			if(i < len(phrasesJaponaises)):
				phraseJap = phrasesJaponaises[i]
		elif j < len(phrasesAnglaises):
			file2.write(f'    {phraseAng.original}   [{getTimeString(phraseAng.start)}]\n')
			if(j < (len(phrasesAnglaises) - 1)):
				duree=(phrasesAnglaises[j+1].start - phraseAng.end)
				if(duree >= 6):
					file2.write('\n')
				if(duree >= 10):
					file2.write('\n')
			j += 1
			if(j < len(phrasesAnglaises)):
				phraseAng = phrasesAnglaises[j]
	return phrasesJaponaises, phrasesAnglaises


# ja, en
def getManualSub(transcriptList, language):
  japaneseOk=True
  try:
    transcriptJaponaisFetchable=transcriptList.find_manually_created_transcript([language])
  except Exception as e:
    japaneseOk=False
    transcriptJaponaisFetchable = {}
  return japaneseOk, transcriptJaponaisFetchable

# https://testdriven.io/blog/flask-async/
# async
def absorbYoutubeVideo(videoId, languageCodes, languageCodesKnown, alphabetId, fileName):
	file1=open(fileName, 'w+')
	try:
		transcriptList = YouTubeTranscriptApi.list_transcripts(videoId)
	except Exception as e:
		print('%s no subs' % videoId)
		file1.close()
		return fileName
	for languageCode in languageCodesKnown:
		englishOk, transcriptAnglaisFetchable = getManualSub(transcriptList, languageCode)
		print('languageCode: %s / englishOk: %s' % (languageCode, englishOk))
		if englishOk:
			break
	for languageCode in languageCodes:
		japaneseOk, transcriptJaponaisFetchable = getManualSub(transcriptList, languageCode)
		print('languageCode: %s / japaneseOk: %s' % (languageCode, japaneseOk))
		if japaneseOk:
			break
	if(englishOk and japaneseOk):
		try:
			transcriptAnglais = transcriptAnglaisFetchable.fetch()
			transcriptJaponais = transcriptJaponaisFetchable.fetch()
		except Exception as e:
			print('%s erreur bizarre' % videoId)
			file1.close()
			return fileName
	else:
		print('%s snif' % videoId)
		return fileName
	print('%s youpi' % videoId)
	phrasesJaponaises = youtubeToPhraseJap_all(transcriptJaponais, languageCode) # await
	phrasesAnglaises = youtubeToPhraseAng_all(transcriptAnglais, languageCode)
	myYoutubeVideo=YoutubeVideo('', videoId, phrasesAnglaises, phrasesJaponaises, languageCode)
	writeFileGeneral(file1, myYoutubeVideo, alphabetId)
	file1.close()
	postProcessing(fileName, languageCode)
	return fileName

