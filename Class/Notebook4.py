

sciezka_do_pliku = r"C:\przykladowy.txt"

# Tutaj mamy wszystko: open() służy otworzeniu połączenia do pliku. Jest to wspomniane wcześniej pozyskanie zasobu.
# Następnie następuje użycie metody read(). Odczytuje ona całą treść pliku za jednym zamachu. Po pojedynczym odczytaniu,
# drugie wywołanie zwróci nam napis pusty. Na końcu jest close(), zamknięcie połączenia do pliku.
# Jest to zwolnienie zasobu.
# 
# Aby upewnić się, że plik na pewno zostanie zamknięty, moglibyśmy napisać blok try-catch-finally:
try:
    f = open(sciezka_do_pliku)
    print(2/0)
    print(f.read())
except ZeroDivisionError as e:
    print(e)
finally:
    f.close()

# Jednak istnieje jeszcze drugi zapis. Używamy słowa kluczowego with. Wtedy definiujemy zasób, mówimy co chcemy
# zrobić, gdy go pozyskamy, a na końcu, po wykonaniu całej klauzuli, zasób jest zwolniony, niezależnie od tego, czy
# wydarzyła się sytuacja wyjątkowa czy też nie:

try:
    with open(sciezka_do_pliku) as f:
        print(f.read())
        print(2/0)
except ZeroDivisionError as e:
    print(e)

#Pole closed informuje nas czy plik został zamknięty. Jak widzimy został, choć ani razu nie wywołaliśmy close(),
#a po drodze był rzucony wyjątek.


# Teraz zobaczmy, jak użyć pakietu os, aby uzyskać podstawowe informacje o plikach:
# czy plik istnieje, jakie są pliki w folderze itp.
#
# Aby sprawdzić, czy plik istnieje, napiszemy:

import os
print(os.path.exists(sciezka_do_pliku))

# Na koniec omówmy os.path.join(). Jest to funkcja, która skleja kawałki ścieżki.
# Np. gdy mamy ścieżkę do folderu i chcemy dokleić na koniec nazwę pliku, który znajduje się w tym folderze:

print(os.path.join("folder1", "folder2", "plik.txt"))