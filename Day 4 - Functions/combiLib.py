def fact(n):
    result = n
    for i in range(1, n):
        result *= i
    return result


def Cnk(n, k):
    return fact(n) // (fact(k) * fact(n - k))

if __name__ == '__main__':
    print("This is combinatorics library. Please import it.")
