def buble(array):
    for i in range(len(array)):
        n = len(array)
        s = True
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j + 1], array[j]
    print(array)

buble([5,4,2,3,10,1])