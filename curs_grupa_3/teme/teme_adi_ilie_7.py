'''1.Git setup

OBLIGATORIU!
Git setup: (ne ajuta sa ne expunem proiectele angajatorilor - super important)
https://drive.google.com/file/d/1yaURoa2VGyCARQ7BUZ-gplnMTxnJjRuz/view?usp=sharing

OPTIONAL
How to use gitignore: (ne ajuta sa ignoram fisiere pe care nu vrem sa le expunem)
https://drive.google.com/file/d/17NVuy28nspPt5_DzynmD0CF7mbmiVzY9/view?usp=sharing
'''

# https://github.com/cobradinbalcani/intro.git

# from teme_adi_ilie_5 import print_spatiu
import math
# print_spatiu()
from abc import (
    ABC,
    abstractmethod,
)

'''2. Faceti exercitiul dupa ce ati urcat proiectul (tot ce am facut pana acum impreuna)

ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’

INHERITANCE
Clasa Patrat - mosteneste FormaGeometrica
constructor pt latura

ENCAPSULATION
latura este proprietate privata
Implementati getter, setter, deleter pt latura
Implementati metoda ceruta de clasa abstracta

Clasa Cerc - mosteneste FormaGeometrica
constructor pt raza
raza este proprietate privata
Implementati getter, setter, deleter pt raza
Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte

POLYMORPHISM 
Definiti o noua metoda descrie() - printati ‘Eu nu am colturi’

Creati un obiect de tip Patrat si jucati-va cu metodele lui
Creati un obiect de tip Cerc si jucati-va cu metodele lui
'''


class FormaGeometrica(ABC):  # ABSTRACTION
    pi = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):  # POLYMORPHISM mai jos
        print('Cel mai probabil am colturi.')


class Patrat(FormaGeometrica):  # INHERITANCE

    def __init__(self, latura):
        self.__latura = latura

    @property  # ENCAPSULATION
    def lungime(self):
        print(f'Getter: lungimea este de {self.__latura} cm.')
        return self.__latura

    @lungime.setter  # ENCAPSULATION
    def lungime(self, latura):
        print(f'Setter: Noua lungime este de: {self.__latura} cm.')
        self.__latura = latura

    @lungime.deleter  # ENCAPSULATION
    def lungime(self):
        print('Am sters lungimea.')
        self.__latura = None

    def aria(self):
        print(f'Aria este egala cu : {self.__latura * self.__latura} cm.')


class Cerc(FormaGeometrica):  # INHERITANCE

    def __init__(self, raza):
        self.__raza = raza

    @property  # ENCAPSULATION
    def cercle(self):
        print(f'Getter: raza este de {self.__raza} cm.')
        return self.__raza

    @cercle.setter  # ENCAPSULATION
    def cercle(self, raza):
        print(f'Setter: Noua raza este: {self.__raza} cm.')
        self.__raza = raza

    @cercle.deleter  # ENCAPSULATION
    def cercle(self):
        print('Am sters raza.')
        self.__raza = None

    def aria(self):
        print(f'Aria cercului este de {(self.__raza * self.__raza) * self.pi} cm.')

    def descrie(self):  # POLYMORPHISM cu cel de sus
        print(f'Sunt cerc si nu am colturi.')


patrat1 = Patrat(7)

patrat1.lungime = 6  # set lungime
patrat1.lungime  # get lungime
patrat1.aria()
del patrat1.lungime  # del lungime
patrat1.lungime  # get lungime
patrat1.descrie()

cerc1 = Cerc(2)

cerc1.cercle = 4  # set cercle
cerc1.cercle  # get cercle

cerc1.aria()
del cerc1.cercle  # del cercle
cerc1.cercle  # get cercle
cerc1.descrie()

''' 3. Actualizati proiectul pe github facand un push la noul cod
In Folder de teme ajunge sa puneti doar linkul cu proiectul vostru public'''
