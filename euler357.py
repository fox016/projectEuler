from math import ceil, sqrt

# Prime tester
"""
prime_set = set()

def prime(a):
  if a in prime_set:
    return True
  if not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1))):
    prime_set.add(a)
    return True
  return False
"""

# Generate primes using sieve method
"""
def primes(upper):
  set_primes = set(xrange(3, upper, 2))
  for i in xrange(3, int(ceil(sqrt(upper))), 2):
    if i in set_primes:
      multiples_of_i = set(xrange(2 * i, upper, i))
      set_primes -= multiples_of_i
  set_primes.add(2)
  return set_primes

prime_set = primes(limit+1)
def prime(a):
  return a in prime_set;
"""

limit = 100000000

sieve = list()

# sieve of Eratosthenes
def prime(a):
  global sieve
  if a & 1 == 0:
    return a == 2
  return sieve[a >> 1]

def fill_sieve(upper):
  global sieve
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

def is_every_divisor_magic(n):
  for d in xrange(1, int(ceil(sqrt(n))) + 1):
    if n % d == 0:
      if not prime(d + n/d):
        return False
  return True

fill_sieve(limit+1)
total = 1
k = 0
n = 2
while n <= limit:
  if is_every_divisor_magic(n):
    total += n
  k+=1
  n=4*k+2
print total
