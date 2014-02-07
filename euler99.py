from math import log

sizes = map(lambda pair: pair[1] * log(pair[0]), [map(int, (lines.split(','))) for lines in open('files/99.dat', 'r')])
print sizes.index(max(sizes))+1
