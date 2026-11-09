class Person:
    def __init__(self,name,age,country):
        self.name = name
        self.age = age
        self.country = country

    def greet(self):
        return f'{self.name} is {self.age} years old'

    def is_adult(self):
        return self.age >= 30

    def describe(self):
        status = 'старая' if self.is_adult() else 'молодая'
        return f'{self.name} is {self.age} лет, {status}'





person = Person('Anna',55,'Russia')
print(person.describe())