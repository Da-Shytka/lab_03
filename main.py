n = int(input("Введите количество чисел в массиве: "))
mas = []

for i in range(n):
    mas.append(int(input("Введите число: ")))

sort = int(input("Если хотите отсортировать по возрастанию, то введите 1, если по убыванию, то введите 2: "))

if(sort == 1):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if mas[j] > mas[j + 1]:
                mas[j], mas[j + 1] = mas[j + 1], mas[j]

elif (sort == 2):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if mas[j] < mas[j + 1]:
                mas[j], mas[j + 1] = mas[j + 1], mas[j]

else:
    print("Вы ввели не верную комбинацию")

print(mas)