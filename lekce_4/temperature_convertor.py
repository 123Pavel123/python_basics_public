import sys

# Zadani:
# Vytvorte program, ktery prevadi teplotu z Fahrenheita na Celsius nebo naopak.
# Program bude prijimat dva argumenty: teplotu (cislo) a jednotku (C nebo F),
# ve ktere je teplota zadana.
#
# Priklad volani a vysledku:
# $ python temperature_convertor.py 32 F
# 32.0°F is 0.0°C
#
# $ python temperature_convertor.py 0 C
# 0.0°C is 32.0°F

def far_to_cel(far):
    return (far - 32) * 5 / 9


def cel_to_far(cel):
    return cel * 9 / 5 + 32


def main():
    # TODO: Zkontroluj pocet zadanych argumentu, pokud nejsou dva, vypis napovedu
    # pozor, prvni argument (index 0) je vzdy nazev skriptu

    # TODO: Ziskej hodnotu teploty a jednotku z argumentu

    # TODO: (VOLITELNE) zkontroluj, ze je teplota cislo, pokud ne, vypis chybu

    # TODO: pomoci vhodneho vetveni (C/F) zavolej spravnou prevodni funkci a vypis vysledek
    # ve tvaru "<zadana_teplota>< zadana_jednotka> is <prevedena_teplota><jednotka>"
    # v pripade spatne zadane jednotky vypis chybu
    pass


if __name__ == "__main__":
    main()