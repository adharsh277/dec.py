class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1)
# 34


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()
# 4


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print('iam '+self.age)
