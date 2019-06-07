from __future__ import division
from itertools import combinations

# sieve of Eratosthenes
# make it so sieve[i] is smallest prime factor of i
prime_limit = 20000
sieve = list()
def fill_sieve(upper):
  global sieve
  size = upper+1
  sieve = [0] * size
  for i in xrange(2, size):
    if sieve[i] == 0:
      n = 1
      while i * n < size:
        if sieve[i*n] == 0:
          sieve[i*n] = i
        n+=1
fill_sieve(prime_limit)

# return dictionary where each key is prime factor of n and value is prime factor's highest power divisible by n
stored_prime_factors = {}
def get_prime_factors_and_powers(n):
  global stored_prime_factors
  if n in stored_prime_factors:
    return stored_prime_factors[n]
  factor_power_map = {}
  curr = sieve[n] # current prime factor (start with smallest prime factor of n)
  power = 1 # power of current prime factor
  init_num = n
  while n > 1:
    n //= sieve[n]
    if curr == sieve[n]:
      power+=1
      continue
    factor_power_map[curr] = power
    curr = sieve[n]
    power = 1
  stored_prime_factors[init_num] = factor_power_map
  return factor_power_map

# Get all prime factors for B(n) parts (and thus for B(n))
def get_prime_factors_powers_b(n):
  if n <= 2:
    return {n: 1}
  # Get list of numerators and denominators in calculating B(n)
  numer = [n] # numbers in B(n) numerator
  denom = [] # numbers in B(n) denominator
  bottom_fac = 2
  half = (n // 2)
  for x in xrange(1, half): # only go halfway to take advantage of symmetry
    sym = 2 if ((n & 1 == 1) or (x < half - 1)) else 1 # symmetry
    for y in xrange(sym):
      for sub in xrange(x+1):
        numer.append(n-sub)
      for den in xrange(2, bottom_fac+1):
        denom.append(den)
    bottom_fac+=1
  numer.append(n) # symmetry
  # Get all prime factors and powers of numerators and add them
  factor_power_map = {}
  for n in numer:
    pfs = get_prime_factors_and_powers(n)
    for pf in pfs:
      if pf in factor_power_map:
        factor_power_map[pf] += pfs[pf]
      else:
        factor_power_map[pf] = pfs[pf]
  # Get all prime factors and powers of denominators and subtract them
  for d in denom:
    pfs = get_prime_factors_and_powers(d)
    for pf in pfs:
      factor_power_map[pf] -= pfs[pf]
  return factor_power_map;

# Get sum of all divisors for B(n) after calculating prime factorization 
# D(n) is the sum of all divisors of B(n) (sum_of_divisors, sum_of_factors, sum_factors)
# B(n) is product of all (n choose k) from k=0 to k=n
# In general, if you have the prime factorization of the number n, then to calculate the sum of its divisors, you take each different prime factor and add together all its powers up to the one that appears in the prime factorization, and then multiply all these sums together! (From https://www.math.upenn.edu/~deturck/m170/wk3/lecture/sumdiv.html)
# S(p^k) = 1 + p + p^2 + . . . + p^k = (p^(k+1) - 1) / (p-1) .
def D(n):
  if n == 1:
    return 1
  if n % 10 == 0:
    print "Calculating D(n) for", n
  pfs = get_prime_factors_powers_b(n)
  return reduce(lambda x, y: x * y, map(lambda pf: ((pf**(pfs[pf]+1)-1)//(pf-1)), pfs), 1)

# S(n) is the sum of all D(k) from k=1 to k=n
def S(n):
  return sum(map(lambda k: D(k), xrange(1, n+1)))

print "S(5):"
print S(5)
print "S(10):"
print S(10)
print "S(100) mod 1,000,000,007:"
print S(100) % 1000000007
print "S(20,000) mod 1,000,000,007:"
print S(20000) % 1000000007
