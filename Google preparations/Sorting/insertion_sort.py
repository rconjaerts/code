# insertion sort algorithm
def insertion_sort(l=[]):
    for i in range(1, len(l)):
        curr_el = l[i]
        position = 0
        for j in range(i-1, -1, -1):
            if l[j] > curr_el:
                l[j+1] = l[j]
            else:
                position = j+1
                break
        l[position] = curr_el

# test cases
to_sort = [5,7,2,5345,345,7,3,1,2,55,8,54,3]
to_sort_empty = []
to_sort_small = [1]
to_sort_ordered = [1,2,3,4,5]
to_sort_reversed = [5,4,3,2,1]

insertion_sort(to_sort)
insertion_sort(to_sort_empty)
insertion_sort(to_sort_small)
insertion_sort(to_sort_ordered)
insertion_sort(to_sort_reversed)

print(to_sort)
print(to_sort_empty)
print(to_sort_small)
print(to_sort_ordered)
print(to_sort_reversed)