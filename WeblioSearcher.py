# -*- coding: utf-8 -*-
# Script Name	: WeblioSearcher.py
# Author		: Uehara25
# Created		: 
# Last Modified :
# Version		: 


# Modifications	: 

# Description	: 英単語の意味ををWeblio英和・和英辞典から取得する。



import sys
import io
import requests

import meaning
import weblio_parser


def getmeaning(word):
	""" 英単語を引数で受け取り、Meaningオブジェクトを返す """

	parser = weblio_parser.WeblioParser()
	src = requests.get("http://ejje.weblio.jp/content/" + word)
	parser.feed(src.text)
	data = parser.getdata()
	return meaning.Meaning(data)


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
		for word in sys.argv:
			it_mean = getmeaning(word)
			print("[", word, "]")
			print(it_mean.main, end='\n\n')
