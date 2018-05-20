def factorial(N):
    if N <= 0:
        return 1
    else:
        acc = 1
        return fact_large(N,2,acc)


def fact_large(N,m,acc):
    if N <= m:
        return N*acc
    else:
        return fact_large(N,m+1,m*acc)

def loop_fct(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1,n+1):
            result *= i
        return result


print(factorial(500))

print(loop_fct(500))

#print(norm_fct(5000))
