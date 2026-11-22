from random import randint
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def bin_search(arr, target):
    left = 0
    right = len(arr) - 1
    comp = 0
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            comp+=1
            return mid, comp
        elif arr[mid] < target:
            left = mid + 1
            comp+=1
        else:
            right = mid - 1
            comp+=1
    return -1, comp

#measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]
measurements = []
for _ in range(1000):
    measurements.append(randint(0, 100))
#val = int(input('Введите число: '))
val = randint(0, 103)
print(measurements, '\n', val)
su = 0
mini = measurements[0]
maxi = measurements[0]
chet = 0
mt = 0                   #кол-во превосходящих среднее арифметическое
flag_enter = 0
prost = 0
comp_lin = 0
for j in range(len(measurements)):
    i = measurements[j]
    flag_prost =0
    if flag_enter ==0:
        comp_lin+=1
        if i == val:
            print(f'индекс элемента в исходном массиве: {j} (линейный поиск)')
            flag_enter = 1
    su+=i
    if i>maxi: maxi = i
    elif i<mini: mini = i
    if i%2 == 0: chet+=1

    for deli in range(2, int((i**0.5))+1):
        if flag_prost == 0 and i%deli == 0:
            flag_prost = 1
            break
    if i <= 1: flag_prost = 1
    if flag_prost == 0: prost+=1
if flag_enter ==0: print('индекс элемента в исходном массиве: -1 (линейный поиск)')
sr_ar = su/len(measurements)
for x in measurements:
    if x>sr_ar: mt+=1

print(f'сумма: {su} \nминимум: {mini} \nмаксимум: {maxi} \nкол-во четных: {chet} \nкол-во превосходящих среднее арифметическое: {mt} \nпростых чисел: {prost}')

sorted_measurements = selection_sort(measurements)
idx_a, comp_bin = bin_search(sorted_measurements, val)
print(f'индекс искомого элемента {val} в отсортированном массиве: {idx_a} (бинарный поиск)')
print('---------------------------------------------')
print(f'сравнений при линейном поиске: {comp_lin}')
print(f'сравнений при бинарном поиске: {comp_bin}')