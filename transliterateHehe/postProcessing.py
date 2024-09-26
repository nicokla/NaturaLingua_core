


def postProcessing(fileName, language):
	replacementsAll={'&lrm;':'','&rlm;':'','<i>':' ', '</i>':' ', '،':',', '。':'.', '،':',', '؟':'?', '！':'!','，':',', '\xa0':' ', '\u202f':' ', '\u202c':'', '{\i1}':'', '\u202b':'', '\u200f':'', '\\ N':' ', '\\N':' ','？':'?','{\\an8}':''}
	if(language=='ja'):
		replacementsOthers = {'ochichi':'otou', 'ohaha':'okaa','Ochichi':'Otou', 'Ohaha':'Okaa','atakushi':'atashi', 'konnichiha': 'konnichiwa', 'nippon':'nihon', 'Nippon':'Nihon', 'Konnichiha': 'Konnichiwa'}
	elif(language in ['he','he-IL']):
		replacementsOthers = {'khakha':'kakha', ' beli ':' bli ', "ha '":"ha ", "ka'n":'kan', "she '":'she ', "ve '":'ve ', "be '":"be ", "yay":"ya", 'layv':'lav', ' k ze':' ka ze',' k ':' ke '}
	else:
		replacementsOthers={}
	replacements=dict(replacementsOthers, **replacementsAll)
	lines = []
	with open(fileName) as infile:
		for line in infile:
			for src, target in replacements.items():
				line = line.replace(src, target)
			lines.append(line)
	with open(fileName, 'w') as outfile:
		for line in lines:
			outfile.write(line)


