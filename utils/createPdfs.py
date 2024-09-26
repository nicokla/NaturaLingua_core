
# https://pzwiki.wdka.nl/mediadesign/Weasyprint
# https://stackoverflow.com/questions/4140466/shrink-and-merge-pdfs-in-python
# https://pypi.org/project/pdfnup/

from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration


universal_css='''
@media print {
  @page {
    margin: 0.3in;
    size: A4;
    @top-right {
      content: counter(page);
    }
  }
  @page :first {
    @top-right {
      content: "";
    }
  }
}
'''

font_configNotJap = FontConfiguration()
cssNotJap=CSS(string='''
body {
	font-family: sans-serif;
}
p {
	margin: 0;
	padding: 0;
	font-family: sans-serif;
}
'''+universal_css, font_config=font_configNotJap)

def getCssName(language):
	if language == 'chinese':
		return 'Noto Sans SC', 'sans-serif'
	elif language == 'japanese':
		return 'Noto Sans JP', 'sans-serif'
	elif language == 'hindi':
		return 'Mukta', 'sans-serif'
	elif language == 'korean':
		return 'Noto Serif KR', 'serif'
	elif language == 'thai':
		return 'Sarabun', 'sans-serif'


def getCssSub(language):
	cssName, serifOrNot=getCssName(language)
	font_config = FontConfiguration()
	css = CSS(string=f'''
body {{
	font-family: '{cssName}', {serifOrNot};
}}
p {{
	margin: 0;
	padding: 0;
	font-family: '{cssName}', {serifOrNot};
}}
'''+universal_css, font_config=font_config)
	return font_config, css


languagesSpecials=['chinese','thai','japanese','korean','hindi']
font_config_s={}
css_s={}
for language in languagesSpecials:
	font_config, css = getCssSub(language)
	font_config_s[language] = font_config
	css_s[language] = css

def getCss(language, alphabetId):
	if((alphabetId in ['original', 'both']) and (language in languagesSpecials)):
		return css_s[language], font_config_s[language]
	else:
		return cssNotJap, font_configNotJap

def getColor(firstChar):
  if firstChar == '-':
    return '#0000FF'
  elif firstChar == ' ':
    return '#EE6A00'
  else: #elif firstChar == '*':
    return '#2CAB2C'


def getHtml(fileName, title, isYoutube=True):
	if(isYoutube):
		debut = f"""
			<h2 style="text-align: center;"><a href="{title}">{title}</a></h2>
			"""
			# 			<h4 style="text-align: center;">Document made with <a href="https://getyoutubesubtitles.netlify.app">https://getyoutubesubtitles.netlify.app</a></h4>
	else:
		debut = f"""
			<h2 style="text-align: center;">{title}</h2>
			"""
			# 			<h4 style="text-align: center;">Document made with <a href="https://getmoviessubtitles.netlify.app">https://getmoviessubtitles.netlify.app</a></h4>
	txt = ''
	fh = open(fileName, 'r')
	lines = fh.readlines()
	wasGap=True
	numJap=0
	for index, line in enumerate(lines):
		if(len(line) <= 1):
			wasGap = True
			numJap = 0
			txt+='<br style="line-height:14px;">'
			continue
		if(line.startswith('   ')):
			numJap+=1
		shouldHaveSpace = index >= 1 and (lines[index-1].startswith('    ') and (line.startswith('- ') or line.startswith('* ')))
		marginTop='0px'
		if shouldHaveSpace:
			marginTop='6px'			
		if(not('[' in line)):
			txt+= f'<p style="margin-top: {marginTop}; margin-bottom: 0px; color: {getColor(line[0])};">{line[:-1]}</p>\n'
			continue
		i=-1
		while(line[i] != '[' and i > -15):
			i-=1
		if(i == -15):
			continue
		content = ''
		canAddTime = (numJap % 6 == 0) and shouldHaveSpace
		if wasGap or canAddTime:
			content=f'<p style="margin-top: 6px; margin-bottom: 3px; color: #777777;">{line[i:-1]}</p>'
		content += f'<p style="margin-top: {marginTop}; margin-bottom: 0px; color: {getColor(line[0])};">{line[2:i]}</p>\n'
		txt += content
		wasGap = False
	return (debut + f'<div>\n{txt}\n</div>')



import os

def createPdfYoutube(videoId, inputFileName, outputFileName, language, alphabetId):
	title=f'https://youtu.be/{videoId}'
	myString=getHtml(inputFileName, title, True)
	html = HTML(string=myString)
	css, font_config = getCss(language, alphabetId)
	# return html.write_pdf(...)
	html.write_pdf(outputFileName, stylesheets=[css], font_config=font_config)


def createPdfMovie(title, inputFileName, outputFileName, language, alphabetId):
	myString=getHtml(inputFileName, title, False)
	html = HTML(string=myString)
	css, font_config = getCss(language, alphabetId)
	# return html.write_pdf(...)
	html.write_pdf(outputFileName, stylesheets=[css], font_config=font_config)



