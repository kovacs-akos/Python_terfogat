import math


def terfogat_szamitas():
    print('========================')
    print('Térfogat számítás:')
    adott_input = input('Írj egy "K"-t a kockáért, "T"-t a téglatestért. Írj egy "0"-t, ha ki szeretnél lépni a programból: ').capitalize()
    terfogat: int = 0
    if adott_input == "K":
        kocka_el = int(input('Add meg a kocka élét cm-ben: '))
        terfogat = kocka_el ** 3
        print(f'A kocka térfogata: {terfogat}cm3')
    elif adott_input == "T":
        elso_el = int(input('Add meg a téglatest első élét cm-ben: '))
        masodik_el = int(input('Add meg a téglatest élét második cm-ben: '))
        harmadik_el = int(input('Add meg a téglatest élét harmadik cm-ben: '))
        terfogat = elso_el * masodik_el * harmadik_el
        print(f'A téglatest térfogata: {terfogat}cm3')
    elif adott_input == "0":
        print('Program leállítása...')
        quit()
    else:
        print('Az általad megadott opció nem létezik!')
    print('========================')


def main() -> None:
    terfogat_szamitas()
    while True:
        valasztas = int(input('A program újboli lefuttatásához írj egy "1"-est: '))
        if valasztas == 1:
            terfogat_szamitas()
        else:
            print("Program leállítása...")
            quit()


if __name__ == "__main__":
    main()
