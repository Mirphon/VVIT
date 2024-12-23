def is_prime(number):
    d = set()
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            d.add(number//i)
            d.add(i)
    return print(len(d) <= 2)
is_prime(3)