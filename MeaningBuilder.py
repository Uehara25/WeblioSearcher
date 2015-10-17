import meaning

"""


[品詞]            part : part of speech より
[他動詞or自動詞]   tori : transive or intransive より
[A, B, ...]      u_alph : upper alphabet より
[1, 2, ...]      number : そのまま
[a, b, ...]      alph : alphabet より
[意味]            mean : meaning より
"""

class MeaningBuilder:
    def __init__(self):
        self.meaning = meaning.Meaning()

    def add_part(self, part):
        pass

    def add_tori(self, tori):
        pass

    def add_u_alph(self, u_alph):
        pass

    def add_number(self, number):
        pass

    def add_alph(self, alph):
        pass

    def add_mean(self, mean):
        pass

    def get_meaning(self):
        return self.meaning

if __name__ == "__main__":
    import weblioEJScraper
