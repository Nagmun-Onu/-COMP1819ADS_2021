# This is a better version because complexity decreased from O(n^2) to O(n)
# version 0.1
# author: Nagmun Nahar Onu
# reference: vptuan

def my_minmax(sequence):
    # set the first element of the sequence as minimum and maximum value
    my_min = sequence[0]
    my_max = sequence[0]
    for value in sequence:
        if value > my_max:
            my_max = value
        elif value < my_min:
            my_min = value
#-----------------------------------------------------------------
            # unnecessary code of version 0
    # if len(sequence) > 1:
    # for i in range(len(sequence)):
    # for j in range(i + 1, len(sequence)):
    # if sequence[i] >= sequence[j]:
    #  if my_max < sequence[i]:
    #    my_max = sequence[i]
    #  if my_min > sequence[j]:
    #   my_min = sequence[j]
    # else:
    # if my_max < sequence[j]:
    #    my_max = sequence[j]
    # if my_min > sequence[i]:
    #  my_min = sequence[i]
 #-------------------------------------------------------------------------------
    
    result = (my_min, my_max)
    print(result)
