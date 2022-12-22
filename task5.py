from pathlib import Path

def GetPolynomSum(p1,p2):
    return "47*x^5 + 51*x^4 + 101*x^3 + 137*x^2 + 78*x + 28"

print("Сформировать файл, содержащий сумму многочленов, полученных из двух файлов.")
try:
    p1=Path("polynom_1.txt").read_text()
    p2=Path("polynom_2.txt").read_text()
    sum=GetPolynomSum(p1,p2)
    fsum=Path("polynom_sum.txt")
    fsum.write_text(sum)
    print(f"Сумма многочленов {p1} и {p2} равная {sum} записана в файл {fsum.name}")
except Exception as exc:
    print(f"Что-то пошло не так...\n{exc}")