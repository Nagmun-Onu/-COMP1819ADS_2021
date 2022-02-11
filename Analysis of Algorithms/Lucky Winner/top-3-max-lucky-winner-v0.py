def my_max(my_list):
    my_max0 = my_list[0]
    for n in my_list:
        if n > my_max0:
            my_max0 = n
    return my_max0


def top3_max_winner():
    s = []
    f = open("lucky.txt", "r")
    for line in f:
        s.append(line)
    my_max1 = my_max(s)
    s.remove(my_max1)
    my_max2 = my_max(s)
    s.remove(my_max2)
    my_max3 = my_max(s)
    print(my_max1, my_max2, my_max3)


top3_max_winner()
