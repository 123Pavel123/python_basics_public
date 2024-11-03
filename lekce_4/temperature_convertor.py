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
    # if len(sys.argv) != 3:
    #     print("Spatny pocet argumentu, zadej: <telpota: int> <jednotka: C/F>")
    #     exit()
    #
    # TODO: Ziskej hodnotu teploty a jednotku z argumentu
    temperature = sys.argv[1]
    unit = sys.argv[2]

    # TODO: (VOLITELNE) zkontroluj, ze je teplota cislo, pokud ne, vypis chybu
    # tezky, priste

    temperature = float(temperature)

    # TODO: pomoci vhodneho vetveni (C/F) zavolej spravnou prevodni funkci a vypis vysledek
    # ve tvaru "<zadana_teplota>< zadana_jednotka> is <prevedena_teplota><jednotka>"
    # v pripade spatne zadane jednotky vypis chybu
    if unit == "C":
        converted = cel_to_far(temperature)
        new_unit = "F"
    elif unit == "F":
        converted = far_to_cel(temperature)
        new_unit = "C"
    else:
        print(f"Unit (second argument) has to be C or F! You gave us {unit}")
        exit()

    print(f"{temperature:.2f}°{unit} is {converted:.2f}°{new_unit}")

    # inp = sys.argv
    # if len(inp) != 3:
    #     print("Bad Input please try again!")
    #     return
    #
    # try:
    #     temperature = int(inp[1])
    # except ValueError:
    #     print("Bad input for temperature!")
    #
    # if inp[2] == "C":
    #     return print(f"{cel_to_far(temperature)} Farenheit!")
    # elif inp[2] == "F":
    #     return print(f"{far_to_cel(temperature)} Celsius!")
    # else:
    #     print("Wrong unit, arg2 has to be C/F")


if __name__ == "__main__":
    main()
