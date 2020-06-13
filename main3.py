# Amaury Lendasse
import time
import math

mymax = int(1e6)

myrange=range(3, mymax+1, 2)
myset1 = set(myrange)


start_time = time.time()
for i in range(3, int(math.sqrt(mymax)+1)):
    myset2 = set(range(i*2, mymax+1, i))
    myset1 = set.difference(myset1,myset2)

elapsed_time = time.time() - start_time
print(elapsed_time)

print(max(myset1))
print(len(myset1))
