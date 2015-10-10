# WeblioSearcher
指定された英単語の意味をWeblio英和辞典からオンラインで取得するプログラム  

現在、コマンドラインからの複数問い合わせにまで対応
ただ、出力の形式は不完全でオプションも付けられない。

↓こんな感じに使いたい

例1: コマンドラインから問い合わせ

    $python WeblioSearcher.py program
    [名詞]  1.プログラム、番組表
            2.a 計画，予定; 予定表 〔for〕
              b ...
            3. ...
    [動詞]  1.
    ...

---------------------------------------------------------------------------

例2: モジュールとして使用

    import WeblioSearcher
    meaning = WeblioSearcher.getmeaning('program')
    print(meaning.noun)
    >> ["プログラム、番組表"][["計画、予定;予定表"]["..."]][...]...]
 
