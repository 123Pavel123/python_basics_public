

def main():
    name = 'Bob'
    number = 336366463
    error = "ERRRORRRRR"

    # str.format()
    print('Listen, {name}, your number is {number} and the code is {code}.'.format(number=number, name=name, code=error))
    # f-string ekvivalent
    print(f'Listen, {name}, your number is {number * 2} and the code is {error}.')

    # vytisteni promenne i s nazvem
    print(f"{number=}")

    # Pokrocilejsi formatovani
    # syntax: [flags][width][.precision]type

    # Flags: Modify the alignment or sign of the formatted value.
    #   <: Left-align the output (default is right-align) (znak pred ^ je pouzitej pro padding).
    #   ^: Center-align the output (znak pred ^ je pouzitej pro padding).
    #   +: Show a plus sign for positive numbers.
    #   (space): Print a space before positive numbers and a minus for negatives.
    #   0: Zero-pads numbers up to the width specified.
    #   ,: Adds commas as thousands separators (na konec za typ az)
    # Width: Defines the minimum width of the formatted output. If the value is shorter, it is padded.
    # Precision: (For floating-point numbers) Specifies how many digits to show after the decimal.
    # Type: Specifies the type of formatting for the value.
    #   s: String (default if no type is given).
    #   d: Integer (decimal).
    #   f: Fixed-point decimal for floats.
    #   e: Scientific notation (lowercase).
    #   E: Scientific notation (uppercase).
    #   b: Binary.
    #   x/X: Hexadecimal (lowercase/uppercase)
    #   %: Percentage (multiplies the number by 100 and adds a % sign).

    f"{'100.12334':s}"    # '100.12334'
    f"{100:x}"            # '64'
    f"{100:o}"            # '144'
    f"{100:e}"            # '1.000000e+02'
    f"{0.45:.1%}"           # '45.0%'

if __name__ == "__main__":
    main()
