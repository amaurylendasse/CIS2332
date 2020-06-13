# Amaury Lendasse
import time

myrange = list(range(3, int(1e4), 2))

start_time = time.time()
for i in myrange:
    if i>(myrange[-1]/i):
        break
    for j in range(i,(myrange[-1]+1)//i+1,2):
        m=j*i
        if (m in myrange):
            myrange.remove(m)

elapsed_time = time.time() - start_time
print(elapsed_time)

print(len(myrange))
print(myrange)