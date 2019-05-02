"""
def fill_sieve(upper):
  global primes
  global greatest_prime
  half = (upper >> 1) + 1
  sieve = [True] * half
  sieve[0] = False
  i = 1
  while 2*i*i < half:
    if sieve[i]:
      current = 3*i+1
      while current < half:
        sieve[current] = False
        current += 2*i+1
    i+=1
  primes.add(2)
  for i in xrange(1, half):
    if sieve[i]:
      new_prime = i*2+1
      primes.add(new_prime)
      greatest_prime = new_prime

def prime(a):
  global primes
  global greatest_prime
  if a in primes:
    return True
  if a < greatest_prime:
    return False
  for p in primes:
    if a % p == 0:
      return False
  primes.add(a)
  greatest_prime = a
  return True
"""

def _try_composite(a, d, n, s):
  if pow(a, d, n) == 1:
    return False
  for i in range(s):
    if pow(a, 2**i * d, n) == n-1:
      return False
  return True # n  is definitely composite

def is_prime(n, _precision_for_huge_n=16):
  if n in _known_primes:
    return True
  if any((n % p) == 0 for p in _known_primes) or n in (0, 1):
    return False
  d, s = n - 1, 0
  while not d % 2:
    d, s = d >> 1, s + 1
  # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
  if n < 1373653: 
    return not any(_try_composite(a, d, n, s) for a in (2, 3))
  if n < 25326001: 
    return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
  if n < 118670087467: 
    if n == 3215031751: 
      return False
    return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
  if n < 2152302898747: 
    return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
  if n < 3474749660383: 
    return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
  if n < 341550071728321: 
    return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
  # otherwise
  return not any(_try_composite(a, d, n, s) for a in _known_primes[:_precision_for_huge_n])

_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]

# get integer dividend and remainder
def divide_get_parts(a, b):
  if b == 0:
    raise ZeroDivisionError("Cannot divide by 0")
  d = a // b
  r = a - (d * b)
  return d, r

# right truncatable harshad is a harshad number that is harshad when right digit truncated recursively
def is_right_trunc_harshad(a):
  dig_sum = sum(map(int, str(a)))
  while dig_sum > 0:
    if a % dig_sum != 0:
      return False
    d, r = divide_get_parts(a, 10)
    dig_sum -= r
    a = d
  return True

# strong right truncatable harshad - strong (division by digit sum is prime), right trunc (harhsad when right digit truncated recursively)
def is_strong_right_trunc_harshad(a):
  d, r = divide_get_parts(a, sum(map(int, str(a))))
  if r != 0:
    return False
  if not is_right_trunc_harshad(a // 10):
    return False
  if not is_prime(d):
    return False
  return True

# strong right truncatable harshad prime is prime number that, after removing last digit, is strong and right truncatable harshad
# a must be >= 10 
# lowest such number is 181
def is_strong_right_trunc_harshad_prime(a):
  if not is_prime(a):
    return False
  a //= 10
  d, r = divide_get_parts(a, sum(map(int, str(a))))
  if r != 0 or not is_prime(d):
    return False
  return is_right_trunc_harshad(a // 10)

# strong right truncatable harshad prime is prime number that, after removing last digit, is strong and right truncatable harshad
# p must be known prime >= 101
# lowest such number is 181
def is_strong_right_trunc_harshad_prime_p(p):
  p //= 10
  d, r = divide_get_parts(p, sum(map(int, str(p))))
  if r != 0 or not is_prime(d): # r == 0 tests for harshad, is_prime(d) tests for strong
    return False
  return is_right_trunc_harshad(p // 10)

if __name__ == "__main__":
  #prime_limit = 1000000
  #primes = set()
  #greatest_prime = 2
  #fill_sieve(prime_limit)
  limit = 100000000
  total = 0
  for n in xrange(1, limit/10+1):
    if is_strong_right_trunc_harshad(n):
      for d in [1, 3, 7, 9]:
        test = n*10 + d
        if is_prime(test):
          print test
          total += test
  print total
