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

"""

from bs4 import BeautifulSoup
import io
import sys
import requests
import meaning

class Meaning:

    def __init__(self):
        pass

def _get_source(word):
    src = requests.get("http://ejje.weblio.jp/content/" + word)
    return src.text

class A:
    def __init__(self, word):
        self.word = word

    def get_all(self):
        return self.word

def getmeaning(word):
    return A(word)

def _getmeaning(word):
    
    src = _get_source(word)
    
    soup = BeautifulSoup(src, 'html5lib')

    # 最初に来た辞書に含まれるデータを含む行のリストを抽出する
    kiji = soup.find("div", class_='kiji')
    lines = kiji.find_all("div", class_="level0")

    """
    品詞が来たらここに追加する
    """

    speech_set = {}
    base2 = []

    n = []
    t = []
    ua = []
    a = []

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
                speech_set[node.get_text(strip=True)] = [temp]
            else:
                speech_set[node.get_text(strip=True)] = []
            continue

       # 大文字見出しが含まれる場合
        uppar_alphabet = line.find('span', class_="lvlUAH")
        if uppar_alphabet is not None:
            ua.append(uppar_alphabet.get_text(strip=True))
            uppar_alphabet.extract()
            continue

       # 1, a などと説明を表す行の処理
        text = line.find('p', class_="lvlB")
        number = line.find('p', class_="lvlNH")
        alphabet = line.find('p', class_="lvlAH")
 
        if text is not None:
            t.append(text.get_text(strip=True)) 
            text.extract()
        if alphabet is not None:
            if alphabet.get_text(strip=True) != '':
                a.append(alphabet.get_text(strip=True))
                alphabet.extract()
        if number is not None:
            if number.get_text(strip=True) != '':
                n.append(number.get_text(strip=True))
                number.extract()
    return meaning.Meaning(word)

"""
    print(speech_set)
    print(ua)
    print(n)
    print(a)
    print(t)
"""


if __name__ == "__main__":
    # テストコード
    word_list = ["account","act","addition"]#,"adjustment","advertisement","agreement","air","amount","amusement","animal","answer","apparatus","approval","argument","art","attack","attempt","attention","attraction","authority","back","balance","base","behavior","belief","birth","bit","bite","blood","blow","body","brass","bread","breath","brother","building","burn","burst","business","butter","canvas","care","cause","chalk","chance","change","cloth","coal","color","comfort","committee","company","comparison","competition","condition"]
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    count = 0
    print("hit")
    for word in word_list:
        m = _getmeaning(word)
        print(m)
        print("alltext = ", m.get_all())
        count += 1
        print(count)