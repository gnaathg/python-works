arr = [
        [10,20],
        [30,40],
        [50,60]
]

numbers = [num for lst in arr for num in lst]

print(sum(numbers))


arr1 = [
        [11,20],
        [20,33],
        [34,41]
]

odds = [num for lst in arr1 for num in lst if num % 2 != 0]

print(odds)

num_gt_15 = [ num for lst in arr1 for num in lst if num > 15]

print(num_gt_15)