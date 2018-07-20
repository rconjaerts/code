# bubble sort algorithm
def bubble_sort(l=[]):
    for i in range(len(l)):
        for j in range(len(l)-2, i-1, -1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
        

# test cases
to_sort = [5,7,2,5345,345,7,3,1,2,55,8,54,3]
to_sort_empty = []
to_sort_small = [1]
to_sort_ordered = [1,2,3,4,5]
to_sort_reversed = [5,4,3,2,1]

bubble_sort(to_sort)
bubble_sort(to_sort_empty)
bubble_sort(to_sort_small)
bubble_sort(to_sort_ordered)
bubble_sort(to_sort_reversed)

print(to_sort)
print(to_sort_empty)
print(to_sort_small)
print(to_sort_ordered)
print(to_sort_reversed)