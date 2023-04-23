# Задача 26:  Посчитать факториал (произведение 1 до N) 
# и треугольное число (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов
a = int(input ("Введите число: "))
def factorial(num):
    if num == 1:
        return 1
    return factorial(num - 1) * num
        

def triangular_n(n):
    if n == 1:
        return 1
    return triangular_n(n - 1) + n

print(f'{a}! = {factorial(a)}')
print(f'треугольное число {a} = {triangular_n(a)}')



