def mid(a, l, r):
    m = a[int((l+r)/2)]
    i = l
    j = r
    while(i <= j):
        while(a[i] < m):
            i += 1
        while(a[j] > m):
            j -= 1
        if (i >= j):
            break
        a[i], a[j] = a[j], a[i]
        i+=1
        j-=1
    return j

def hoar(a, l, r):
    if(l < r):
        m = mid(a, l, r)
        hoar(a, l, m)
        hoar(a, m + 1, r)
    return None

input_array = [int(el) for el in input().split()]

even = []
for a in input_array:
    if a % 2 == 0:
        even.append(a)
print("Четные числа: ", even)

hoar(input_array, 0, len(input_array)-1)
print("Максимальное число: ", input_array[-1])
print("Минимальное число: ", input_array[0])
print("Отсортированный список:", input_array)
