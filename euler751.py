from math import floor
from decimal import Decimal

def get_a(theta, n=24):
    b = [Decimal(0.0)] * n
    b[0] = Decimal(theta)
    for i in range(1, n): 
        prev = Decimal(b[i-1])
        f = int(floor(prev))
        b[i] = Decimal(f * (prev - f + 1))
    return map(int, map(floor, b))

place = Decimal(1.0/10.0)
theta = Decimal(2.0)
for i in range(24):
    next_digit = None
    for d in range(10):
        theta_tmp = theta + (place * d)
        a = get_a(theta_tmp, 24)
        tau = "".join(map(str, a))
        tau_f = Decimal(tau[0] + "." + tau[1:])
        diff = tau_f-theta_tmp
        if diff < 0:
            next_digit = d-1
            break
    if next_digit == None:
        next_digit = 9
    theta = theta + (place * next_digit)
    place=place/Decimal(10.0)

print(theta)
