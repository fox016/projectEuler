names = sorted([line.split(",") for line in open("files/22.dat", 'r')][0])

print sum(map(lambda name, index: sum(["ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(n)+1 for n in name]) * index, names, range(1, len(names)+1)))
