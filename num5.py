#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
import math
print(math.sqrt(((x2-x1)**2)+((y2-y1)**2)))