#!/usr/bin/env python3
"""
Implements is_prime(n) and a test harness that runs a set of justified test cases.
Run the script to verify all test cases pass.
"""
import math
from typing import Any, List, Tuple

def is_prime(n: int) -> bool:
	"""Return True if n is a prime number, else False.

	Algorithm:
	- Handle n <= 1 (not prime), 2 and 3 (prime).
	- Eliminate even numbers and multiples of 3.
	- Use 6k ± 1 wheel optimization: test divisors up to sqrt(n).
	"""
	if not isinstance(n, int):
		return False
	if n <= 1:
		return False
	if n <= 3:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	# check possible divisors of form 6k - 1 and 6k + 1
	limit = int(math.isqrt(n))
	i = 5
	while i <= limit:
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i += 6
	return True

def generate_test_cases() -> List[Tuple[Any, bool, str]]:
	"""Generate and justify test cases for is_prime.

	Returns list of tuples: (input, expected_result, justification)
	"""
	tests = [
		( -10, False, "Negative numbers are not prime." ),
		( 0, False, "Zero is not prime." ),
		( 1, False, "One is not prime by definition." ),
		( 2, True, "Smallest prime (even prime)." ),
		( 3, True, "Small odd prime." ),
		( 4, False, "Small composite (even)." ),
		( 9, False, "Odd composite (small square)." ),
		( 17, True, "Small prime." ),
		( 25, False, "Square of prime (5*5)." ),
		( 97, True, "Two-digit prime, near sqrt checks." ),
		( 100, False, "Even composite (multiple of 2,5)." ),
		( 7919, True, "Larger prime (prime near 8000)." ),
		( 7920, False, "Large composite adjacent to a prime." ),
		( 2147483647, True, "Large known Mersenne prime (2^31-1)." ),
		( 2.5, False, "Non-integer input should not be prime." ),
	]
	return tests

def run_tests():
	tests = generate_test_cases()
	all_passed = True
	for i, (inp, expected, reason) in enumerate(tests, start=1):
		result = is_prime(inp)
		passed = result == expected
		status = "PASS" if passed else "FAIL"
		print(f"Test {i}: input={inp!r:12} expected={expected!s:5} got={result!s:5} -> {status} -- {reason}")
		if not passed:
			all_passed = False
	if all_passed:
		print("\nAll tests passed.")
	else:
		print("\nSome tests failed.")

if __name__ == "__main__":
	run_tests()

