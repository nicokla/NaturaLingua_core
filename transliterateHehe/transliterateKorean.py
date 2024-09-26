
from korean_romanizer.romanizer import Romanizer

def transliterateKorean(text):
	try:
		return (Romanizer(text).romanize())
	except Exception as e:
		return text