import math

def countsplitinversions(l1, l2):
    i = 0
    j = 0
    l = []
    num_count_inversions = 0

    while (i<len(l1) and j < len(l2)):
        if l1[i] < l2[j]:
            l.append(l1[i])
            i = i + 1
        else:
            l.append(l2[j])
            j = j + 1
            num_count_inversions = num_count_inversions + 1

    while i < len(l1):
        l.append(l1[i])
        i = i + 1

    while j < len(l2):
        l.append(l2[j])
        j = j + 1
    return (l, num_count_inversions)

def count_inversions(l):
    if len(l) <= 1:
        return (l, 0)
    half_len = math.ceil(len(l)/2)
    (list1, c1) = count_inversions(l[0:half_len])
    (list2, c2) = count_inversions(l[half_len:len(l)])
    (combined_list, c3) = countsplitinversions(list1, list2)
    return (combined_list, c1+c2+c3)

def test_count_inversions():
    print(count_inversions([1,7,2,3,1,5]))
    print(count_inversions([1,2,3,4,5]))
    print(count_inversions([1,2,3,4]))
    print(count_inversions([1,2,3]))
    print(count_inversions([2,1]))
    print(count_inversions([1]))
    print(count_inversions([]))

test_count_inversions()
