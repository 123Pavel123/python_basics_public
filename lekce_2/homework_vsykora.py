# vývojový diagram semafor pro chodce

def semafor():
    odpoved = int(input("Na semaforu svítí, zadej číslo 1 pro červenou, 2 pro zelenou ?: \n"))
    if odpoved == 1 :
        print(f"Svítí červená, stůj !")
    elif odpoved == 2:
        print(f"Svítí zelená, stůj !")
    else:
        print(f"Nezadal jsi povolené hodnoty")
semafor()

