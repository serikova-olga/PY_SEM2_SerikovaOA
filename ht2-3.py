# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n 
# и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13
numbers = [ ]
count = int(input("Write count numbers: "))
for i in range(1, count+1):
    numbers.append((1+1/n)**n)

print(numbers)