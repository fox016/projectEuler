smallest = 1504170715041708
coins = []
value = 0
n = 0
while n < 1000000000:
    value += 1504170715041707
    while value > 4503599627370517:
        value -= 4503599627370517
    if value < smallest:
        print(n, value)
        coins.append(value)
        smallest = value
    n+=1
print(sum(coins))
