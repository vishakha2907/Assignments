def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n

print("6 is perfect number  : % d" % (perfect_number(6)))
