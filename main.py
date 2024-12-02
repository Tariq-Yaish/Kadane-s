data = [1 ,3, -5, 6, 0, 7, -1, -9, 3, 1, 0, 13, -2, 1, 0, 10]

maxElement = 0
maxAlaways = 0

for i in data:
    maxElement = max(0, maxElement + data[i])
    maxAlaways = max(maxAlaways, maxElement)

print(maxAlaways)
print(data)