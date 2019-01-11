class Licznik:
    ile = 0  # pole statyczne

    def __init__(self):  # konstruktor
        Licznik.ile += 1  # odwołanie do pola statycznego - zwiększa pole'ile' wraz z każdą nową instancją
        self.ktory = Licznik.ile
        self.slowo = ''

        print(f"To jest obiekt nr {Licznik.ile}")

    def __del__(self):  # destruktor, czyli kod, który wykonuje się
        # podczas niszczenia obiektu
        Licznik.ile -= 1
        print(f"Niszczę obiekt nr {self.ktory}, pozostało jeszcze {Licznik.ile}.")

    @staticmethod # bez tego bedzie chcial chociaz self
    def policz():
        return Licznik.ile

class Test:
    def __init__(self):
        self.publiczne, self._chronione, self.__prywatne = 1, 2, 3




def main():
    a = Licznik()
    b = Licznik()
    c = Licznik()
    print(f"a to obiekt nr {a.ktory}")
    print(f"b to obiekt nr {b.ktory}")
    print(f"c to obiekt nr {c.ktory}")
    print(f"Liczba obiektow to: {Licznik.policz()}")
    print('fsadfsa', a.policz())

    a = None # python niszczy obiekty od razu po przepisaniu zmiennej do innego obiektu lub None
    b = None
    print(f"Liczba obiektow to: {Licznik.policz()}")

    d = Licznik()
    d.slowo = 'dupa'
    d.ile = 100
    print(d.ile)
    print(Licznik.ile)
    print(d.slowo)

    test = Test()
    print(test.publiczne)
    print(test._chronione)
    print(test._Test__prywatne)

if __name__ == "__main__":
    main()

# W języku Python jednak jest zgoła inaczej: nie jesteśmy w stanie w praktyce czegokolwiek ukryć przed osobą “z zewnątrz”.
# Jednak są pewne zasady nazewnictwa, które działają raczej na zasadzie porozumienia dżentelmeńskiego, niż będące
# prawdziwą barierą. I tak, gdy poprzedzimy nazwę jednym znakiem podkreślenia (_), oznajmiamy, że dany element nie
# jest uwzględniony w dokumentacji, może się zmienić, raczej nie należy z niego korzystać, a środowisko programistyczne
# nie będzie nam go podpowiadać. Przykładowo pole _imie, np. self._imie, czy self._metoda().
#
# Gdy użyjemy dwóch znaków podkreślenia (__), zachowanie jest trochę inne: dane pole czy metoda nie będzie widoczna
#  pod tą nazwą wcale, ale za to będzie można się do niego odwołać (dla nazwy __element) poprzez _nazwaklasy__element.