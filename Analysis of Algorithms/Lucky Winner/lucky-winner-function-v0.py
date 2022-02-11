def lucky_winner(check_id):
    f = open("lucky.txt", "r")
    for my_id in f:
        if check_id in my_id:
            print(my_id)
            print("yes")
            return
    print("No")
    return


lucky_winner("001167255")
