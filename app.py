class Person: #tom usgeer ehelne
    def __init__(self, name:str, age:int):
        self.__name = name
        self.__age = age

    def say_hi(self):
        print('Hi I am', self.__name, self.__age) #dooguur 2 zuraastai baival functseer l ajillna

class Student(Person): # v skobkah stariy class
    def __init__(self, name,age,code):
        super().__init__(name, age) #super() - shuud handdag etseg functsid
        self.code = code

s1 = Student('Tulga', 19, 'm.it2020')
s1.say_hi()
print(s1.code)

class Worker(Person):
    def __init__(self, name, age, profession):
        super().__init__(name, age) #super() - shuud handdag
        self.profession = profession

w1 = Worker('Bayar', 23, 'Kamenshik')
w1.say_hi()
print(w1.profession)
