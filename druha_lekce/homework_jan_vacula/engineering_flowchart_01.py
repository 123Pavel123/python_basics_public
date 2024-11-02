def main():
    does_it_move = input("Does it move? yes/no\n").strip().lower()
    if does_it_move == "no":
        should_it_move_no = input("Should it move? yes/no\n").strip().lower()
        if should_it_move_no == "no":
            print("No problem.")
        else:
            print("Use WD-40.")
    else:
        should_it_move_yes = input("Should it move? yes/no\n").strip().lower()
        if should_it_move_yes == "yes":
            print("No problem.")
        else:
            print("Use duct tape.")


if __name__ == "__main__":
    print("Engineering Flowchart\n")
    main()