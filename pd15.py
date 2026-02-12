# # ----- KOD STARTOWY DO ZADAŃ -----

# def przygotuj_baze():
#     """Tworzy i wypełnia bazę danych na potrzeby zadań."""
# conn = sqlite3.connect('sklep.db') # Tworzy plik sklep.db
# cursor = conn.cursor()
# # Usunięcie tabel, jeśli istnieją, dla czystego startu
# cursor.execute("DROP TABLE IF EXISTS Zamowienia_Produkty")
# cursor.execute("DROP TABLE IF EXISTS Zamowienia")
# cursor.execute("DROP TABLE IF EXISTS Produkty")
# cursor.execute("DROP TABLE IF EXISTS Kategorie")
# cursor.execute("DROP TABLE IF EXISTS Klienci")
# # Tworzenie tabel
# cursor.execute('''
# CREATE TABLE Kategorie (
# id_kategorii INTEGER PRIMARY KEY,
# nazwa_kategorii TEXT UNIQUE NOT NULL
# )''')
# cursor.execute('''
# CREATE TABLE Produkty (
# id_produktu INTEGER PRIMARY KEY,
# nazwa_produktu TEXT NOT NULL,
# cena REAL NOT NULL,
# id_kategorii INTEGER,
# FOREIGN KEY (id_kategorii) REFERENCES Kategorie(id_kategorii)
# )''')
# cursor.execute('''
# CREATE TABLE Klienci (
# id_klienta INTEGER PRIMARY KEY,
# imie TEXT NOT NULL,
# email TEXT UNIQUE NOT NULL
# )''')
# cursor.execute('''
# CREATE TABLE Zamowienia (
# id_zamowienia INTEGER PRIMARY KEY,
# id_klienta INTEGER,
# data_zamowienia DATE,
# FOREIGN KEY (id_klienta) REFERENCES Klienci(id_klienta)
# )''')
# cursor.execute('''
# CREATE TABLE Zamowienia_Produkty (
# id_zamowienia INTEGER,
# id_produktu INTEGER,
# ilosc INTEGER NOT NULL,
# PRIMARY KEY (id_zamowienia, id_produktu),
# FOREIGN KEY (id_zamowienia) REFERENCES Zamowienia(id_zamowienia),
# FOREIGN KEY (id_produktu) REFERENCES Produkty(id_produktu)
# )''')
# # Wstawianie danych
# kategorie = [('Elektronika',), ('Książki',), ('Dom i ogród',)]
# klienci = [('Anna Nowak', 'anna.n@example.com'), ('Jan Kowalski',
# 'jan.k@example.com'), ('Zofia Wiśniewska', 'zofia.w@example.com')]
# produkty = [
# ('Laptop Pro', 5200.00, 1), ('Smartfon X', 2500.00, 1),
# ('Python dla każdego', 89.99, 2), ('Wzorce projektowe', 120.50, 2),
# ('Kosiarka elektryczna', 750.00, 3), ('Zestaw narzędzi', 300.00, 3),

# ('Słuchawki bezprzewodowe', 450.00, 1)
# ]
# zamowienia = [(1, '2023-10-01'), (2, '2023-10-02'), (1, '2023-10-05')]
# zamowienia_produkty = [(1, 1, 1), (1, 7, 1), (2, 3, 2), (3, 5, 1)]
# cursor.executemany("INSERT INTO Kategorie (nazwa_kategorii) VALUES (?)",
# kategorie)
# cursor.executemany("INSERT INTO Klienci (imie, email) VALUES (?,?)",
# klienci)
# cursor.executemany("INSERT INTO Produkty (nazwa_produktu, cena, id_kategorii) VALUES (?,?,?)", produkty)
# cursor.executemany("INSERT INTO Zamowienia (id_klienta, data_zamowienia) VALUES (?,?)", zamowienia)
# cursor.executemany("INSERT INTO Zamowienia_Produkty (id_zamowienia, id_produktu, ilosc) VALUES (?,?,?)", zamowienia_produkty)
# conn.commit()
# conn.close()
# print("Baza 'sklep.db' została przygotowana.")
# # Wywołaj funkcję, aby stworzyć bazę przed rozpoczęciem pracy
# przygotuj_baze()


