# WeblioSearcher
指定された英単語の意味を以下のWeblio英和辞典からオンラインで取得するプログラム  
英和辞典・和英辞典 - Weblio辞書 : http://ejje.weblio.jp/  
!!未完成です　主な機能自体は完成しているので、ソースが理解できれば使えます
  
使用方法(予定)

例1: コマンドラインから問い合わせ

    $python weblioEJScraper.py program
    [program]
    [名詞]  1.プログラム、番組表
            2.a 計画，予定; 予定表 〔for〕
              b ...
            3. ...
    [動詞]  1.
    ...


---------------------------------------------------------------------------

例2: モジュールとして使用

    ソース
    import weblioEJScraper
    meaning = weblioEJScraper.getmeaning('program')
    print(meaning.get_all())
    アウトプット
    [名詞]  1.プログラム、番組表
            2.a 計画，予定; 予定表 〔for〕
              b ...
            3. ...
    [動詞]  1.
    ...
 
