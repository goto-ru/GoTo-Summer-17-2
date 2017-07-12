# part1
def P(array):
    n = len(array)
    for i in range(n - 1):
        s = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                s = False
        if s:
            return array
    return array


# part2
def M(array):
    n = len(array)
    for i in range(n // 2):
        array[i] = array[n - 1 - i]
    return array


# part3
def A(array):
    return sum(array) // len(array)


# part4
def C(value, x):
    array = []
    for i in range(x):
        array.append(value - i)
    return array


# part5
def O(array):
    return list(reversed(array))


# part6
def T(array):
    n = len(array)
    for i in range(n):
        if i % 2 == 0:
            array[i] = array[i] * 2
        else:
            array[i] = array[i] // 2
    return array


# part7
def G(array):
    return sum(array)


# part8
print(G(O(T(O(C(A(M(P([1, 3, -8, 5, -3, 1]))), 4))))))


# answer - 5