#  Zadanie 1 – Liczba produktów
# Napisz skrypt, który połączy się z bazą sklep.db i policzy, ile jest wszystkich produktów w
# tabeli Produkty. Użyj funkcji COUNT().

import sqlite3
conn = sqlite3.connect("sklep.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM Produkty")
liczba_produktow = cursor.fetchone()[0]

print("Liczba produktów:", liczba_produktow)

conn.close()

# 2. ✏ Zadanie 2 – Najdroższy produkt
# Napisz skrypt, który znajdzie nazwę i cenę najdroższego produktu w sklepie. Użyj funkcji
# MAX().

import sqlite3
conn = sqlite3.connect("sklep.db")
cursor = conn.cursor()

cursor.execute("SELECT nazwa_produktu, cena FROM Produkty WHERE cena = (SELECT MAX(cena) FROM Produkty)")
produkt = cursor.fetchone()

print("Najdroższy produkt: ", produkt[0], ", cena: ", produkt[1])

conn.close()


# 3. ✏ Zadanie 3 – Suma wartości
# Oblicz i wyświetl łączną wartość wszystkich produktów z kategorii "Elektronika". Użyj funkcji
# SUM() oraz klauzuli WHERE z JOIN.

import sqlite3
conn = sqlite3.connect("sklep.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT SUM(p.cena) 
    FROM Produkty p
    JOIN Kategorie k ON p.id_kategorii = k.id_kategorii
    WHERE k.nazwa_kategorii = ?
""", ("Elektronika",))

suma_elektronika = cursor.fetchone()[0]

print("Suma produktów z kategorii Elektronika:", suma_elektronika)

conn.close()


# 4. ✏ Zadanie 4 – Średnia cena książki
# Napisz zapytanie, które obliczy średnią cenę produktów w kategorii "Książki". Użyj AVG().


import sqlite3
conn = sqlite3.connect("sklep.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT AVG(cena) 
    FROM Produkty p
    JOIN Kategorie k ON p.id_kategorii = k.id_kategorii
    WHERE nazwa_kategorii = ?
""", ("Książki",))

srednia_cena = cursor.fetchone()[0]

print(f"Średnia cena produktów w kategorii Książki to : {srednia_cena:.2f}")

conn.close()



# 5. ✏ Zadanie 5 – Lista klientów
# Napisz skrypt, który wyświetli imiona i adresy e-mail wszystkich klientów z tabeli Klienci.

import sqlite3
conn = sqlite3.connect("sklep.db")
cursor = conn.cursor()

cursor.execute("SELECT imie, email FROM Klienci")

lista_klientow = cursor.fetchall()

for k in lista_klientow:
    print(f"Klient: {k[0]}, email: {k[1]}")

conn.close()


# 6. 🧠 Zadanie 6 – Produkty droższe od średniej
# Napisz skrypt, który wyświetli nazwy i ceny wszystkich produktów, których cena jest wyższa
# niż średnia cena wszystkich produktów w sklepie. Wykorzystaj podzapytanie.
# (challenge)

import sqlite3
conn = sqlite3.connect("sklep.db")
cursor = conn.cursor()

cursor.execute("""
        SELECT nazwa_produktu, cena 
        FROM Produkty
        WHERE cena > (SELECT AVG(cena) FROM Produkty)
""")

lista_produktow = cursor.fetchall()

print("Produkty droższe od średniej ceny produktów:")
for p in lista_produktow:
    print(f"Produkt: {p[0]}, cena: {p[1]}")

conn.close()


