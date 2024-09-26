
import MicroTokenizer
import pinyin


def transliterateChineseSub(blob):
	try:
		return pinyin.get(blob, delimiter="")
	except Exception as e:
		return blob

def isLatin(mychar):
  number=ord(mychar)
  return number < 0x80

from functools import reduce

def maFonction(acc, s):
	if(len(acc)==0):
		return s
	if(len(s)==1 and isLatin(s[0]) and isLatin(acc[-1])):
		return acc+s
	else:
		return acc+' '+s

def transliterateChinese(phrase):
	tokens = MicroTokenizer.cut(phrase)
	liste=list(map(transliterateChineseSub,tokens)) 
	result = reduce(maFonction, liste, '') #' '.join(liste)
	return result