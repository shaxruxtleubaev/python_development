'''
class Gold:

    def __init__(self, employer, employee):
        self.employer = employer
        # self._employee = employee   ПРиватность
        self.__employee = employee

    def __str__(self):
        return f'{self.__employee} - {self.employer}'

    def _protected(self):
        return f'This method is protected'

print(Gold('John', 'Smith')._protected())
'''
class Home:

    def __init__(self, father, mother, me, phone, computer, clothes):
        self.__father = father
        self.__mother = mother
        self.me = me
        self.phone = phone
        self.computer = computer
        self.clothes = clothes
    
    def __repr__(self):
        return f'{self.__father}, {self.__mother}, {self.me}, {self.phone}, {self.phone}, {self.computer}, {self.clothes}'
print(Home('Папа', 'Мама', "Я", "Телефон", "Компьютер", "Одежды"))

class NewHome(Home):

    def __init__(self, father, mother, me, phone, computer, clothes):
        super().__init__(father, mother, me, phone, computer, clothes)
        
    def __repr__(self):
        return f'{self.__father}, {self.__mother}, {self.me}, {self.phone}, {self.computer}, {self.clothes}'

print(NewHome('Папа', 'Мама', "Я", "Телефон", "Компьютер", "Одежды"))