# 7. 🧠 Zadanie 7 – Zamówienia Anny Nowak
# Napisz skrypt, który wyświetli nazwy wszystkich produktów zamówionych przez klienta o
# imieniu 'Anna Nowak'. Będziesz potrzebować połączyć dane z czterech tabel: Klienci,
# Zamowienia, Zamowienia_Produkty i Produkty.

import sqlite3
conn = sqlite3.connect("sklep.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT p.nazwa_produktu 
    FROM Klienci k
    JOIN Zamowienia z ON k.id_klienta = z.id_klienta
    JOIN Zamowienia_Produkty zp ON zp.id_zamowienia = z.id_zamowienia
    JOIN Produkty p ON zp.id_produktu = p.id_produktu
    WHERE imie = ?
""", ("Anna Nowak",))

lista_produktow = cursor.fetchall()

print("Produkty zamówione przez Annę Nowak:")
for p in lista_produktow:
    print(f"Produkt: {p[0]}")


conn.close()


# 8. 🧠 Zadanie 8 – Kategorie z liczbą produktów
# Napisz zapytanie, które wyświetli nazwę każdej kategorii oraz liczbę produktów należących
# do tej kategorii. Użyj JOIN, COUNT() oraz GROUP BY.

import sqlite3
conn = sqlite3.connect("sklep.db")
cursor = conn.cursor()

cursor.execute("""
        SELECT k.nazwa_kategorii,
        COUNT(p.id_produktu) 
        FROM Kategorie k
        LEFT JOIN Produkty p ON k.id_kategorii = p.id_kategorii
        GROUP BY k.nazwa_kategorii
""")

lista_wynikow = cursor.fetchall()

for l in lista_wynikow:
    print(f"Kategoria: {l[0]}. lość produktów: {l[1]}")

conn.close()



# 9. 🧠 Zadanie 9 – Funkcja do wyszukiwania produktów
# Napisz w Pythonie funkcję znajdz_produkty_w_kategorii(nazwa_kategorii), która przyjmuje
# jako argument nazwę kategorii i zwraca listę krotek (nazwa_produktu, cena) dla wszystkich
# produktów w tej kategorii.


import sqlite3

def znajdz_produkty_w_kategorii(nazwa_kategorii):
    conn = sqlite3.connect("sklep.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT p.nazwa_produktu, p.cena 
        FROM Kategorie k
        JOIN Produkty p ON k.id_kategorii = p.id_kategorii
        WHERE nazwa_kategorii = ?
    """, (nazwa_kategorii,))

    lista_produktow = cursor.fetchall()
    conn.close()
    return lista_produktow

lista_wynikow = znajdz_produkty_w_kategorii("Elektronika")
for l in lista_wynikow:
    print(f"Produkt: {l[0]}. Cena: {l[1]}")


# 10. 🧠 Zadanie 10 – Prosta symulacja ORM
# Stwórz klasę Produkt w Pythonie z atrybutami id_produktu, nazwa_produktu i cena.
# Następnie napisz funkcję pobierz_wszystkie_produkty(), która połączy się z bazą danych,
# pobierze wszystkie produkty i zwróci listę obiektów klasy Produkt. To ćwiczenie pokaże Ci,
# jak ORM automatyzuje mapowanie wierszy na obiekty.

class Produkt():
    def __init__(self, id_produktu, nazwa_produktu, cena):
        self.id_produktu = id_produktu
        self.nazwa_produktu = nazwa_produktu
        self.cena = cena

    def __repr__(self):
        return f"Produkt(id={self.id_produktu}, nazwa='{self.nazwa_produktu}', cena={self.cena})"

    def pobierz_wszystkie_produkty():
        conn = sqlite3.connect("sklep.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id_produktu, nazwa_produktu, cena FROM Produkty")
        rows = cursor.fetchall()
        conn.close()
        produkty = []
        for r in rows: 
            produkty.append(Produkt(r[0], r[1], r[2]))

        return produkty
    
print(Produkt.pobierz_wszystkie_produkty())