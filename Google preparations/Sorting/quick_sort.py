def quick_sort_helper(l, min_i, max_i):
    if min_i >= max_i:
        return
    else:
        pivot = max_i
        left, right = min_i, max_i-1
        done = False
        while not done:
            while left != right and l[left] < l[pivot]:
                left += 1
            while left != right and l[right] > l[pivot]:
                right -=1
            
            if left != right:
                l[left], l[right] = l[right], l[left]
                left += 1
            else:
                if l[left] > l[pivot]:
                    l[left], l[pivot] = l[pivot], l[left]
                    pivot = left
                else:
                    l[left+1], l[pivot] = l[pivot], l[left+1]
                    pivot = left+1
                done = True
        quick_sort_helper(l, min_i, pivot-1)
        quick_sort_helper(l, pivot+1, max_i)

# quick sort algorithm
def quick_sort(l=[]):
    quick_sort_helper(l, 0, len(l)-1)
        

# test cases
to_sort = [5,7,2,5345,345,7,3,1,2,55,8,54,3]
to_sort_empty = []
to_sort_small = [1]
to_sort_ordered = [1,2,3,4,5]
to_sort_reversed = [5,4,3,2,1]

quick_sort(to_sort)
quick_sort(to_sort_empty)
quick_sort(to_sort_small)
quick_sort(to_sort_ordered)
quick_sort(to_sort_reversed)

print(to_sort)
print(to_sort_empty)
print(to_sort_small)
print(to_sort_ordered)
print(to_sort_reversed)