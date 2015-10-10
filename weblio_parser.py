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
		self._maindata = ""

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
			self._maindata += data


	def getdata(self):
		return {"conjugate":self._conjugate, "maindata":self._maindata}




