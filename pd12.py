# 1. ✏️ Zadanie 1 – Klasa danych Film
# Stwórz klasę danych (@dataclass) o nazwie Film, która będzie przechowywać tytuł (string),
# reżysera (string) i rok_produkcji (integer). Utwórz dwie instancje tej klasy i wyświetl je.


from dataclasses import dataclass

@dataclass
class Film:
    tytul: str
    rezyser: str
    rok_produkcji: int

film1 = Film("Matrix", "Larry i Andy Wachowski", 1999)
film2 = Film("Incepcja", "Christopher Nolan", 2010)

print(film1)
print(film2)


###############################################################################################


# 2. ✏️ Zadanie 2 – Walidator wieku
# Stwórz klasę Uzytkownik z atrybutem _wiek. Użyj dekoratora @property, aby stworzyć
# właściwość wiek. Getter powinien zwracać wiek, a setter powinien sprawdzać, czy podany
# wiek jest w zakresie od 0 do 120. Jeśli nie jest, powinien wyświetlić komunikat błędu i nie
# zmieniać wartości.

class Uzytkownik:
    def __init__(self, wiek):
        self._wiek = wiek

    @property
    def wiek(self):
        return self._wiek
    
    @wiek.setter
    def wiek(self, nowy_wiek):
        if (nowy_wiek < 0) or (nowy_wiek > 120):
            print("Nieprawidłowy wiek, wiek musi być w zakresie 0-120!")
        else:
            print("Ustawiono nowy wiek.")
            self._wiek = nowy_wiek
        
uzytkownik = Uzytkownik(20)
print(uzytkownik.wiek)
uzytkownik.wiek = 121
print(uzytkownik.wiek)


########################################################################################################

# 3. ✏️ Zadanie 3 – Konwerter Walut
# Stwórz klasę KalkulatorWalut. Dodaj w niej metodę statyczną (@staticmethod) o nazwie
# usd_na_pln, która przyjmuje kwotę w dolarach i zwraca ją przeliczoną na złotówki (przyjmij
# stały kurs, np. 1 USD = 4.0 PLN). Wywołaj tę metodę bez tworzenia obiektu klasy.
# Zadania-wyzwania (challenge)

class KalkulatorWalut:
    @staticmethod
    def usd_na_pln(kwota):
        return kwota * 4.0
    
print(KalkulatorWalut.usd_na_pln(100))

###############################################################################################


# 4. ✏️ Zadanie 4 – Bezpieczne dzielenie
# Napisz funkcję bezpieczne_dzielenie(a, b), która zwraca wynik dzielenia a / b. Użyj bloku
# try...except, aby obsłużyć błąd ZeroDivisionError. Jeśli wystąpi ten błąd, funkcja powinna
# zwrócić None i wyświetlić komunikat "Błąd: Dzielenie przez zero!".


def bezpiecznie_dzielenie(a, b):
    try:
        return (a / b)
    except ZeroDivisionError:
        print("Błąd: Dzielenie przez zero!")
        return None

print(bezpiecznie_dzielenie(10, 2))    
print(bezpiecznie_dzielenie(10, 0))

###############################################################################################


# 5. ✏️ Zadanie 5 – Odczyt pliku
# Napisz program, który próbuje otworzyć i odczytać plik o nazwie nieistniejacy.txt. Użyj bloku
# try...except, aby obsłużyć wyjątek FileNotFoundError i wyświetlić przyjazny komunikat
# użytkownikowi.

try:
    with open("nieistniejacy.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Błąd: plik nie istnieje!")

###############################################################################################


# 6. 🧠 Zadanie 6 – Własny wyjątek InvalidPasswordError
# Stwórz własny wyjątek InvalidPasswordError. Następnie napisz funkcję ustaw_haslo(haslo),
# która sprawdza, czy hasło ma co najmniej 8 znaków. Jeśli nie, funkcja powinna podnieść
# (raise) wyjątek InvalidPasswordError z odpowiednim komunikatem. Napisz kod, który
# testuje tę funkcję w bloku try...except.

class InvalidPasswordError(Exception):
    pass

def ustaw_haslo(haslo):
    if len(haslo) < 8:
        raise InvalidPasswordError("Nieprawidłowe hasło. Hasło musi posiadać co najmniej 8 znaków!")
    return "Hasło ustawione poprawnie."

try:
    print(ustaw_haslo("abc"))
except InvalidPasswordError as e:
    print(e)


###############################################################################################


# 7. 🧠 Zadanie 7 – Alternatywny konstruktor dla Daty
# Stwórz klasę Data z atrybutami dzien, miesiac, rok. Dodaj metodę klasy (@classmethod) o
# nazwie ze_stringa, która przyjmuje datę w formacie "DD-MM-RRRR" (np. "25-12-2023") i
# tworzy na jej podstawie obiekt klasy Data. Pamiętaj o konwersji typów na int.

class Data:
    def __init__(self, dzien, miesiac, rok):
        self.dzien = dzien
        self.miesiac = miesiac
        self.rok = rok
    
    @classmethod
    def ze_stringa(cls, data_str):
        dzien, miesiac, rok = map(int, data_str.split('-'))
        return cls(dzien, miesiac, rok)
    
    def __str__(self):
        return f"{self.dzien:02d}-{self.miesiac:02d}-{self.rok:02d}"

data = Data.ze_stringa("03-05-2025")
print(data)

