def digit_sum(n):
    q = n
    sum = 0
    while q != 0:
        r = q % (10)
        q = int(q / 10)
        sum += r
        print(q, r, sum)
    return sum

digit_sum(54369)