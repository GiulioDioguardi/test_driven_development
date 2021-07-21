#!/usr/bin/python

import argparse
import math

def factors_of(number):
    factors = []
    devisor = 2
    while number > math.sqrt(number):
        while number % devisor == 0:
            factors.append(devisor)
            number /= devisor
        devisor += 1
    return factors

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", type=int, help="the number to factor out")
    parser.add_argument("--search-primes", type=int, help="Get a list of primes, maximum of a given number")
    parsed_args = parser.parse_args()
    if parsed_args.number is None and parsed_args.search_primes is None:
        print("No number given to factor out, or no searched primes")
        parser.print_help()
        exit(1)
    return parsed_args

def search_primes(max):
    number = 1
    while max > 0:
        if len(factors_of(number)) == 1:
            print(number)
        number += 1
        max -= 1

if __name__ == "__main__":
    args = get_parser()
    if args.number:
        print(factors_of(parser.number))
    if args.search_primes:
        search_primes(parser.search_primes)
