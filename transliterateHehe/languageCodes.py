
# http://www.lingoes.net/en/translator/langcode.htm
# https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes?oldid=376677794
languageToCodes={
	'arabic':['ar','ar-EG','ar-SA','ar-LB','ar-MA','ar-SY','ar-IQ','ar-JO'],
	'chinese':['zh','zh-CN','zh-TW','zh-CHS','zh-Hans','zh-HK','zh-MO','zh-Hant','zh-CHT','zh-SG'],
	'tagalog':['tl','tl-PH'],
	'french':['fr','fr-FR','fr-CA','fr-BE','fr-CH'],
	'greek':['el','el-GR'],
	'hebrew':['he','he-IL','iw','iw-IL'],
	'hindi':['hi','hi-IN'],
	'italian':['it','it-IT'],
	'japanese':['ja','ja-JP'],
	'korean':['ko','ko-KR'],
	'persian':['fa','fa-IR'],
	'portuguese':['pt','pt-BR','pt-PT'],
	'russian':['ru','ru-RU'],
	'spanish':['es','es-AR','es-ES','es-MX'],
	'thai':['th','th-TH'],
	'turkish':['tr','tr-TR'],
	'vietnamese':['vi','vi-VN'],
	'english':['en','en-CA','en-US','en-GB','en-AU']
}


def getCode(langue):
	if(langue in languageToCodes):
		return languageToCodes[langue][0]
	else:
		return langue[:2]

codeToLanguage={}
for key in languageToCodes:
	for stuff in languageToCodes[key]:
		codeToLanguage[stuff]=key

def getLanguage(code):
	codeSmall=code[:2]
	return codeToLanguage[codeSmall]



