def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    # Check divisibility from 2 to square root of the number
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False
    return True

def primes_up_to(max: int = 100) -> list[int]:
    # Find and print prime numbers between 1 and max
    primes = []
    for num in range(2, max+1): # Loop through numbers from 2 to max
        if is_prime(num):
            primes.append(num)
    return primes

def result(max: int = 100):
    print(f"Prime numbers between 1 and {max} are:\n{primes_up_to(max)}")
