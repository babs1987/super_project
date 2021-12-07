import math
class Math():
    @staticmethod
    def maximum(one, two, three, four):
        return max(one, two, three, four)

    @staticmethod
    def minimum(one, two, three,four):
        return min(one, two, three, four)

    @staticmethod
    def summa(one, two, three,four):
        return (one + two + three + four)

    @staticmethod
    def minus (one, two, three, four):
        return (one- two - three - four)

    @staticmethod
    def factor(num):
        return math.factorial(num)

print(Math.maximum(1,10,3,8))
print(Math.minimum(1,2,5,6))
print(Math.summa(1,2,3,4))
print(Math.minus(50,2,3,4))
print(Math.factor(2))