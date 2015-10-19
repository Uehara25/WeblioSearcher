# -*- coding: utf-8 -*-
import meaning
from enum import Enum 

class Level(Enum):
    part = 0
    tori = 1
    u_alph = 2
    number = 3
    alph = 4
    mean = 5

class MeaningBuilder:

    def __init__(self):
        self.level = Level.part
        self.meaning = meaning.Meaning()

    def add_part(self, part):
        self.level = Level.part
        self.meaning.string += '\n' + part

    def add_tori(self, tori):
        if self.level != Level.tori:
            self.meaning.string += '\n' + tori
        else:
            print("level error", self.level.name, " at add_tori")

    def add_u_alph(self, u_alph):
        self.level = Level.u_alph
        self.meaning.string += '\n' + u_alph

    def add_number(self, number):
        if self.level == Level.part or self.level == Level.tori or self.level == Level.u_alph:
            self.meaning.string += '\n' + ' ' + number + '.'
            self.level = Level.number
        elif self.level == Level.mean:
            self.meaning.string += '\n' + ' ' + number + '.'
            self.level = Level.number
        else:
            print("level error", self.level.name, " at add_number")

    def add_alph(self, alph):
        if self.level == Level.part or self.level == Level.tori or self.level == Level.u_alph:
            print("level error", self.level.name, " at add_alph")
        elif self.level == Level.number:
            self.level = Level.alph
            self.meaning.string +=  alph + '.'
        elif self.level == Level.mean:
            self.level = Level.alph
            self.meaning.string += '\n' + '   ' + alph + '.'
        else:
            print("level error", self.level.name, " at add_alph")            

    def add_mean(self, mean):
        if self.level == Level.part or self.level == Level.tori:
            self.meaning.string += '\n' + mean
        elif self.level == Level.mean:
            self.meaning.string += '\n' + mean
        else:
            self.meaning.string += mean
            self.level = Level.mean

    def get_meaning(self):
        return self.meaning
