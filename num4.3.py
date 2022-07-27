#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

numbers = [3, 10, 20, 30, 30, 40, 50, 125, 40, 10, 125]

def get_unique_num(numbers):
    unique = []
    for num in numbers:
        if num in unique:
            continue
        else:
            unique.append(num)
    return unique

print(get_unique_num(numbers))

