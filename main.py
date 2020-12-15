import random
import statistics


for x in range(1000):
    print(x)
    table = []
    for i in range(1000000):
        table.append(random.randrange(100))
        print(i)

    me = statistics.mean(table)
    dirav = statistics.stdev(table)

print(me)
print(dirav)
