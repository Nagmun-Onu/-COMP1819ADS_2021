# @author: Nagmun Nahar Onu
# version 1
def minmax(sequence):
  # set the first element of the sequence as minimum and maximum value
    min = sequence[0]
    max = sequence[0]
    if len(sequence) > 1:
        for i in range(len(sequence)):
            for j in range(i+1,len(sequence)):
                if sequence[i] >= sequence [j]:
                    if max < sequence[i]:
                       max=sequence[i]
                    if min > sequence[j]:
                       min=sequence[j]
                else:
                    if max < sequence[j]:
                       max = sequence[j]
                    if min > sequence[i]:
                       min = sequence[i]
    result = (min,max)
    print(result)

# driver code
minmax([1,2,3,5])  # expected output (1, 5)
minmax([0,1,-2])   # expected output (-2, 1)
minmax([3])        # expected output (3, 3)
