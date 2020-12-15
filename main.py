import random
import statistics

# mamy uzyc seed?
t1 = []
t2 = []
for x in range(1000):
    table = []
    for i in range(1000000):
        table.append(random.randrange(100))
    t1.append(statistics.mean(table))
    t2.append(statistics.stdev(table))

print(t2)

