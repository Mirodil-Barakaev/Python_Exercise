def filter_positive(nums):
    positive_nums = []
    for num in nums:
        if num > 0:
            positive_nums.append(num)
    return positive_nums

numbers = [-2, 5, 0, -1, 3, 8, -7]
print(filter_positive(numbers))
