# -*- coding: utf-8 -*-
"""
資料が見当たらないので、いくつかの検索結果をもとに考え、構造は以下のようになっているとした。

[出典辞書] - [品詞] - [他動詞or自動詞] - [A, B, ...] - [1, 2, ...] - [a, b, ...] - [意味]

出典時点は先頭にに来るものとする。これはほぼ「研究社 新英和中辞典」からとなる。
特定は<div class="kiji"></div>内にあることを利用して行う。

出典辞書以下の項目は、一行一行を囲む<div class="level0"></div>の要素を抽出し、その中から分岐して取り込む
[品詞]は<div class="KnenjSub"></div>内に囲まれていて、[他動詞or自動詞]はさらにその中の<span class="KejjeSm">に囲まれた中に入っている。

[A, B, ...]は、単語の表す量が多いときに番号が多くなりすぎて、分かりにくくなるのを防ぐために挿入されるのだと思う。ほとんど出てこない。
これは<span class="lvlUAH"></span>内に含まれることから特定する。

[1, 2, ...]は品詞ごとの大まかな意味を列挙して表示したときの項目につける番号。
<p class="lvlAH"></p>で特定

[a, b, ...]は、[1, 2, ...]についてさらに細かく意味を列挙するときに用いる。
<p class="lvlAH"></p>で特定

[意味]は意味。
<p class="lvlB"></p>で特定


・項目と変数の対応

[品詞]            part : part of speech より
[他動詞or自動詞]   tori : transive or intransive より
[A, B, ...]      u_alph : upper alphabet より
[1, 2, ...]      number : そのまま
[a, b, ...]      alph : alphabet より
[意味]            mean : meaning より


"""

from bs4 import BeautifulSoup
import io
import sys
import requests
import meaning
import MeaningBuilder

def _get_source(word):
    src = requests.get("http://ejje.weblio.jp/content/" + word)
    return src.text


def getmeaning(word):
    
    builder = MeaningBuilder.MeaningBuilder()

    src = _get_source(word)
    
    soup = BeautifulSoup(src, 'html5lib')

    # 最初に来た辞書に含まれるデータを含む行のリストを抽出する
    kiji = soup.find("div", class_='kiji')
    lines = kiji.find_all("div", class_="level0")


    for line in lines:
       # 動詞、他動詞など、タイトルを表すような行であるときの処理
        node = line.find('div', class_="KnenjSub")

        if node is not None:
            temp = ""
            sub = node.find('span', class_='KejjeSm')
            if sub is not None:
                temp = sub.get_text(strip=True)
                sub.extract()
           
            if temp != "":
                builder.add_part(node.get_text(strip=True))
            else:
                builder.add_tori(node.get_text(strip=True))
            continue

        # 大文字見出しが含まれる場合
        u_alph = line.find('span', class_="lvlUAH")
        if u_alph is not None:
            builder.add_u_alph(u_alph.get_text(strip=True))
            u_alph.extract()
            continue

        # 1, a などと説明を表す行の処理
        mean = line.find('p', class_="lvlB")
        number = line.find('p', class_="lvlNH")
        alph = line.find('p', class_="lvlAH")
        
        # 取得する順番実際の並びの反対となるため、一時的に値を保持して処理する
        mean_dat = None
        number_dat = None
        alph_dat =None

        if mean is not None:
            mean_dat = mean.get_text(strip=True)
            mean.extract()
        if alph is not None:
            if alph.get_text(strip=True) != '':
                alph_dat = alph.get_text(strip=True)
                alph.extract()
        if number is not None:
            if number.get_text(strip=True) != '':
                number_dat = number.get_text(strip=True)
                number.extract()
        
        if number_dat is not None:
            builder.add_number(number_dat)
        if alph_dat is not None:
            builder.add_alph(alph_dat)
        if mean_dat is not None:
            builder.add_mean(mean_dat)

        if mean is None and alph is None and number is None:
            builder.add_mean(line.get_text(strip=True))

    return builder.get_meaning()


if __name__ == "__main__":
    # テストコード
    # OGDEN's BASIC ENGLISHより一部拝借
    # http://ogden.basic-english.org/words.html
    word_list = ["account","act","addition","adjustment","advertisement","agreement","air","amount","amusement","animal","answer","apparatus","approval","argument","art","attack","attempt","attention","attraction","authority","back","balance","base","behavior","belief","birth","bit","bite","blood","blow","body","brass","bread","breath","brother","building","burn","burst"]

    # うまく表示されないときは以下のコメントを外すとうまくいくかも
    #sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    count = 0
    string = ""
    for word in word_list:
        m = getmeaning(word)
        count += 1
        string += str(count) + ":" + word + "'s meaning is ..." + m.get_all() + '\n'
        print(str(count) + ":" + word + "'s meaning is ..." + m.get_all())

    with open("out.txt", "w", encoding='utf-8') as fp:
        fp.write(string)
