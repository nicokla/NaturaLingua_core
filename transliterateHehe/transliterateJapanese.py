
import cutlet
katsu = cutlet.Cutlet()
katsu.use_foreign_spelling = False


# せっかく 神奈川まで来たので、鎌倉で 一泊することにしました。
# phrase1='votre {m} {f} vos {m-p} {f-p} [formal]'
# phrase2='[generic] (discourteous if used for a superior) 貴方達'
# transliterateJapaneseOld
def transliterateJapanese(phrase):
	currentJapanese=''
	result=''
	try:
		for c in phrase:
			if (c >= 'A' and c <= 'z') or (c in ' [].!?,;}{()'):
				if(currentJapanese!=''):
					result += katsu.romaji(currentJapanese).lower()
					currentJapanese=''
					if c == ' ' and not (result[-1] in '.!?,;'):
						result+=','
				result += c
			else:
				currentJapanese+=c
		if(currentJapanese!=''):
			result += katsu.romaji(currentJapanese).lower()
			currentJapanese=''
		return result
	except Exception as e:
		return phrase


# import pykakasi
# kks = pykakasi.kakasi()

# text='[generic] (discourteous if used for a superior) 貴方達'
# text = "せっかく 神奈川まで来たので、鎌倉で 一泊することにしました。"

# def transliterateJapaneseNew(text):
# 	result = kks.convert(text)
# 	toto = ''
# 	for item in result:
# 		# print("{}[{}] ".format(item['orig'], item['hepburn']), end='')
# 		fusion1=item['hepburn']
# 		if(fusion1 == ' '):
# 			toto+=' '
# 			continue
# 		coucou=transliterateJapaneseOld(item['orig'])
# 		fusion2=coucou.replace(' ','')
# 		# print(f'fusion1: [{fusion1}]')
# 		# print(f'fusion2: [{fusion2}]')
# 		# print(f'coucou: [{coucou}]\n')
# 		if(not coucou.startswith('ichi')):#fusion1==fusion2):
# 			toto += coucou+' '
# 		else:
# 			toto+=fusion1+' '
# 	return toto


# def transliterateJapanese(text):
# 	try:
# 		return transliterateJapaneseNew(text)
# 	except Exception as e:
# 		transliterateJapaneseOld(text)
