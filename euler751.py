from math import floor
from decimal import Decimal

def get_a(theta, n=24):
    b = [Decimal(0.0)] * n
    b[0] = Decimal(theta)
    for i in range(1, n): 
        prev = Decimal(b[i-1])
        f = int(floor(prev))
        b[i] = Decimal(f * (prev - f + 1))
    return map(floor, b)

theta = Decimal(2.223561019313554106173177)
a = get_a(theta, 24)
tau = "".join(map(str, a))
tau_f = Decimal(tau[0] + "." + tau[1:])
print(tau)
print(tau_f)
print(theta)
print(abs(tau_f-theta))
print("")
