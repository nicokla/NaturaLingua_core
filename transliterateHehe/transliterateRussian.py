

ru2la = [[u"о",u'o'],[u"О",u'O'],[u'Щ',u'Shtsh'],[u'щ',u'shtsh'],[u'Х',u'Kh'],[u'х',u'kh'],[u'Ч',u'Tsh'],[u'ч',u'tsh'],[u'Ш',u'Sh'],[u'ш',u'sh'],[u'Ц',u'Ts'],[u'ц',u'ts'],[u'Ё',u'Io'],[u'ё',u'io'],[u'е',u'ie'],[u'ю',u'iu'],[u'Е',u'Ie'],[u'Ю',u'Iu'],[u'Я',u'Ia'],[u'я',u'ia'],[u'а',u'a'],[u'з',u'z'],[u'э',u'e'],[u'р',u'r'],[u'т',u't'],[u'у',u'u'],[u'и',u'i'],[u'п',u'p'],[u'с',u's'],[u'д',u'd'],[u'Ф',u'f'],[u'г',u'g'],[u'ж',u'j'],[u'к',u'k'],[u'л',u'l'],[u'м',u'm'],[u'в',u'v'],[u'б',u'b'],[u'н',u'n'],[u'й',u'y'],[u'А',u'A'],[u'З',u'Z'],[u'Э',u'E'],[u'Р',u'R'],[u'Т',u'T'],[u'У',u'U'],[u'И',u'I'],[u'П',u'P'],[u'С',u'S'],[u'Д',u'D'],[u'ф',u'F'],[u'Г',u'G'],[u'Ж',u'J'],[u'К',u'K'],[u'Л',u'L'],[u'М',u'M'],[u'В',u'V'],[u'Б',u'B'],[u'Н',u'N'],[u'Й',u'Y']]


la2ru = []
for l in ru2la:
	la2ru.append([l[1],l[0]])

def latinToRus(s):
	for k in la2ru:
		s = s.replace(k[0], k[1])
	return s

def transliterateRussian(s):
	for k in ru2la:
		s = s.replace(k[0], k[1])
	return s