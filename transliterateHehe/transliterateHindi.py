
from indictrans import Transliterator
# https://github.com/libindic/indic-trans
trn = Transliterator(source='hin', target='eng', build_lookup=True)

def transliterateHindi(text):
	try:
		return trn.transform(text)
	except Exception as e:
		return text

