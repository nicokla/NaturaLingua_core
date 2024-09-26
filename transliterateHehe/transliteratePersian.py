from PersianG2p import Persian_g2p_converter

PersianG2Pconverter = Persian_g2p_converter()

def transliteratePersian_temp(sentence):
	return PersianG2Pconverter.transliterate(sentence, secret = True)

# phrase1='votre {m} {f} vos {m-p} {f-p} [formal]'
# phrase2='[generic] (discourteous if used for a superior)'
def transliteratePersian(phrase):
	currentJapanese=''
	result=''
	try:
		for c in phrase:
			if (c >= 'A' and c <= 'z') or (c in ' [].!?,;}{()'):
				if(currentJapanese!=''):
					result += transliteratePersian_temp(currentJapanese)
					currentJapanese=''
				result += c
			else:
				currentJapanese+=c
		if(currentJapanese!=''):
			result += transliteratePersian_temp(currentJapanese)
			currentJapanese=''
		return result
	except Exception as e:
		return phrase
