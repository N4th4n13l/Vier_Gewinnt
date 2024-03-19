# https://www.youtube.com/watch?v=9F1FKpwbnl0&t=369s

spielfeld = {}  # Key = (spalte, zeile), value, ='O' oder 'X'

SPALTEN = 7
ZEILEN = 6
ZELLEN = SPALTEN * ZEILEN


# Funktionen zur Prüfung, ob Spielfeld noch leer ist!


def findeTiefsteZeile(spalte):  # von unten --> oben auslesen, ob Feld besetzt
    for zeile in reversed(range(ZEILEN)):
        if (spalte, zeile) not in spielfeld:  # alles was belegt ist, ist in Spielfeld
            return zeile


def column_valid(spalte):
    if (spalte, 0) in spielfeld:
        return False
    if 0 <= spalte < 7:
        return True


# Ausgabe des Spielfeldes in die Konsole


def print_spielfeld():
    for i in range(ZELLEN):
        if i % SPALTEN == 0:
            print()
        pos = (i % SPALTEN, i // SPALTEN)  # WICHTIG Koordinaten auslesen $ siehe am Schluss
        if pos in spielfeld:
            print(spielfeld[pos], end=' ')
        else:
            print('.', end=' ')
    print()


spieler = True  # Spielerwechsel
# Spielschleife
while True:
    while True:
        spalte = int(input('Dein Zug (Spalte 0-6): '))  # ab hier Prüfung, ob frei
        if column_valid(spalte):
            break
    zeile = findeTiefsteZeile(spalte)  # bis hier
    spielfeld[(spalte, zeile)] = 'O' if spieler else 'X'  # Spielerwechsel

    print_spielfeld()
    spieler = not spieler  # Spielerwechsel
