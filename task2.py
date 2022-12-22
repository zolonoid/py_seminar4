# Найти список множителей для числа n
def Divisions(n):
    a = []
    f = 2
    while n > 1:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 1
    return a


print("Составить список простых множителей для числа N")
inp=input("Введите натуральное число N...\n")
try:
    n=int(inp)
    print(f"Список простых множителей для числа {n}: {Divisions(n)}")
except:
    print("Это неправильное число")