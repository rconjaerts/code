# selection sort algorithm
def selection_sort(l=[]):
    for i in range(len(l)-1):
        curr_small = l[i]
        curr_index = i

        for j in range(i+1, len(l)):
            if l[j] < curr_small:
                curr_small = l[j]
                curr_index = j

        l[i], l[curr_index] = l[curr_index], l[i]

# test cases
to_sort = [5,7,2,5345,345,7,3,1,2,55,8,54,3]
to_sort_empty = []
to_sort_small = [1]
to_sort_ordered = [1,2,3,4,5]
to_sort_reversed = [5,4,3,2,1]

selection_sort(to_sort)
selection_sort(to_sort_empty)
selection_sort(to_sort_small)
selection_sort(to_sort_ordered)
selection_sort(to_sort_reversed)

print(to_sort)
print(to_sort_empty)
print(to_sort_small)
print(to_sort_ordered)
print(to_sort_reversed)