
import sys
sys.path.append("/Users/nicolas/Desktop/NaturaLingua")
from transliterateHehe.languageCodes import languageToCodes, getCode
from youtube.youtube import absorbYoutubeVideo
from movies.movies import subsToTxt
from utils.createPdfs import createPdfYoutube, createPdfMovie


################
# A) Subtitle files (.SRT or .VTT)
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

# language de depart (inconnu)
language = 'french'
# alphabetId = original|roman|both  (alphabet du langage de depart, le langage d'arrive est connu)
alphabetId = 'original'
# mettre anglais.srt et japonais.srt dans dirPath ---> dirPath/result.txt ---> dirPath/result.pdf
dirPath = '/Users/nicolas/Desktop/NaturaLingua/directoryMovies'

def createDocsFromMovieSubtitles(language, alphabetId, dirPath):
	languageCode = getCode(language) #languageToCodes[language]
	txtFileName = subsToTxt(dirPath, languageCode, alphabetId)
	createPdfMovie('Titre', txtFileName, txtFileName+'.pdf', language, alphabetId)

createDocsFromMovieSubtitles(language, alphabetId, dirPath)



################
# B) Youtube video ID
################

# to enable this B) code, you first need to
# - create a Youtube API key (here : https://console.cloud.google.com/apis/credentials?pli=1 )
# - create a .env file in the "youtube" folder containing the uncommented line : 
# YOUTUBE_KEY=.....
# where you replace ..... with your Youtube API key.

# language de depart, inconnu
language = 'english'
# alphabetId = roman|original|both  (alphabet du langage de depart, le langage d'arrive est connu)
alphabetId = 'original'
videoId = 'BkQuosRLSS8'
languageKnown = 'french'
outputDir = '/Users/nicolas/Desktop/NaturaLingua/directoryYoutube'

def createDocsFromYoutube(videoId, language, languageKnown, alphabetId, outputDir):
	languageCodes=languageToCodes[language]
	languageCodesKnown=languageToCodes[languageKnown]
	txtFileName = f'{outputDir}/{videoId}.txt'
	pdfFileName = f'{outputDir}/{videoId}.pdf'
	absorbYoutubeVideo(videoId, languageCodes, languageCodesKnown, alphabetId, txtFileName)
	myPdf = createPdfYoutube(videoId, txtFileName, pdfFileName, language, alphabetId)

createDocsFromYoutube(videoId, language, languageKnown, alphabetId, outputDir)

