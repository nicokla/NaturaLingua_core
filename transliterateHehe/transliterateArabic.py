ar2la=[[u'لإ',u'\'iL'],[u'لأ',u'\'aL'],[u'إ',u'\'i'],[u'أ',u'\'a'],[u'ا',u'\''],[u'ر',u'R'],[u'ز',u'Z'],[u'ش',u'Sh'],[u'س',u'S'],[u'ص',u'S*'],[u'ض',u'D*'],[u'ط',u'T*'],[u'ظ',u'Th*'],[u'ع',u'3'],[u'غ',u'Gh'],[u'ح',u'7'],[u'خ',u'Kh'],[u'ج',u'J'],[u'ت',u'T'],[u'ث',u'Th'],[u'د',u'D'],[u'ذ',u'Th'],[u' و',u' W'],[u'و',u'W'],[u'ي',u'Y'],[u'ق',u'Q'],[u'ف',u'F'],[u'ة',u'a'],[u'ه',u'H'],[u'ك',u'K'],[u'ل',u'L'],[u'م',u'M'],[u'ب',u'B'],[u'ن',u'N'],[u'ى',u'aa'],[u'ُ',u'u'],[u'ِ',u'i'],[u'َ',u'a']]

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

