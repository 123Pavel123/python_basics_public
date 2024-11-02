####################### Tabulky ###########################

# UKOL 1: Tisk Tabulky
# |    Name    |    Age     | Occupation |
# ----------------------------------------
# |    John    |    22.00   |  Student   |
# |    Jane    |    48.00   |   Baker    |

# Ukol 2: Binarni vek
# |    Name    |    Age     | Occupation | Binary age |
# -----------------------------------------------------
# |    John    |    22.00   |  Student   |   10110    |
# |    Jane    |    48.00   |   Baker    |   110000   |

# Pomoci definovanych promennych vytvorte tabulku, ktera vypada jako vystup vyse.
# Vytisknete tabulku na obrazovku a vystup si overte spustenim programu.

def main():
    """
    Function prints a table with names, ages and occupations of two people.
    """

    header1 = "Name"
    header2 = "Age"
    header3 = "Occupation"

    name1 = "John"
    age1 = 22
    occupation1 = "Student"

    name2 = "Jane"
    age2 = 48
    occupation2 = "Baker"

    print(f"| {header1:^10} | {header2:^10} | {header3:^10} |")
    print("-" * 40)
    # TODO: Ukol 1: Vytisknete radky tabulky
    # TODO: Ukol 2: Rozsirte tabulku o dalsi sloupec, ve kterem bude binarni zapis veku osoby


if __name__ == "__main__":
    main()
