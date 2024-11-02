# 1.zadani
def sell_or_repair():
    print("************\nIt looks like it´s broken\n")
    
    answer = input("Does it move?\n")
    if answer == "yes":
        answer2 = input("Shall it move?\n")
        if answer2 == "yes":
            print("Then it´s OK and let it bee.\nBYE!")
        elif answer2 == "no":
            print("Then it´s bad but use the tape, that can fix it.\nBYE!")

    else:
        answer2 = input("Shall it move?\n")
        if answer2 == "yes":
            print("Then  use WD40 and oil it as you can!\n")
        elif answer2 == "no":
            print("Then it´s OK, no problem.\nBYE!")

sell_or_repair()

# 2.zadani
def lifeproblem():
    answer = input("Do you have problem in your life? Answer ´yes´, or ´no´.\n")
    if answer == "yes":
            answer2 = input("Can you do anything about it? Answer ´yes´, or ´no´\n")
            if answer2 == "yes":
                print("Then don´t worry!\n")
            else:
                print("Then why  worry :)\n")
    else:
        print("You should get a wife, trust me")
