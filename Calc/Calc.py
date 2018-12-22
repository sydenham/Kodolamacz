def main():
    another_operation = True;
    while another_operation:
        print("Podaj w oddzielnych wierszach liczbę, operację matematyczną: +,-,*,/,%, a następnie kolejną liczbę:")
        x = (float(input()))
        operand = input()
        y = (float(input()))
        if operand is "+":
            print("Twój wynik to:", x + y)
        elif operand == "-":
            print("Twój wynik to:", x - y)
        elif operand == "*":
            print("Twój wynik to:", x * y)
        elif operand == "/":
            print("Twój wynik to:", x / y)
        elif operand == "%":
            print("Twój wynik to:", x % y)
        else:
            print("Nierozpoznano polecenia")
        print("Chcesz wykonać kolejne działanie? Wpisz literę t lub n.")
        if input() is "n":
            another_operation = False;

if __name__ == "__main__":
    main()
