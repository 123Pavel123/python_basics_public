def get_user_input():
    does_it_move = input("Does it move? yes/no:\n").strip().lower() == "yes"
    should_it_move = input("Should it move? yes/no\n").strip().lower() == "yes"
    return does_it_move, should_it_move


def engineering_flowchart(does_it_move, should_it_move):
    if not does_it_move:
        if should_it_move:
            return "Use WD-40."
        else:
            return "No problem."
    else:
        if should_it_move:
            return "No problem."
        else:
            return "Use duct tape."


def main():
    does_it_move, should_it_move = get_user_input()
    result = engineering_flowchart(does_it_move, should_it_move)
    print(result)


if __name__ == "__main__":
    print("Engineering Flowchart\n")
    main()