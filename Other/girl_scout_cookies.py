def merge_lists(l1, l2):
    res = []
    i1 = 0
    i2 = 0

    while i1 < len(l1) and i2 < len(l2):
        if l1[i1] < l2[i2]:
            res.append(l1[i1])
            i1 += 1
        else:
            res.append(l2[i2])
            i2 += 1

    if i1 < len(l1):
        res.extend(l1[i1:])

    if i2 < len(l2):
        res.extend(l2[i2:])
    return res

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

print merge_lists(my_list, alices_list)
# prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]