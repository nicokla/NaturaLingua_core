

ar2la=[[u'لإ',u'il'],[u'لأ',u'al'],[u'إ',u'i'],[u'أ',u'a'],[u'ا',u'a'],[u'ر',u'r'],[u'ز',u'z'],[u'ش',u'š'],[u'س',u's'],[u'ص',u'ṡ'],[u'ض',u'ḋ'],[u'ط',u'ṫ'],[u'ظ',u'ż'],[u'ع',u'3'],[u'غ',u'ġ'],[u'ح',u'7'],[u'خ',u'ḣ'],[u'ج',u'j'],[u'ت',u't'],[u'ث',u'ṭ'],[u'د',u'd'],[u'ذ',u'ḍ'],[u' و',u' w'],[u'و',u'w'],[u'ي',u'y'],[u'ق',u'q'],[u'ف',u'f'],[u'ة',u'a'],[u'ه',u'h'],[u'ك',u'k'],[u'ل',u'l'],[u'م',u'm'],[u'ب',u'b'],[u'ن',u'n'],[u'ى',u'a'],[u'ُ',u'u'],[u'ِ',u'i'],[u'َ',u'a'],[u'؟',u'?'],[u'ْ',u''],[u'ّ',u'*'],[u'،',u','],[u'ً',u''],[u'ؤ',u'u'],[u'آ',u'aa'],[u'آ',u'aa'],[u'ء',u"'"],[u'ئ',u"'"],[u'١',u"1"],[u'٢',u"2"],[u'٣',u"3"],[u'٤',u"4"],[u'٥',u"5"],[u'٦',u"6"],[u'٧',u"7"],[u'٨',u"8"],[u'٩',u"9"],[u'٠',u"0"]]
# ,[u'٠',u"0"]

def transliterateArabic(string):
	for k in ar2la:
		string=string.replace(k[0], k[1])
	return string


# ====================
# import epitran
# epi = epitran.Epitran('ara-Arab')

# def transliterateArabic(s):
# 	try:
# 		return epi.transliterate(s)
# 	except Exception as e:
# 		return s

