# defaultni hodnota argumentu
def greet(name=None):
    if name is None:
        print("Ahoj, neznamy")
    else:
        print("Ahoj", name)


print("Example 1\n#########")
greet()
print("vs")
greet("Adam")
print("\n")


# test klice v dictu
print("Example 2\n#########")
people_age = {"Petr": 25, "Jana": 30, "Karel": 35}

the_chosen_one = "Petr"
chosen_ones_age = people_age.get(the_chosen_one, None)
if chosen_ones_age is not None:
    print(the_chosen_one, "ma", chosen_ones_age, "let.")


# navratova hodnota funkce v pripade chyby
def sqrt(x):
    if x < 0:
        return None
    else:
        return x ** 0.5


print("Example 3\n#########")
print("sqrt(4):", sqrt(4))
print("sqrt(-4): ", sqrt(-4))
