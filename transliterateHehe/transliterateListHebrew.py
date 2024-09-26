
import os
import aiohttp
import asyncio
import functools
from transliterateHehe.transliterateHebrew import transliterateHebrew

# class PhraseTraduite:
# 	def __init__(self, original, translation, romanized=''):
# 		self.original = original
# 		self.translation = translation
# 		self.romanized = romanized
# 	def __str__(self) -> str:
# 		return (f'{self.original} ({self.romanized}) : {self.translation}')

# https://nakdan.dicta.org.il/

def getData(sentence):
	sentence=sentence.replace('"','\\"').replace("'","\\'")
	data = '{"task":"nakdan","data":"'+sentence+'","addmorph":true,"keepqq":false,"matchpartial":true,"nodageshdefmem":false,"patachma":false,"keepmetagim":true,"genre":"modern"}'
	return data.encode('utf-8')


def getFirstOption(object):
	if(object['sep']):
		return object['word']
	else:
		return object['options'][0][0]



# 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
# 'sec-ch-ua-mobile': '?0',
# 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
# 'sec-ch-ua-platform': '"macOS"',


headers = {
	'authority': 'nakdan-4-0.loadbalancer.dicta.org.il',
	'content-type': 'text/plain;charset=UTF-8',
	'accept': '*/*',
	'origin': 'https://nakdan.dicta.org.il',
	'sec-fetch-site': 'same-site',
	'sec-fetch-mode': 'cors',
	'sec-fetch-dest': 'empty',
	'referer': 'https://nakdan.dicta.org.il/',
	'accept-language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,he-IL;q=0.6,he;q=0.5,zh-CN;q=0.4,zh;q=0.3',
}


async def getNikud2(session, sentence):
	async with session.post('https://nakdan-4-0.loadbalancer.dicta.org.il/api', headers=headers, data=getData(sentence)) as resp:
		# try:
		myjson = await resp.json()
		words=list(map(getFirstOption, myjson))
		sentence2=functools.reduce(lambda a, b: a+b, words)
		return sentence2
		# except Exception as e:
		# 	return sentence

def improve(sentence):
  return sentence.replace('\n', ' ').strip()

async def getResults(sentences):
	async with aiohttp.ClientSession() as session:
		tasks = []
		for sentence in sentences:
			tasks.append(asyncio.ensure_future(getNikud2(session, improve(sentence.original))))
		all_results = await asyncio.gather(*tasks)
		return all_results

# async
def computeRomanizedHebrewSub(phrases):
	nikuds=asyncio.run( getResults(phrases) ) # asyncio.run(...) # await
	romanizedList=list(map(transliterateHebrew, nikuds))
	for i, phrase in enumerate(phrases):
		phrase.romanized=romanizedList[i]


# https://testdriven.io/blog/flask-async/
# async
def transliterateListHebrew(phrases):
	length=len(phrases)
	num=int(length/1000)
	for i in range(num+1):
		print(i*1000)
		computeRomanizedHebrewSub(phrases[i*1000:(i+1)*1000]) # await

