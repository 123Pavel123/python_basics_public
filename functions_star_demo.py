from math import sqrt

def greet(name, surname="", age=""):
    greet_type = "Ahoj"  # "nazdar"
    output = greet_type + ", " + name + " " + surname + " " + age
    print("Funkce greet: ", output)
    return output, output

def f(one, two, three, *args, ein=1, zwei=2, drei=3, **kwargs):
    print(one, two, three)
    print(args)
    print(ein, zwei, drei)
    print(kwargs)


def check_small_letter(character):
    ord_char = ord(character)
    if ord_char >= 97 and ord_char <= 122:
        return True
    else:
        return False

def my_print(datum, pozdrav, *nacionale, jmeno="unknown", prijmeni="unknown", **zakladni_nacionale):
    print(datum, pozdrav)
    print("########")
    for n in nacionale:
        print(n)
    print("########")
    print(jmeno)
    print(prijmeni)
    print("########")
    for key, value in zakladni_nacionale.items():
        print(key, ":", value)
    print("########")
    # print("Ahoj", " ".join(nacionale))

    # for arg in args:
    #     print(arg*2)


def main():
    # f(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ein=11, zwei=12, drei=13, vier=14, funf=15)
    # print(sorted(locals()))

    my_print("10.10.2024", "Nazdar", "Bezrucova 15", "Plzen", prijmeni="Votypka", vek="23", zamestnani="obrabec")


print(dir())

if __name__ == "__main__":
    print("Zacatek programu, spoustim main()")
    main()
