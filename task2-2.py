# 2. Создать список, длины n, значения формируются по формуле 3k + 1,
# где k принимает значения от 1 до n включительно.
numbers = [ ]
count = int(input("Write count numbers: "))
for i in range(1, count+1):
    numbers.append(3*i +1)

print(numbers)