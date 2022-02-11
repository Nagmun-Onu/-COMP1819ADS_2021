def my_max(my_list):
    my_max0 = int(my_list[0])
    for n in my_list:
        if int(n) > my_max0:
            my_max0 = int(n)
    return str(my_max0)


def top3_max_winner():
    my_list = []
    f = open("lucky 4.txt", "r")
    for line in f:
        s = str(line)
        s = s.split(" ")
        print(s)
    my_max1 = my_max(s)
    s.remove(my_max1)
    my_max2 = my_max(s)
    s.remove(my_max2)
    my_max3 = my_max(s)
    print(my_max1, my_max2, my_max3)


top3_max_winner()
