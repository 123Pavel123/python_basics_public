import time

# Naprogramujte prevod ze sekund na roky, dny, hodiny, minuty a sekundy. Vysledek zkuste vypsat pomoci print()
# Napriklad 3661 sekund by se melo prevest na
# 0 years, 0 days, 1 hours, 1 minutes and 1 seconds
# pokud chcete, muzete si pohrat i s mnoznym/jednotnym cislem ve vypisu
# a pripadne prevodem hodnot na cela cisla


def time_convertor(input_seconds):
    """
    Function converts seconds to years, days, hours, minutes and seconds
    and prints the result.
    """

    pass  # TODO: implement the function


def main():
    """
    Function calculates current time in seconds and converts it to hours, minutes and seconds
    """
    current_time = time.time()  # Get current time since 1.1. 1970 in seconds
    time_convertor(current_time)


if __name__ == "__main__":
    main()
