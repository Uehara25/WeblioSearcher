# WeblioSearcher
指定された英単語の意味をWeblio英和辞典からオンラインで取得するプログラム  
以下のように使いたい  

    $python WeblioSearcher.py program
    [名詞]  1.プログラム、番組表
            2.a 計画，予定; 予定表 〔for〕
              b ...
            3. ...
    [動詞]  1.
    ...

---------------------------------------------------------------------------

    import WeblioSearcher
    searcher = WeblioSearcher.WeblioSearcher()
    meaning = searcher.getmeaning('program')
    print(meaning.noun)
    >> ["プログラム、番組表"][["計画、予定;予定表"]["..."]][...]...]
 
 
もっといい形式があれば教えてください。  
当方pythonというか、プログラミング初心者なので、勝手がわからないです。  
