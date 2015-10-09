# Script Name	: WeblioSearcher.py
# Author		: Uehara25
# Created		: 
# Last Modified :
# Version		: 


# Modifications	: 

# Description	: 英単語の意味ををWeblioから取得する。


# -*- coding: utf-8 -*-

from html.parser import HTMLParser
import http.client

class WeblioParser(HTMLParser):
	""" ネット上からダウンロードしたデータを受け取り、そこから必要な情報だけを取り出すためのクラス

		どういった処理ができるのか知らないから、まだ詳しくどうするかは決められないけれども、
		WeblioSearcherクラスの内部メソッドでちゃんとした整形をするので
		ここでは不必要なデータを切り捨てる程度の処理の予定"""

	def __init__(self):
		HTMLParser.__init__(self)

	def handle_starttag(self, tag, attrs):
		pass

	def handle_endtag(self, tag):
		pass

	def handle_data(self, data):
		pass


class Meaning:
	""" プロパティ形式で意味を返すクラス

		使いたい形式が確定次第仕様を決定する """

	def __init__(self, string):
		self._noun = []
		self._verb = []
		# ...

		construct(string)

	def construct(self, string):
		""" string の値を見やすい形に変形し、以下の変数に保存していく

			self._noun,self._verb,...にリストの形で格納する
			細かい仕様はまだ決まってない """
		pass

	def getnoun(self):
		""" 名詞の意味があればそれを返す """
		return self._noun

	noun = property(getnoun)



class WeblioSearcher:
	def __init__(self):
		""" 初期化 """
		self.weblioURL = "http://ejje.weblio.jp/content/program"
		self.Parser = WeblioParser()



	def getmeaning(self, word):
		""" Meaningオブジェクトを返す。　"""

		src = urllib.request.urlopen(self.weblioURL + word).read()
		rawdata = self.Parser.feed(src)
		adjusted = self._adjust(rawdata)
		return Meaning(adjusted)

	def _adjust(self, string):
		""" パースされたデータを変換しやすい形式に整形する """
		# ここで何らかの整形処理
		adjusted = string

		return adjusted

if __name__ == "__main__":
	print("まだ未完成です")
