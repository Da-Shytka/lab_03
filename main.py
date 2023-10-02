n = int(input("Введите количество чисел в массиве: "))
mas = []

for i in range(n):
    mas.append(int(input("Введите число: ")))

for i in range(n - 1):
    for j in range(n - i - 1):
        if mas[j] > mas[j + 1]:
            mas[j], mas[j + 1] = mas[j + 1], mas[j]

print(mas)