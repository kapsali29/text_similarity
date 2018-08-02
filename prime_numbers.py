def prime(number):
    oldnum = number
    factor = 1
    while number > 1:
        factor += 1
        if number % factor == 0:
            if 1 < factor < oldnum:
                return False # is not prime
            number //= factor
    return True # is prime!
