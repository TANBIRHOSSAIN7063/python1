
#using function calculate twin prime number between 1 to 100 in python

def find_prime_pairs(n):

    sieve = [True] * n

    if n > 0:
        sieve[0] = False
        if n > 1:
            sieve[1] = False

    for number in range(2, int(n ** 0.5) + 1):
        if sieve[number]:
            for index in range(number * number, n, number):
                sieve[index] = False

    return [(a, b) for b, a in enumerate(range(0, n - 2), start=2) if sieve[a] and sieve[b]]

print(*find_prime_pairs(100), sep='\n')