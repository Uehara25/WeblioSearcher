# -*- coding: utf-8 -*-
# Script Name	: WeblioSearcher.py
# Author		: Uehara25
# Created		: 
# Last Modified :
# Version		: 


# Modifications	: 

# Description	: 英単語の意味ををWeblioから取得する。



import codecs
import sys
import requests
import io

import meaning
import weblio_parser

class WeblioSearcher:
	def __init__(self):
		""" 初期化 """
		self.weblioURL = "http://ejje.weblio.jp/content/"
		self.parser = weblio_parser.WeblioParser()


	def getsource(self, word):
		""" ソースを取得する """
		url = self.weblioURL + word
		return urllib.request.urlopen(url).read()

	def getmeaning(self, word):
		""" Meaningオブジェクトを返す。　"""

		src = requests.get(self.weblioURL + word)
		self.parser.feed(src.text)
		return meaning.Meaning(self.parser.getdata())

	def _adjust(self, string):
		""" パースされたデータを変換しやすい形式に整形する """
		# ここで何らかの整形処理
		adjusted = string

		return adjusted

if __name__ == "__main__":
	
	## init
	sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
	searcher = WeblioSearcher()
	meaning = searcher.getmeaning("interpolate")

	print(meaning.all)