#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
nomer= int(input())
if nomer==1:
    print("значение х и у больше или равны нулю " )
elif nomer==2:
    print("х - меньше или равен нулю , у - больше или равен нулю")    
elif nomer==3:
    print("значения х и у меньше или равны нулю")  
elif nomer==4:
    print("х -больше или равен нулю ,у -меньше или равен нулю")    
else:
    print("повторите ввод")      