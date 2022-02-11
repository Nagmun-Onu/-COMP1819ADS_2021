# @author: Nagmun Nahar Onu
# version 0
def my_minmax(sequence):
    # set the first element of the sequence as minimum and maximum value
    my_min = sequence[0]
    my_max = sequence[0]
    if len(sequence) > 1:
        for i in range(len(sequence)):
            for j in range(i + 1, len(sequence)):
                if sequence[i] >= sequence[j]:
                    if my_max < sequence[i]:
                        my_max = sequence[i]
                    if my_min > sequence[j]:
                        my_min = sequence[j]
                else:
                    if my_max < sequence[j]:
                        my_max = sequence[j]
                    if my_min > sequence[i]:
                        my_min = sequence[i]
    result = (my_min, my_max)
    print(result)

# driver code
my_minmax([1,2,3,5])  # expected output (1, 5)
my_minmax([0,1,-2])   # expected output (-2, 1)
my_minmax([3])        # expected output (3, 3)
