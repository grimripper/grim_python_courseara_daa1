import math

def mergelists(l1, l2):
    i = 0
    j = 0
    l = []

    while (i<len(l1) and j < len(l2)):
        if l1[i] < l2[j]:
            l.append(l1[i])
            i = i + 1
        else:
            l.append(l2[j])
            j = j + 1

    while i < len(l1):
        l.append(l1[i])
        i = i + 1

    while j < len(l2):
        l.append(l2[j])
        j = j + 1
    return l

def merge_sort(l):
    if len(l) <= 1:
        return l
    half_len = math.ceil(len(l)/2)
    list1 = merge_sort(l[0:half_len])
    list2 = merge_sort(l[half_len:len(l)])
    return mergelists(list1, list2)

def test_merge_sort():
    print(merge_sort([1,7,2,3,1,5]))
    print(merge_sort([1,2,3,4,5]))
    print(merge_sort([1,2,3,4]))
    print(merge_sort([1,2,3]))
    print(merge_sort([2,1]))
    print(merge_sort([1]))
    print(merge_sort([]))

test_merge_sort()
