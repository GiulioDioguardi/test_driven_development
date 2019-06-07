#!/usr/bin/python

import argparse
import sys

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

def main():
    parser = argparse.ArgumentParser(
        description="Calculate the prime factors of an integer")
    parser.add_argument('integer', type=int,
        help="The integer number to be prime factored")
    args = parser.parse_args()

    print factortoprimes(args.integer)
    return 0

if __name__ == "__main__":
    sys.exit(main())
