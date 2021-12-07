class VinilMarket(object):
    def __init__(self,name,date,genre):
        self.name=name
        self.date=date
        self.genre=genre

    def __str__(self):
        return f"Название пластинки {self.name}, Дата Поступления {self.date}, Жанр музыки {self.genre}"

    def __add__(self, other):
        return VinilMarket(self.name + other,self.date+other,self.genre+other)

