def main():
    question_1_1 = input("Funguje to? ano/ne:\n").strip().lower()
    if question_1_1 == "ano":
        print("Nejeb do toho!!!")
        print("Nemáš problém.")
    else:
        question_2_1 = input("Jebal jsi do toho? ano/ne:\n").strip().lower()
        if question_2_1 == "ne":
            question_2_2 = input("Zjebe tě někdo? ano/ne:\n").strip().lower()
            if question_2_2 == "ano":
                print("SI V PI**!!!.")
                question_2_3= input("Můžeš to na někoho hodit? ano/ne:\n").strip().lower()
                if question_2_3 == "ano":
                    print("Nemáš problém.")
                else:
                    print("SI V PI**!!!")
            else:
                print("Ser na to!")
                print("Nemáš problém.")
        else:
            print("SI K***T!!!")
            question_3_1 = input("Ví o tom někdo? ano/ne:\n").strip().lower()
            if question_3_1 == "ne":
                print("Schovej to!")
                print("Nemáš problém.")
            else:
                print("SI V PI**!!!")
                question_3_2 = input("Můžeš to na někoho hodit? ano/ne:\n").strip().lower()
                if question_3_2 == "ano":
                    print("Nemáš problém.")
                else:
                    print("SI V PI**!!!")


if __name__ == "__main__":
    print("Řešení problému po česku.\n")
    main()