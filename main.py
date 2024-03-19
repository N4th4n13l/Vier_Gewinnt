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


while True:
    spalte = int(input('Dein Zug (Spalte 0-6): '))
    zeile = findeTiefsteZeile(spalte)
    print(spalte, zeile)
    spielfeld[(spalte, zeile)] = 'O'
    print(spielfeld3)

