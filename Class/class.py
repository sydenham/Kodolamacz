from math import sqrt


class FunkcjaKwadratowa:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def rozwiaz(self):
        if self.a == 0 and self.b == 0:
            print("To stała", self.c, 'Nie zwracam wyniku')
        elif self.a == 0:
            print("To funkcja liniowa. NIe zwracam wyniku")
        else:
            delta = self.b**2 - 4*self.a*self.c
            if delta < 0:
                print("Brak miejsc zerowych. Zwracam None")
                return None
            elif delta == 0:
                x = -self.b / (2*self.a)
                print("Miejsce zerowe wynosi", x, "i zwracam jedną wartość")
                return  x
            else:
                x1 = (-self.b + sqrt(delta))/(2*self.a)
                x2 = (-self.b - sqrt(delta))/(2*self.a)
                print('Miejsca zerowe to:', x1, 'oraz', x2, "Zwracam krotkę")
                return x1, x2

class Zespolona:

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def modul(self):
        z = sqrt(self.re**2+self.im**2)
        print('Modul z liczby {}{}{}i to:'.format(self.re, '+-'[self.im < 0], abs(self.im)), z)
        return z

    @staticmethod
    def dodaj(a, b):
        result = Zespolona(a.re + b.re, a.im + b.im)
        print("Wynik to {}{}{}i".format(result.re, '+-'[result.im < 0], abs(result.im)))
        return result

    @staticmethod
    def mnoz(a, b):
        temp_re = a.re * b.re + -(a.im * b.im)
        temp_im =  a.re * b.im + a.im * b.re
        result = Zespolona(temp_re, temp_im)
        print("Wynik to {}{}{}i".format(result.re, '+-'[result.im < 0], abs(result.im)))
        return result

class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik



def main():
    a = FunkcjaKwadratowa(1, 5, 0)
    b = a.rozwiaz()
    print(b)

    zes = Zespolona(4.88, 12)
    zes2 = Zespolona(7.55, -4.2)
    print(zes.modul())
    print(Zespolona.modul(zes))

    #print(modul(zes))
    #print(zes.modul(zes))
    #print(zes.modul(zes2))

    Zespolona.dodaj(zes, zes2)
    Zespolona.mnoz(zes, zes2)

if __name__ == "__main__":
    main()