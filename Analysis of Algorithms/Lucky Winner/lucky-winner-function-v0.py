# replace with file-name
f = open("lucky.txt", "r")
flag = 0
for my_id in f:
  # you can replace "0001167255" with any id
    if "001167255" in my_id:
        print(my_id)
        print("yes")
        flag = 1
if flag == 0:
    print("No")
