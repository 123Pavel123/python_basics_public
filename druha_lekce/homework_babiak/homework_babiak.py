from random import randint
from PIL import Image

################## Vetveni ##################
# Naprogramujte funkci, ktera nacte od uzivatele dve promenne typu bool
# does_it_move a should_it_move. Na zaklade flowchartu pak doporucte, jak
# se ma uzivatel zachovat.
# flowchart: https://www.reddit.com/r/funny/comments/2lrwoo/engineering_flowchart/

def does_it_move():
    print("Does It Move? [yes/no]")
    a = input()
    if a == "yes":
        print("should it? [yes/no]")
        answer = input()
        if answer == "yes":
            print("No problem")
        elif answer == "no":
            print("Use duckttape!")
    if a == "no":
        print("Should it? [yes/no]")
        answer2 = input()
        if answer2 == "yes":
            print("Use WD40")
        elif answer2 == "no":
            print("No problem!")

# does_it_move()
# TODO



################# Domaci ukol #################
# Najdi si flowchart, ktery by slo prevest do podoby kodu.
# Naprogramuj funkci, ktera bude simulovat rozhodovani podle tohoto flowchartu
# vstupy budou zadavany uzivatelem. Nahraj funkci na github do sdileneho souboru
# a do dokumentace se podepis, at se v tom vyzname.
image = Image.open(r"flowchart_babiak.jpg")
image.show()

def homework_stud():
    nums = int(input("Choose your range of numbers: " ))
    a=randint(0,nums)
    b=randint(0,nums)
    c=randint(0,nums)
    print(f"Chosen numbers are : 'a'= {a}, 'b'={b}, c={c}")
    print("is 'a' bigger than 'b'?")
    if a > b:
        print("'a' is bigger than 'b'")
        print("is 'a' bigger than 'c'?")
        if a>c:
            print(f"'a' bigger than 'c'\nthis is the biggest number 'a'= {a}")
        else:
            print(f"'c' bigger than 'a'\n{c} is the biggest number")
    else:
        print("b is bigger than a")
        print("is 'b' bigger than 'c'?")
        if b>c:
            print(f"'b' bigger than 'c'\nthis is the biggest number 'b'= {b}")
        else:
            print(f"'c' bigger than 'b'\n{c} is the biggest number")
homework_stud()
