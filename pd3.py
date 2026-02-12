# 1. Tworzenie i typowanie: Utwórz zmienne przechowujące Twoje imię (str), wiek (int), średnią
# ocen (float) i status studenta (bool). Wyświetl na ekranie wartość i typ każdej zmiennej.

name = "Krzysiek"
age = 41
grade_avg = 4.56
status = True

print(f"Imię: {name}, typ {type(name)}")
print(f"Wiek: {age}, typ {type(age)}")
print(f"Średnia ocen: {grade_avg}, typ {type(grade_avg)}")
print(f"Status studenta: {status}, typ {type(status)}")


#---------------------------------------------------------------------------------
# 2. Kalkulator BMI: Napisz program, który zapyta użytkownika o jego wagę w kilogramach i wzrost w metrach. 
# Oblicz i wyświetl wskaźnik masy ciała (BMI) według wzoru: BMI = waga / (wzrost * wzrost).

weight = float(input("Podaj wagę w kg:\n"))
height = float(input("Podaj wzrost w m (np. 1.80):\n"))

print(f"Twoje BMI to {round(weight / (height * height), 1)}\n") # {(weight / (height * height)):.2f}")

#---------------------------------------------------------------------------------
# 3. Analiza stringa: Utwórz zmienną z łańcuchem znaków " Python jest super! " .
# Wykonaj następujące działania i wyświetl wynik każdego kroku:
# Usuń zbędne białe znaki na początku i na końcu.
# Przekształć cały ciąg na małe litery.
# Zamień słowo "super" na "świetny".
# Wyświetl na ekranie znak pod indeksem 4 .

test_str = " Python jest super! "

test_str = test_str.strip()

print(test_str)
print(test_str.lower())
print(test_str.replace("super", "świetny"))
print(f"Znak na pozycji 4 to: {test_str[4]}")


#---------------------------------------------------------------------------------
# 4. Praca z f-stringami: Poproś użytkownika o jego imię i rok urodzenia. Oblicz jego przybliżony wiek 
# i wyświetl komunikat w formacie: "Cześć, [Imię]! W 2025 roku będziesz mieć około [Wiek] lat."

name = input("Podaj swoje imię:\n")
birth_year = int(input("Podaj rok urodzenia:\n"))

import datetime
date = datetime.date.today()
age = date.year - birth_year

print(f"Cześć, {name}! W 2025 roku będziesz mieć około {age} lat.")


#---------------------------------------------------------------------------------
# 5. Popraw kod zgodnie z PEP 8: Poniżej znajduje się fragment kodu. Przepisz go tak, aby
# był zgodny z zasadami PEP 8.
# Kod źródłowy
# NazwaUzytkownika="JanKowalski"
# wiekUzytkownika=25
# if wiekUzytkownika>=18:print(NazwaUzytkownika+' jest dorosły.')

nazwa_uzytkownika = "JanKowalski"
wiek_uzytkownika = 25

if wiek_uzytkownika >= 18:
    print(nazwa_uzytkownika + ' jest dorosły.')


#---------------------------------------------------------------------------------
# 6. Operacje na liście:
# Utwórz listę owoce = ["jabłko", "banan", "wiśnia"] .
# Dodaj na koniec listy "pomarańczę".
# Zmień drugi element ("banan") na "jagodę".
# Wyświetl końcową listę na ekran.

owoce = ["jabłko", "banan", "wiśnia"]

owoce.append ("pomarańcza")
owoce[1] = "jagoda"
print(owoce)


#---------------------------------------------------------------------------------
# 7. Niemutowalność krotki:
# Utwórz krotkę punkt = (10, 20, 30) .
# Spróbuj zmienić pierwszy element krotki nа 15 .
# Wyjaśnij w komentarzu do kodu, dlaczego wystąpił błąd.

punkt = (10, 20, 30)
punkt [0] = 15

# # krotka jest niemutowalna, nie można zmieniać jej wartości


#---------------------------------------------------------------------------------
# 8. Rzutowanie typów: Utwórz zmienną liczba_str = "5.8" . Przekonwertuj ją najpierw na
# float , a następnie na int i wyświetl wyniki obu konwersji. Co zauważyłeś podczas
# konwersji float na int ?

liczba_str = "5.8"

liczba_float = float(liczba_str)
liczba_int = int(liczba_float)

print(f"Liczba float: {liczba_float}")
print(f"Liczba int: {liczba_int}")

# przy konwersji float na int nie zaokrągla liczby tylko obcina część dziesiętną

#---------------------------------------------------------------------------------
# 9. Bramki logiczne: Napisz program, który poprosi o dwie wartości logiczne ( True lub False ). Niech użytkownik wprowadza 1 dla True i 0 dla False . 
# Program powinien wyświetlić wyniki operacji AND oraz OR dla tych dwóch wartości.

while True:
    value_1 = int(input("Podaj pierwszą wartość (0 - False / 1 - True):\n"))
    value_2 = int(input("Podaj drugą wartość (0 - False / 1 - True):\n"))

    if (value_1 == 0 or value_1 == 1) and (value_2 == 0 or value_2 == 1):
        bool_1 = bool(value_1)
        bool_2 = bool(value_2)
        print(f"{bool_1} AND {bool_2} = {(bool_1 and bool_2)}")
        print(f"{bool_1} OR {bool_2} = {(bool_1 or bool_2)}")
        break
    else:
        print("Podano nieprawidłowe wartości! Spróbuj ponownie!\n")


# ---------------------------------------------------------------------------------
# 10. Mini-projekt "Formater danych": Napisz program, który poprosi użytkownika o jego imię i nazwisko w jednej linii (np. " jan kowalski "). 
# Program powinien:
# Oczyścić zbędne białe znaki.
# Sprawić, aby każde słowo zaczynało się wielką literą (metoda .title() ).
# Wyświetlić sformatowane dane oraz ich długość.

# # wersja 1

name = input("Podaj imię i nazwisko:\n")

name_strip = name.strip()
name_title = name_strip.title()

print(f"{name_title}")
print(f"Długość tekstu to {len(name_strip)}")


# # wersja 2 (krótsza)

name = input("Podaj imię i nazwisko:\n")

print(f"{name.strip().title()}")
print(f"Długość tekstu to {len(name.strip())}")