def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes=[]
not_primes=[]
for i in numbers:
    if i < 2:
        continue
    elif is_prime(i) == True:
        primes.append(i)
    else:
        not_primes.append(i)

print("Primes:", primes)
print("Not Primes", not_primes)