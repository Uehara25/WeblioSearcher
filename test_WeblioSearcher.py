# Script Name	: test_WeblioSearcher.py
# Author		: Uehara25
# Created		: 
# Last Modified : 
# Version		: 


# Modifications	: 

# Description	: WeblioSearcher.py のテストプログラム


# -*- coding: utf-8 -*-

""" 仕様が確定してないため、まだ書きようがない """

import WeblioSearcher
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

searcher = WeblioSearcher.WeblioSearcher()
meaning = searcher.getmeaning("interpolate")

print(meaning.main)

# ここまで