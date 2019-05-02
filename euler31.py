values = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200
table = [1] + [0] * target
for value in values:
    for i in range(value, target+1):
        table[i] += table[i - value]

print table
print table[target]
