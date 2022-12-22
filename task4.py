from random import randint
from pathlib import Path


E = ['^0', '^1', '^2', '^3', '^4', '^5', '^6', '^7', '^8', '^9']


def CreatePolynom(k):
    polynom = ''
    for i in range(k, -1, -1):
        koef = randint(0, 100)
        base = '*x' if i > 0 else ''
        pow = E[i] if i > 1 else ''
        part = f"{koef}{base}{pow}"
        polynom+=f"{part}{' + ' if i > 0 else ''}"
    return polynom


print("Сформировать список коэффициентов многочлена и записать в файл многочлен степени k.")
inp = input("Укажите степень k многочлена от 2 до 9 ...\n")
try:
    k = int(inp)
    if k < 2 or k > 9:
        raise ValueError
    pol = CreatePolynom(k)
    fp1 = Path("polynom_1.txt")
    fp2 = Path("polynom_2.txt")
    fp = fp1 if fp1.stat().st_mtime_ns < fp2.stat().st_mtime_ns else fp2
    fp.write_text(pol)
    print(f"Многочлен {pol} сформирован и записан в файл {fp.name}")
except Exception as exc:
    print(f"Что-то пошло не так...\n{exc}")
