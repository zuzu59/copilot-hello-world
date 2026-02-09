def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def first_n_primes(n):
    """Return the first n prime numbers."""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Get the first 30 prime numbers
first_30_primes = first_n_primes(30)
print(first_30_primes)
print("zuzu, c'est vraiment dingue cet agent Copilot ᕗ")
for _ in range(3):
    print("vive zuzu")