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

	def getmeaning(self, word):
		""" Meaningオブジェクトを返す。　"""

		self.parser = weblio_parser.WeblioParser()
		self.data = None
		src = requests.get(self.weblioURL + word)
		self.parser.feed(src.text)
		self.data = self.parser.getdata()
		return meaning.Meaning(self.data)


if __name__ == "__main__":
	
	# うまく表示されないときは下のコメントを外す
	# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

	# コマンドラインから受け取った値を処理
	print(sys.argv)
	print(len(sys.argv))
	if len(sys.argv) == 1:
		print(u"何も聞かれてないから、何も答えないよ")
	else:
		sys.argv.pop(0)
		searcher = WeblioSearcher()
		for word in sys.argv:
			it_mean = searcher.getmeaning(word)
			print("[", word, "]")
			print(it_mean.main, end='\n\n')
