# Задача 10
print("количество монеток:")
n = int(input())
a = 0
print("Орлы(1) и Решки(0)")
for i in range(n):
    OrelReshka = int(input())
    if OrelReshka == 1:
        a+=1
print(a if a<n/2 else n-a)
