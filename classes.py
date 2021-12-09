
#Зачем блеать создавать экземпляры класса который невозмрожно инициализировать


class car(object):
    def name(self):
        print("car 1")
    def length(self):
        print(210)
    def width(self):
        print(140)
    def height(self):
        print(180)
    def engine_type(self):
        print("disel")
    def engine_stroke(self):
        print(4)
    def doors(self):
        print(4)
    def color(self):
        print("silver")
    def power(self):
        print(12345678)


class human(object):
    def name(self):
        print("oleg")
    def height(self):
        print(175)
    def weight(self):
        print(70)
    def specialization(self):
        print("street cleaner")

s=human()
s.name()




