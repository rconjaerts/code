def matrixReshape(nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    if not nums:
        return nums
    
    old_r = len(nums)
    old_c = len(nums[0])
    if not old_r*old_c == r*c:
        return nums
    
    curr_r = 0
    curr_c = 0
    sol = []
    curr_row = []
    
    for i in range(old_r):
        for j in range(old_c):
            val = nums[i][j]
            curr_row.append(val)
            #sol[curr_r][curr_c] = val
            curr_c += 1
            if curr_c >= c:
                sol.append(curr_row)
                curr_row = []
                curr_r += 1
                curr_c = 0
    return sol

print(matrixReshape([[1,2],[3,4]], 4, 1))