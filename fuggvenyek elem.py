elem = [3,6,9,12]
print(elem)           


for i in enumerate(elem):
    print(i)

elem.append(3)
elem.append(-9)

elem.insert(2,10)

print(elem.count(11))

elem.sort()
print(elem)
