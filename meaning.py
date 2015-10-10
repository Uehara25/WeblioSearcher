# -*- coding: utf-8 -*-
# Script Name	: meaning.py
# Author		: Uehara25
# Created		: 
# Last Modified :
# Version		: 


# Modifications	: 

# Description	: weblio_searcherから受け取ったデータを処理しやすい形で提供する

class Meaning:
	""" プロパティ形式で意味を返すクラス

		使いたい形式が確定次第仕様を決定する """

	def __init__(self, data_dict):
		self._conjugate = []
		self._verb = []
		self.all = []
		self.main = ""
		# ...

		self.construct(data_dict)

	def construct(self, data_dict):
		""" string の値を見やすい形に変形し、以下の変数に保存していく

			self._noun,self._verb,...にリストの形で格納する
			細かい仕様はまだ決まってない """
		self._conjugate = data_dict["conjugate"]
		self.all = ''.join(data_dict["conjugate"]) + data_dict["maindata"]
		self.main = data_dict["maindata"].replace('.','.\n')

		# ウザったらしいから語源以下を消去
		self.main, temp0, temp1 = self.main.partition('【語源】')

	def getall(self):
		""" 結果すべてを返す """
		return self.all