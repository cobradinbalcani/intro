# O O P

class Car:
    #atribute sau fields (in alte limbaje proprietati)
    make = 'Dacia'
    model = None
    year = 2022
    culoare = None
    lista_culori = ['rosu', 'galben', 'magenta']


    #metode
    def accelerare(self):
        print('vrum vruum!')

    def stop(self):
        print('masina s-a oprit!')

    def __init__(self, model_nou, culoare_9, year):
        self.model = model_nou
        self.culoare = culoare_9
        # if type(year) == int:
        #     self.year = year

        if isinstance(year, (int, float)):
            self.year = year

        if culoare_9 in self.lista_culori:
            self.culoare = culoare_9
        else:
            print('culoarea nu exista')



car1 = Car(input('Introdu modelul: '), input('Introdu culoarea: '), 1980)
#car2 = Car(input('Introdu modelul: '), input('Introdu culoarea: '))
# car1 = Car('Logan', 'alb')
car2 = Car('Duster', 'rosu', 1800)


print(car1.model, car1.culoare, car1.year)
print(car2.model, car2.culoare, car2.year)


# car1 = Car()
# car2 = Car()
# car1.model = 'Spring'
# print(car1.model)
# car1.accelerare()
# car2.model = 'Logan'
#
# print(car2.model)
#
# car2.accelerare()



