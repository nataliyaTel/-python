#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции вводятся с клавиатуры .
def get_mult(numbers, first_list):
    mult = 1
    for i in numbers:
        mult *= first_list[int(i)]
    return mult
n = int(input('Введите число: '))
first_list = list(range(-n, n + 1))
print(first_list)
numbers = input('Введите позицию чисел через пробел: ').split()
print(get_mult(numbers, first_list))