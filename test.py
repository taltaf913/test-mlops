#!/usr/bin/env python3
"""
Sample Python program: greeting and a small utility (factorial).

Usage examples:
  python test.py            # prints a greeting
  python test.py -n Alice   # greet Alice
  python test.py -f 5       # compute factorial(5)
  python test.py -n Bob -f 6
"""

import argparse
import sys


def greet(name: str) -> str:
	"""Return a greeting for name."""
	return f"Hello, {name}!"


def factorial(n: int) -> int:
	"""Compute factorial iteratively. Raises ValueError for negative n."""
	if n < 0:
		raise ValueError("n must be non-negative")
	result = 1
	for i in range(2, n + 1):
		result *= i
	return result


def parse_args(argv=None):
	p = argparse.ArgumentParser(description="Sample program: greeting + factorial")
	p.add_argument("-n", "--name", help="Name to greet", default="World")
	p.add_argument("-f", "--factorial", type=int, help="Compute factorial of N")
	return p.parse_args(argv)


def main(argv=None) -> int:
	args = parse_args(argv)
	print(greet(args.name))
	if args.factorial is not None:
		try:
			print(f"factorial({args.factorial}) = {factorial(args.factorial)}")
		except ValueError as e:
			print("Error:", e, file=sys.stderr)
			return 2
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
