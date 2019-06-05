from __future__ import division
from itertools import combinations

# functions for n choose k (n-choose-k)
def factorial(n):
	f = 1
	for i in xrange(1,n+1):
		f *= i
	return f
def falling_factorial(x, n):
	f = 1
	for i in xrange(n):
		f *= (x - i)
	return f
def choose(n, k):
	return falling_factorial(n, k) / factorial(k)
  
# sieve of Eratosthenes
# make it so sieve[i] is smallest prime factor of i
prime_limit = 184756
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
print "Fill sieve..."
fill_sieve(prime_limit)
print "Sieve filled"

# return dictionary where each key is prime factor of n and value is prime factor's highest power divisible by n
def get_prime_factors_and_powers(n):
  print "Get prime factors and powers(", n, ")"
  global sieve
  factor_power_map = {}
  curr = sieve[n] # current prime factor (start with smallest prime factor of n)
  power = 1 # power of current prime factor
  while n > 1:
    n //= sieve[n]
    if curr == sieve[n]:
      power+=1
      continue
    factor_power_map[curr] = power
    curr = sieve[n]
    power = 1
  return factor_power_map

"""
# B(n) is product of all (n choose k) from k=0 to k=n
#def B(n):
#  return int(reduce(lambda x, y: x*y, map(lambda k: choose(n, k), xrange(0, n+1)), 1))
def B(n):
  print "Calculate B(", n, ")"
  choose_results = map(lambda k: choose(n, k), xrange(0, n//2 + 1))
  if n & 1 == 0:
    return int(reduce(lambda x, y: x*y, choose_results + choose_results[:-1], 1))
  return int(reduce(lambda x, y: x*y, choose_results + choose_results, 1))
"""

# B(n) is product of all (n choose k) from k=0 to k=n
# This returns list of numbers multiplied together to get B(n)
def get_n_choose_k_parts(n):
  parts = [1]
  for i in xrange(1, n//2 + 1):
    parts.append(int(choose(n, i)))
  return parts

# Get all prime factors for B(n) parts (and thus for B(n))
def get_prime_factors_powers_b(n):
  parts = get_n_choose_k_parts(n)
  factor_power_map = {}
  if n & 1 == 0:
    parts = parts + parts[:-1]
  else:
    parts = parts + parts
  print "parts:", parts
  for part in parts:
    pfs = get_prime_factors_and_powers(part)
    for pf in pfs:
      if pf in factor_power_map:
        factor_power_map[pf] += pfs[pf]
      else:
        factor_power_map[pf] = pfs[pf]
  return factor_power_map

# Get sum of all divisors for B(n) after calculating prime factorization 
# D(n) is the sum of all divisors of B(n) (sum_of_divisors, sum_of_factors, sum_factors)
# B(n) is product of all (n choose k) from k=0 to k=n
# In general, if you have the prime factorization of the number n, then to calculate the sum of its divisors, you take each different prime factor and add together all its powers up to the one that appears in the prime factorization, and then multiply all these sums together! (From https://www.math.upenn.edu/~deturck/m170/wk3/lecture/sumdiv.html)
# S(p^k) = 1 + p + p^2 + . . . + p^k = (p^(k+1) - 1) / (p-1) .
def D(n):
  print "Calculate D(", n, ")"
  # Get prime factors and powers for B(n)
  pfs = get_prime_factors_powers_b(n)
  print pfs
  div_sum = 1
  for pf in pfs:
    div_sum *= int((pf**(pfs[pf]+1) - 1) / (pf -1))
  print "div_sum:", div_sum
  return div_sum

# S(n) is the sum of all D(k) from k=1 to k=n
def S(n):
  print "Calculate S(", n, ")"
  return sum(map(lambda k: D(k), xrange(1, n+1)))

#print S(5)
#print S(6)
print S(10)
#print S(20)
#print S(20000)
