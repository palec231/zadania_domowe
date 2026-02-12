# POZIOM 1
# 1. task1_hello.py
print("Witaj w Pythonie!")

# 2. task2_greeting.py
name = input("Jak masz na imię? ")
age = input("Ile masz lat? ")

print(f"Cześć, {name}! Wiem, że masz {age} lat.")


# 3. Terminal – komendy (tu nic nie piszemy w pliku)

# W terminalu VSCode wpisujesz kolejno:

# mkdir homework
# cd homework
# pwd        # Linux/Mac
# echo %cd%  # Windows
# cd ..

# POZIOM 2
# 4. task4_area.py
length = float(input("Podaj długość prostokąta: "))
width = float(input("Podaj szerokość prostokąta: "))

area = length * width
print("Pole prostokąta wynosi:", area)

#5. task5_exchange.py
rate = 4.0
pln = float(input("Podaj kwotę w złotówkach: "))

usd = pln / rate
print("To będzie", usd, "dolarów.")

# 6. task6_converter.py
number = int(input("Podaj liczbę całkowitą: "))

print("W systemie dwójkowym:", bin(number))
print("W systemie szesnastkowym:", hex(number))

# 7. task7_reverse.py
word = input("Podaj słowo: ")

print("Od tyłu:", word[::-1])

# POZIOM 3
# 8. task8_even_odd.py
n = int(input("Podaj liczbę całkowitą: "))

if n % 2 == 0:
    print("Liczba jest parzysta.")
else:
    print("Liczba jest nieparzysta.")

# 9. task9_calculator.py
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
op = input("Podaj znak operacji (+, -, *, /): ")

if op == "+":
    print("Wynik:", a + b)
elif op == "-":
    print("Wynik:", a - b)
elif op == "*":
    print("Wynik:", a * b)
elif op == "/":
    if b != 0:
        print("Wynik:", a / b)
    else:
        print("Błąd: nie można dzielić przez zero!")
else:
    print("Nieznana operacja.")

# 10. task10_access.py
height = int(input("Podaj swój wzrost w cm: "))
adult = input("Czy jesteś z opiekunem? (tak/nie): ")

has_adult = adult.lower() == "tak"

allowed = (height >= 120 and has_adult) or (height >= 160)

print(allowed)
