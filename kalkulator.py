def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def pomnoz(a, b):
    return a * b

def podziel(a, b):
    return a / b if b != 0 else 'Błąd: dzielenie przez zero'

def main():
    while True:
        try:
            a = float(input("Wpisz pierwszą liczbę: "))
            b = float(input("Wpisz drugą liczbę: "))
            operacja = input("Wybierz operację (dodaj, odejmij, pomnoz, podziel): ")

            if operacja == 'dodaj':
                print("Wynik:", dodaj(a, b))
            elif operacja == 'odejmij':
                print("Wynik:", odejmij(a, b))
            elif operacja == 'pomnoz':
                print("Wynik:", pomnoz(a, b))
            elif operacja == 'podziel':
                print("Wynik:", podziel(a, b))
            else:
                print("Nieznana operacja!")

        except ValueError:
            print("Błąd: Niepoprawne dane wejściowe.")
        except KeyboardInterrupt:
            print("\nWyjście z programu.")
            break

if __name__ == "__main__":
    main()

