def potega(podstawa, do_potegi):
    if do_potegi == 0:
        return 1
    if do_potegi == 1:
        return podstawa
    if do_potegi%2 == 0:
        if do_potegi == 2:
            return podstawa*podstawa
        wynik = potega(podstawa, do_potegi / 2)
        return wynik*wynik
    wynik = potega(podstawa, (do_potegi-1) / 2)
    return wynik * wynik * podstawa

def potega2(podstawa, do_potegi, kumul=1):
    if do_potegi == 0:
        return kumul
    return potega2(podstawa, do_potegi-1, kumul*podstawa)

def potega3(podstawa, do_potegi):
    def _potega3(wynik, do_potegi):
        if do_potegi == 0:
            return wynik
        return _potega3(podstawa*wynik, do_potegi-1)
    return _potega3(podstawa, do_potegi-1)

def potega4(podstawa, do_potegi):
    if do_potegi == 0:
        return 1
    return podstawa * potega4(podstawa, do_potegi-1)

def czyPalindrom(word):
    if len(word) < 2:
        return True
    else:
        if word[0] == word[len(word)-1]:
            return czyPalindrom(word[1:len(word)-1])
        else:
            return False

def czyAnagram(base, check):
    word = dict()
    for i in base:
        word[i] = word.get(i, 0)+1
    for i in check:
        if i not in word.keys() or word[i] == 0:
            return False
        else:
            word[i] = word[i]-1
    return True

def moda(lst):
    numbers = dict()
    for number in lst:
        numbers[number] = numbers.get(number, 0)+1
    big = max(numbers.values())
    for k, v in numbers.items():
       if v == big:
           return k

def main():
   print(potega(2, 450000))
   print(potega2(2, 996))
   print(potega3(2, 996))
   print(potega4(2, 996))
   print(czyPalindrom("kajak"))
   print(czyAnagram("epies", "sieeep"))
   print(moda([78, 5, 4, 78, 34, 5, 65, 34, 78, 4, 5, 5]))

if __name__ == "__main__":
    main()