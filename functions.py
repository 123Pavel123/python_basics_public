import math

def greet(name, surname="", age=""):
    greet_type = "Ahoj"  # "nazdar"
    output = greet_type + ", " + name + " " + surname + " " + age
    print("Funkce greet: ", output)
    return output, output

def f2():
    print("hello")

def main():
    name = "Honza"
    surname = "Votypka"
    age = 22 # None

    greet_honza = greet(name)
    print("Funkce main: ", greet_honza)


if __name__ == "__main__":
    print("Zacatek programu, spoustim main()")
    main()
