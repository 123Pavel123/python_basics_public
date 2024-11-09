import sys
sys.path.append("lekce_4")
import math
from functions_star_demo import my_print
from temperature_convertor import far_to_cel as fc, cel_to_far as cf


def main():
    a = 3
    b = 6
    # my_print("honza", "votypka")
    print(math.sqrt(8))
    print(cf(34))

    print("dir2", dir())

print("dir1: ", dir())


if __name__ == "__main__":
    main()