###############################################################################################

# 8. 🧠 Zadanie 8 – Kalkulator z pełną obsługą błędów
# Stwórz prosty kalkulator, który prosi użytkownika o podanie dwóch liczb i operacji (+, -, *, /).
# Całość umieść w pętli while True , aby program działał do momentu przerwania.
# Użyj bloku try...except do obsługi:
# ValueError , jeśli użytkownik wpisze coś, co nie jest liczbą.
# ZeroDivisionError przy próbie dzielenia przez zero.
# Użyj bloku else , aby wyświetlić wynik tylko wtedy, gdy nie było błędu.
# Użyj bloku finally , aby na koniec każdej iteracji pętli wyświetlić komunikat "Koniec obliczeń.".


while True:
    try:
        a = input("Podaj pierwszą liczbę (wpisz 'koniec' aby wyjść): ")
        if a.lower() == "koniec":
            break
        a = float(a)
        b = float(input("Podaj drugą liczbę: "))
        operator = input("Podaj operator matematyczny (+, -, *, /): ")

        if operator == "+":
            wynik = a + b
        elif operator == "-":
            wynik = a - b
        elif operator == "*":
            wynik = a * b
        elif operator == "/":
            wynik = a / b
        else:
            print("Błąd: Nieznana operacja!")
            continue

    except ValueError:
        print("Błąd: podaj wartości liczbowe!")
    except ZeroDivisionError:
        print("Błąd: Nie można dzielić przez zero!")
    else:
        print(f"{a} {operator} {b} = {wynik}")
    finally:
        print("Koniec obliczeń.\n")


###############################################################################################


# 9. 🧠 Zadanie 9 – Klasa KontoBankowe z property i wyjątkami
# Stwórz klasę KontoBankowe za pomocą @dataclass, która ma atrybut _saldo (prywatne).
# Stwórz właściwość ( @property ) saldo , która tylko odczytuje wartość _saldo .
# Stwórz metodę wplac(kwota) , która dodaje kwotę do salda. Metoda powinna podnosić
# ValueError , jeśli kwota jest ujemna.
# Stwórz metodę wyplac(kwota) , która odejmuje kwotę od salda. Metoda powinna
# podnosić ValueError , jeśli kwota do wypłaty jest ujemna, oraz własny wyjątek
# BrakSrodkowError , jeśli saldo jest niewystarczające.
# Przetestuj działanie klasy, obsługując wszystkie możliwe wyjątki.


from dataclasses import dataclass

class BrakSrodkowError(Exception):
    """Wyjątek podnoszony przy próbie wypłacenia kwoty wyższej niż saldo konta"""
    pass

@dataclass
class KontoBankowe:
    _saldo: float

    @property
    def saldo(self):
        return self._saldo
    
    def wplac(self, kwota):
        if kwota < 0:
            raise ValueError("Kwota wpłaty nie może być ujemna.")
        self._saldo += kwota

    def wyplac(self, kwota):
        if kwota < 0:
            raise ValueError("Kwota wypłaty nie może być ujemna.")
        if kwota > self._saldo:
            raise BrakSrodkowError("Brak wystarczających środków na koncie.")
        self._saldo -= kwota

konto = KontoBankowe(1000)

try:
    konto.wplac(100)
    print(f"Saldo po wpłacie: {konto.saldo}") # Saldo po wpłacie: 1100

    konto.wyplac(100)
    print(f"Saldo po wypłacie: {konto.saldo}") # Saldo po wypłacie: 1000

   # konto.wplac(-100)    # 'Błąd wartości: Kwota wpłaty nie może być ujemna.'

    konto.wyplac(-100)   # 'Błąd wartości: Kwota wypłaty nie może być ujemna.'

    konto.wyplac(1500)   # 'Błąd: Brak wystarczających środków na koncie.'

except ValueError as e:
    print("Błąd wartości:", e)
except BrakSrodkowError as e:
    print("Błąd:", e)
else:
    print("Operacje zakończone sukcesem.")      

###############################################################################################


# 10. 🧠 Zadanie 10 – Metaklasa walidująca
# Stwórz metaklasę MetaWalidujMetody, która podczas tworzenia nowej klasy sprawdza, czy
# wszystkie jej metody (poza metodami "magicznymi", czyli zaczynającymi się od __) mają
# docstring. Jeśli któraś metoda go nie ma, metaklasa powinna podnieść TypeError z
# informacją, która metoda wymaga dokumentacji. Przetestuj ją, tworząc klasę z poprawnie i
# niepoprawnie udokumentowanymi metodami.

class MetaWalidujMetody(type):
    def __new__(cls, name, bases, namespace):
        for attr_name, attr_value in namespace.items():
            if attr_name.startswith("__"):
                continue

            if callable(attr_value):
                if not attr_value.__doc__:
                    raise TypeError(f"Metoda {attr_name} musi posiadać docstring.")

        return super().__new__(cls, name, bases, namespace)
    
class PoprawnaKlasa(metaclass=MetaWalidujMetody):
    def metoda1(self):
        """Docstring dla metody 1"""
        pass 

    def metoda2(self):
        """Docstring dla metody 2"""
        pass 

class NiepoprawnaKlasa(metaclass=MetaWalidujMetody):
    def metoda3(self):
        """Docstring dla metody 1"""
        pass 

    def metoda4(self):
        pass     