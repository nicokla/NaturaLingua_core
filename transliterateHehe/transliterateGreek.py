from transliterate import translit

def transliterateGreek(text):
	return translit(text, 'el', reversed=True)
