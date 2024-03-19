# https://www.youtube.com/watch?v=9F1FKpwbnl0&t=369s

spielfeld = {}  # Key = (spalte, zeile), value, ='O' oder 'X'

SPALTEN = 7
ZEILEN = 6
ZELLEN = SPALTEN * ZEILEN


def findeTiefsteZeile(spalte):
    global zeile
    for zeile in reversed(range(ZEILEN)):
        if (spalte, zeile) not in spielfeld:
            return zeile


def column_valid(spalte):
    if (spalte, 0) in spielfeld:
        return False
    if 0 <= spalte < 7:
        return True


def print_spielfeld():
    for i in range(ZELLEN):
        if i % SPALTEN == 0:
            print()
        pos = (i % SPALTEN, i // SPALTEN)  # WICHTIG Koordinaten auslesen
        if pos in spielfeld:
            print(spielfeld[pos], end=' ')
        else:
            print('.', end=' ')
    print()


while True:
    while True:
        spalte = int(input('Dein Zug (Spalte 0-6): '))
        if column_valid(spalte):
            break
    zeile = findeTiefsteZeile(spalte)
    spielfeld[(spalte, zeile)] = 'O'
    print_spielfeld()
