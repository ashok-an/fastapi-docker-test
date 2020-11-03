#!/usr/bin/env python

import argparse
import math

def is_prime(n):
	if n <= 1:
		return False

	for i in range(2, int(math.sqrt(n))+1):
		if n % i == 0:
			return False
	return True
# end

def gen_prime_numbers(n):
	output = []
	for i in range(1, n+1):
		if is_prime(i):
			output.append(i)
	# for
	return output
# end

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-n', '--number', required=True, help='number to be tested', type=int)
	args = parser.parse_args()

	output = gen_prime_numbers(args.number)
	print("n={}, count={}, primes={}".format(args.number, len(output), output[-5:]))
