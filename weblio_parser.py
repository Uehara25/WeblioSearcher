# -*- coding: utf-8 -*-
"""
 Script Name	: weblio_parser.py
 Author			: Uehara25
 Created		: 
 Last Modified 	:
 Version		: 
 Modifications	: 
 Description	: Weblioのソースコードから必要なデータを抜き出す
"""

from html.parser import HTMLParser


class WeblioParser(HTMLParser):
	""" ネット上からダウンロードしたデータを受け取り、そこから必要な情報だけを取り出すためのクラス

		WeblioSearcherクラスの内部メソッドでちゃんとした整形をするので
		ここでは不必要なデータを切り捨てる程度の処理の予定"""

	def __init__(self):
		HTMLParser.__init__(self)

		# 取得した情報を格納する変数群
		
		# 変化形
		self._conjugate = []

		# 意味本体
		self._maindata = []

		# パース状態保持用変数軍

		self._is_conjugate = False
		self._is_maindata = False

	def handle_starttag(self, tag, attrs):
		# 変化形であるか
		if tag == "div":
			attrs_dict = {t[0]:t[1] for t in attrs}
			if attrs_dict.get("id", None) == "conjugateNavi":
				self._is_conjugate = True

		# 記事本体であるか
		if tag == "div":
			attrs_dict = {t[0]:t[1] for t in attrs}
			if attrs_dict.get("class", None) == "level0":
				self._is_maindata = True


	def handle_endtag(self, tag):
		# 変化形を表すタグの終了処理
		if tag == "div" and self._is_conjugate:
			self._is_conjugate = False

		# 意味データ終了判定
		if tag == "div" and self._is_maindata:
			self._is_maindata = False


	def handle_data(self, data):
		# 変化形を受け取る
		if self._is_conjugate:
			self._conjugate.append(data)

		# 意味データなら追加
		if self._is_maindata:
			self._maindata.append(data)


	def getdata(self):
		return {"conjugate":self._conjugate, "maindata":self._maindata}


class AlphabetPutter:
	def __init__(self):
		self._level = 0

	def put(self):
		self._level += 1
		return chr(97 + (self._level - 1))

	def init(self):
		self._level = 0




class Structure:
	def __init__(self):
		self.level = 0
		self.base = []
		self.first = []
		self.second = []

	def add(self, word):
		if self.level == 0:
			self.base.append(word)
		elif self.level == 1:
			self.first.append(word)
		elif self.level == 2:
			self.second.append(word)
		else:
			print("あり得ないパラメータです")

	def up(self):
		self.level += 1

	def down(self):
		if self.level == 0:
			print("あり得ない操作です")
		elif self.level == 1:
			self.base.append(self.first)
			self.first = []
		elif self.level == 2:
			self.first.append(self.second)
			self.second = []
		else:
			print("どうしてこうなった")
		self.level -= 1




#### test

if __name__ == "__main__":
	import requests
	import sys
	import io

	sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
	parser = WeblioParser()
	src = requests.get("http://ejje.weblio.jp/content/interpolate")
	parser.feed(src.text)
	data = parser.getdata()
	data = data["maindata"]

	"""
	# structure test
	## first
	structure = Structure()
	for x in range(3):
		structure.add("foo")

	print(structure.base)
	## second
	structure = Structure()
	for x in range(3):
		structure.add("base")
		structure.up()
		for y in range(2):
			structure.add("first")
			structure.up()
			for z in range(4):
				structure.add("third")
			structure.down()
		structure.down()

	print(structure.base)
	"""

	# 文字列への変換といこうか・・・

#	print(data)
	l = Structure()
	for d in data:
		if '】' in d:
			if l.level == 0:
				pass
			elif l.level == 1:
				l.down()
			elif l.level == 2:
				l.down()
				l.down()
			else:
				print("] is fukumareteru kedo okasii")

		elif d.isdecimal():

			if l.level == 0:
				l.up()
			elif l.level == 1:
				pass
			elif l.level == 2:
				l.down()
			else:
				pass

		elif d.isalpha() and len(d) == 1 and l.level == 1:

			if l.level == 0:
				print("1 mozi dakedo atteru")
			elif l.level == 1:
				l.up()
			elif l.level == 2:
				l.down()
				l.up()
			else:
				print("incorrect")
		else:
			pass
		l.add(d)

	putter = AlphabetPutter()
	base = ""
	for x in l.base:
		if type(x) is str:
			base += x
		else:
			first = "\n"
			for y in x:
				if type(y) is str:
					first += y
				else:
					second = "\n"
					for z in y:
						second += z
					first += second
			base += first
	print(base)