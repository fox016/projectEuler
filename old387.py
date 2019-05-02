prime_limit = 100000000
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

fill_sieve(prime_limit)

# get integer dividend and remainder
def divide_get_parts(a, b):
  if b == 0:
    raise ZeroDivisionError("Cannot divide by 0")
  d = a // b
  r = a - (d * b)
  return d, r

# harshad number is divisible by sum of its digits
def is_harshad(a):
  return a % (sum(map(int, str(a)))) == 0

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

# strong harshad is a harshad number that when divided by sum of digits, results in prime
def is_strong_harshad(a):
  d, r = divide_get_parts(a, sum(map(int, str(a))))
  return r == 0 and prime(d)

# strong right truncatable harshad prime is prime number that, after removing last digit, is strong and right truncatable harshad
# a must be >= 10 
# lowest such number is 181
def is_strong_right_trunc_harshad_prime(a):
  if not prime(a):
    return False
  a //= 10
  d, r = divide_get_parts(a, sum(map(int, str(a))))
  if r != 0 or not prime(d):
    return False
  return is_right_trunc_harshad(a // 10)

# strong right truncatable harshad prime is prime number that, after removing last digit, is strong and right truncatable harshad
# p must be known prime >= 101
# lowest such number is 181
def is_strong_right_trunc_harshad_prime_p(p):
  p //= 10
  d, r = divide_get_parts(p, sum(map(int, str(p))))
  if r != 0 or not prime(d): # r == 0 tests for harshad, prime(d) tests for strong
    return False
  return is_right_trunc_harshad(p // 10)

total = 0
for i in xrange(50, (prime_limit >> 1) + 1):
  if sieve[i]:
    p = i*2+1
    if is_strong_right_trunc_harshad_prime_p(p):
      print p
      total += p
print total
