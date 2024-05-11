def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

x1 = int(input())
n1 = int(input())
total = power(x1, n1)
print(total)



