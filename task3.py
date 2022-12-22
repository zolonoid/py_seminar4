from random import randint

# Найти различающиеся элементы последовательности nums
def Distinct(nums):
    dist = []
    for num in nums:
        if num in dist:
            continue
        dist.append(num)
    return dist


print("Вывести список неповторяющихся элементов исходной последовательности.")
try:
    nums = [randint(1, 9) for i in range(randint(10, 20))]
    print(f"Задана последовательность чисел: {nums}")
    print(f"Список неповторяющихся элементов: {Distinct(nums)}")
except Exception as exc:
    print(f"Что-то пошло не так...\n{exc}")
