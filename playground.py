# 1. lekce dump
PI = 3.14
print("Hello world!")


def a_plus_a(a: int):
    """
    Tato funkce pocita druhou mocninu.

    Parameters
    ----------
    a: int
        a je vstup funkce

    Returns
    -------
    Druha mocnina a
    """
    print(PI)
    # assert isinstance(a, int), "Wrong type of a!!!!!!"
    result = a+a  # computes result
    print(result)
    return result


a_plus_a("string")

a_plus_a(2)
a_plus_a([3, 4, 5])
moje_kocka = 0
moje_kocka = moje_kocka


# 2. lekce dump