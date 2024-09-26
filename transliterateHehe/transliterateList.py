
from transliterateHehe.transliterateAll import transliterate
from transliterateHehe.transliterateListHebrew import transliterateListHebrew
from transliterateHehe.languageCodes import getCode, getLanguage
from utils.utils import languagesLatines

# async
def transliterateList(phrases, languageCode):
	print('transliterateList', languageCode)
	if(getLanguage(languageCode) in languagesLatines):
		for phrase in phrases:
			if(phrase.romanized == ''):
				phrase.romanized = phrase.original
			if(phrase.original == ''):
				phrase.original = phrase.romanized
	elif(getLanguage(languageCode) == 'hebrew'):
		transliterateListHebrew(phrases) # await
	else:
		longueur=len(phrases)
		for index,phrase in enumerate(phrases):
			# print(f'\r{index/longueur*100} %', end='', flush=True)
			phrase.romanized = transliterate(phrase.original, languageCode)
	print('finished transliterateList')

# async
def transliterateList2(word, language):
	return ( transliterateList(word, getCode(language))) # await

