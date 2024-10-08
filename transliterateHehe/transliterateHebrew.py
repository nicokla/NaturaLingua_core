

he2la2 = [[u"ג'",u'j'], [u' נְ',u' ne'], [u' מְ',u' me'], [u' לְ',u' le'], [u' וְ',u' ve'],[u' יְ',u' ye'],[u' רְ',u' re'],[u' וֵּ',u've'],[u' תְּ',u'te'],[u' נְּ',u'ne'],[u' מְּ',u'me'],[u'א ',u' '], [u'א,',u','], [u'א.',u'.'], [u'א?',u'?'],[u'א!',u'!'], [u' א',u' '],[u',א',u','], [u'.א',u'.'],[u'?א',u'?'],[u'!א',u'!'], [u'א',u'\''],[u'ז',u'Z'],[u'כָל ',u'KhoL '],[u'כָּל ',u'KoL '],[u'ר',u'R'],[u'ת',u'T'],[u'יֽ',u''], [u'יי',u'Y'],[u'ִי',u'i'], [u'יִ',u'i'],[u'י',u'Y'],[u'ִ',u'i'],[u'ק',u'K'],[u'ד',u'D'],[u'ג',u'G'],[u'ל',u'L'],[u'ט',u'T'],[u'ס',u'S'],[u'מ',u'M'],[u'ם',u'M'],[u'נ',u'N'],[u'ן',u'N'],[u'צ',u'Ts'],[u'ץ',u'Ts'],[u'וו',u'V'],[u'ֹו',u'o'], [u'וֹ',u'o'],[u'וּ',u'u'],[u'וֽ',u''], [u'ון',u'on'],[u'ו',u'V'],[u'שׁ',u'Sh'],[u'שׂ',u'S'],[u'ש',u'Sh'],[u'פּ',u'P'],[u'פ',u'F'],[u'ף',u'F'],[u'כּ',u'K'],[u'כ',u'Kh'],[u'ך',u'Kh'],[u'בְּ',u'Be'],[u'בּ',u'B'],[u'ב',u'V'],[u'ה ',u' '],[u'ה,',u','],[u'ה.',u'.'],[u'ה?',u'?'], [u'ה!',u'!'], [u'ה',u'H'],[u'חַ,',u'aKh,'],[u'חַ ',u'aKh '],[u'חַ!',u'aKh!'],[u'חַ?',u'aKh?'],[u'חַ.',u'aKh.'],[u'ח',u'Kh'],[u' ע',u' '], [u',ע',u','], [u'.ע',u'.'], [u'?ע',u'?'], [u'!ע',u'!'], [u'עַ ',u'a '],[u'עַ,',u'a,'],[u'עַ.',u'a.'],[u'עַ!',u'a!'],[u'עַ?',u'a?'],[u'ע ',u""],[u'ע,',u","],[u'ע.',u"."],[u'ע?',u"?"],[u'ע!',u"!"],[u'ע',u"'"],[u'ַ',u'a'],[u'ֱ',u'e'],[u'ֲ',u'a'],[u'ֳ',u'a'],[u'ָ',u'a'],[u'ֵ',u'e'],[u'ֶ',u'e'],[u'ֻ',u'u'],[u'ֹ',u'o'],[u'ְ',u''],[u'ּ',u''],[u'\\u05bd',u'']]


def transString(langue2lat, string):
	string=' '+string+' '
	for k in langue2lat:
		string=string.replace(k[0], k[1])
	return string.strip()

def enleveNonLatin(mot):
	mot2=""
	for c in mot:
		if(ord(c)<128):
			mot2+=c
	return mot2

def lastStep(phrase):
	phrase=phrase.lower() # can comment out if wanna see the vowels
	phrase=phrase.replace('|', ' ')
	return phrase

def transliterateHebrew(s):
	return lastStep(enleveNonLatin(transString(he2la2, s)))


# ----------------------

# he2la2 = [[u'א',u'@'],[u"ג'",u'j'], [u' נְ',u' ne'], [u' מְ',u' me'], [u' לְ',u' le'], [u' וְ',u' ve'],[u' יְ',u' ye'],[u'ז',u'z'],[u'כָל ',u'Hol '],[u'כָּל ',u'kol '],[u'ר',u'r'],[u'ת',u't'],[u'יֽ',u''],[u'ִי',u'i'], [u'יִ',u'i'],[u'י',u'y'],[u'ִ',u'i'],[u'ק',u'q'],[u'ד',u'd'],[u'ג',u'g'],[u'ל',u'l'],[u'ט',u't'],[u'ס',u's'],[u'מ',u'm'],[u'ם',u'm'],[u'נ',u'n'],[u'ן',u'n'],[u'צ',u'ts'],[u'ץ',u'ts'],[u'ֹו',u'o'], [u'וֹ',u'o'],[u'וּ',u'u'], [u'ון',u'on'],[u'ו',u'w'],[u'שׁ',u'š'],[u'שׂ',u's'],[u'ש',u'š'],[u'פּ',u'p'],[u'פ',u'p'],[u'ף',u'f'],[u'כּ',u'k'],[u'כ',u'k'],[u'ך',u'H'],[u'בּ',u'b'],[u'ב ',u'v '],[u'ב',u'b'], [u'ה',u'h'],[u'חַ,',u'aH,'],[u'חַ ',u'aH '],[u'חַ!',u'aH!'],[u'חַ?',u'aH?'],[u'חַ.',u'aH.'],[u'ח',u'H'],[u'ע',u"3"],[u'ַ',u'a'],[u'ֱ',u'e'],[u'ֲ',u'a'],[u'ֳ',u'a'],[u'ָ',u'a'],[u'ֵ',u'e'],[u'ֶ',u'e'],[u'ֻ',u'u'],[u'ֹ',u'o'],[u'ְ',u''],[u'ּ',u''],[u'\\u05bd',u'']]


# def transString(langue2lat, string):
# 	string=' '+string+' '
# 	for k in langue2lat:
# 		string=string.replace(k[0], k[1])
# 	return string.strip()

# def transliterateHebrew(s):
# 	try:
# 		return transString(he2la2, s)
# 	except Exception as e:
# 		return s
