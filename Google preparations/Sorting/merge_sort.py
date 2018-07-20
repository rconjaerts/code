# function to merge two lists together
def combine_lists(l=[], r=[]):
    if not l:
        return r
    elif not r:
        return l
    else:
        curr = []
        while l and r:
            if l[0] < r[0]:
                curr.append(l.pop(0))
            else:
                curr.append(r.pop(0))
        if l:
            curr.extend(l)
        else:
            curr.extend(r)
        return curr

# merge sort algorithm
def merge_sort(l=[]):
    if not l:
        return []
    elif len(l) == 1:
        return l
    else:
        i = int(len(l)/2)
        left = merge_sort(l[:i])
        right = merge_sort(l[i:])
        return combine_lists(left, right)

# test cases
to_sort = [5,7,2,5345,345,7,3,1,2,55,8,54,3]
to_sort_empty = []
to_sort_small = [1]
to_sort_ordered = [1,2,3,4,5]
to_sort_reversed = [5,4,3,2,1]

to_sort = merge_sort(to_sort)
to_sort_empty = merge_sort(to_sort_empty)
to_sort_small = merge_sort(to_sort_small)
to_sort_ordered = merge_sort(to_sort_ordered)
to_sort_reversed = merge_sort(to_sort_reversed)

print(to_sort)
print(to_sort_empty)
print(to_sort_small)
print(to_sort_ordered)
print(to_sort_reversed)