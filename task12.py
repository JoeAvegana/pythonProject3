#Задача 12
print("Петя загадывает числа...")
x = int(input())
y = int(input())
S = x+y
print (f"Сумма равна {S}")
P = x*y
print (f"Произведение равно {P}")
print ("Катя находит числа, используя дискриминант")
D = S**2 - 4 * P
temp1=-S + D**(0.5)
x1 = temp1 / 2 * -1
temp2 = -S - D**(0.5)
x2 = temp2 / 2 * -1
print(x1, x2)