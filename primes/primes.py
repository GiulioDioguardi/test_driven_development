#!/usr/bin/python

def factortoprimes(number):
    if number is None:
        return []

    primes = []
    devisor = 2
    while number > 1:
        if number % devisor == 0:
            primes.append(devisor)
            number /= devisor
        else:
            devisor += 1
    return primes
