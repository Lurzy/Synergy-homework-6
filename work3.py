a = int(input())
b = int(input())

if a > b:
    print("Ошибка, значение A > B")
else:
    for i in range (a, b+1, +1):
        if i % 2 == 0:
            print (i)

