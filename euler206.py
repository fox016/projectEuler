n = long(19293949596979899**(1.0/2.0))+1
while not str(n*n)[::2] == "123456789": n-=2
print n*10
