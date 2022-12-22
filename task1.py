from random import uniform

# Получить кол-во цифр после точки.
def GetDigits(d):
    dstr = f"{d:.10f}"
    dot = dstr.index('.')
    one = dstr.index('1', dot)
    return one-dot


print("Вычислить число с заданной точностью d, где 0.0000000001 <= d <= 0.1.")
num = uniform(0.01, 9.99)
print(f"Дано число: {num}")
inp = input("Укажите с какой точностью нужно округлить число (например: 0.001)...\n").replace(',', '.')
try:
    d = float(inp)
    print(f"Результат округления до указанной точности: {num:.{GetDigits(d)}f}")
except:
    print("Это неправильное число")
