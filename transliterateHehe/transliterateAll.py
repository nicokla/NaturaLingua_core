from transliterateHehe.transliterateHindi import transliterateHindi
from transliterateHehe.transliterateChinese import transliterateChinese
from transliterateHehe.transliterateJapanese import transliterateJapanese
from transliterateHehe.transliterateKorean import transliterateKorean
from transliterateHehe.transliterateArabic import transliterateArabic
from transliterateHehe.transliterateHebrew import transliterateHebrew
from transliterateHehe.transliterateRussian import transliterateRussian
from transliterateHehe.transliterateGreek import transliterateGreek
from transliterateHehe.transliteratePersian import transliteratePersian
from transliterateHehe.transliterateThai import transliterateThai
from transliterateHehe.languageCodes import getCode, getLanguage

# https://www.alchemysoftware.com/livedocs/ezscript/Topics/Catalyst/Language.htm
def transliterate(phrase, languageCode):
	language = getLanguage(languageCode)
	if language == 'japanese':
		return transliterateJapanese(phrase)
	elif language == 'arabic':
		return transliterateArabic(phrase)
	elif language == 'korean':
		return transliterateKorean(phrase)
	elif language == 'greek':
		return transliterateGreek(phrase)
	elif language == 'chinese':
		return transliterateChinese(phrase)
	elif language == 'russian':
		return transliterateRussian(phrase)
	elif language == 'hindi':
		return transliterateHindi(phrase)
	elif language == 'persian':
		return transliteratePersian(phrase)
	elif language == 'thai':
		return transliterateThai(phrase)
	elif language == 'hebrew':
		return transliterateHebrew(phrase)
	else:
		return phrase


def transliterate2(word, langue):
	return transliterate(word, getCode(langue))
