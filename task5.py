from pathlib import Path

E = ['^0', '^1', '^2', '^3', '^4', '^5', '^6', '^7', '^8', '^9']

def GetPolynomSum(p1: str,p2: str):
    parts1=p1.split(' + ')
    parts2=p2.split(' + ')
    kofs1=[k.split('*')[0] for k in parts1]
    kofs2=[k.split('*')[0] for k in parts2]
    pows1=[k.split('^')[1] for k in parts1 if '^' in k]
    pows1.append('1')
    pows1.append('0')
    pows2=[k.split('^')[1] for k in parts2 if '^' in k]
    pows2.append('1')
    pows2.append('0')
    kps1=dict(list(zip(pows1,kofs1)))
    kps2=dict(list(zip(pows2,kofs2)))
    sum=dict()
    for i in range(9,-1,-1):
        key=str(i)
        kof1=kps1[key] if key in kps1 else 0
        kof2=kps2[key] if key in kps2 else 0
        kofSum=int(kof1)+int(kof2)
        if kofSum>0:
            sum[key]=int(kof1)+int(kof2)
    psum=''
    for i in range(9,-1,-1):
        key=str(i)
        if key not in sum: continue
        koef = sum[key]
        base = '*x' if i > 0 else ''
        pow = E[i] if i > 1 else ''
        part = f"{koef}{base}{pow}"
        psum+=f"{part}{' + ' if i > 0 else ''}"
    return psum

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