
import sys
sys.path.append("/Users/nicolas/Desktop/NaturaLingua")
from transliterateHehe.languageCodes import languageToCodes, getCode
from youtube.youtube import createDocsFromYoutube, absorbYoutubeChannels
from movies.movies import subsToTxt
from utils.createPdfs import createPdfYoutube, createPdfMovie


# ----------------------------
# 1) single video / movie
# -------------------------

################
# 1.A) Subtitle files (.SRT or .VTT)
################

# To get subtitle files, 2 techniques :
# A) Get them on opensubtitles.org (format : .srt)
# B) Or get them from netflix using devtools (format : .vtt or .xml):
#   ---> go on netflix, open devtools, go in network, then enable the subtitle in the language you want, then look for the file in devtools/network. you need to do this twice to get the two files.

# before using the function, put the subtitle files in the same directory (called dirPath)
# and rename them like this : 
# - the language you know should be renamed "anglais.srt" (even if it is not english)
# - the language you don't know should be renamed "japanese.srt" (even if it is not japanese)
# if you use .vtt or .xml files as input, use "anglais.vtt" and "japanese.vtt"


def createDocsFromMovieSubtitles(language, alphabetId, dirPath):
	languageCode = getCode(language) #languageToCodes[language]
	txtFileName = subsToTxt(dirPath, languageCode, alphabetId)
	createPdfMovie('Titre', txtFileName, txtFileName+'.pdf', language, alphabetId)

# language de depart (inconnu)
language = 'french'
# alphabetId = original|roman|both  (alphabet du langage de depart, le langage d'arrive est connu)
alphabetId = 'original'
# mettre anglais.srt et japonais.srt dans dirPath ---> dirPath/result.txt ---> dirPath/result.pdf
dirPath = '/Users/nicolas/Desktop/NaturaLingua/directoryMovies'

createDocsFromMovieSubtitles(language, alphabetId, dirPath)



################
# 1.B) Youtube video ID
################

# to enable this B) code, you first need to
# - create a Youtube API key (here : https://console.cloud.google.com/apis/credentials?pli=1 )
# - create a .env file in the "youtube" folder containing the uncommented line : 
# YOUTUBE_KEY=.....
# where you replace ..... with your Youtube API key.


language = 'persian'
# alphabetId = roman | original | both  (alphabet du langage de depart, le langage d'arrive est connu)
alphabetId = 'roman'
videoId = 'kP15q815Saw'
languageKnown = 'english'
outputDir = '/Users/nicolas/Desktop/NaturaLingua/directoryYoutube'

createDocsFromYoutube(videoId, language, languageKnown, alphabetId, outputDir)



# --------------------------
# 2) whole youtube channel
# --------------------------


language = 'arabic'
channelName = languageToChannels[language][0]

listAllVideoIds = absorbChannel(channelName, language)

outputDir = '/Users/nicolas/Desktop/NaturaLingua/directoryYoutube'
fileName = f'{outputDir}/{language.capitalize()}/{channelName}.json'
saveVariableAsJson(listAllVideoIds, fileName)
listAllVideoIds = loadJsonToVariable(fileName)

for videoId in listAllVideoIds[:10]:
	print(videoId)
	absorbAndWriteYoutubeVid(videoId, language, alphabetId='roman')
