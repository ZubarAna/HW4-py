'''
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
'''
n = int(input("Введите число: "))
i = 2 # первое простое число,  1 - не простое
numbers = []
n1 = n
while i <= n:
    if n % i == 0:
        numbers.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {n1}: {numbers}")