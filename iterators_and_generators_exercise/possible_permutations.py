def possible_permutations(nums: list):
    if len(nums) == 1:
        yield nums
    else:
        for i in range(len(nums)):
            for p in possible_permutations(nums[:i] + nums[i + 1:]):
                yield [nums[i]] + p


[print(n) for n in possible_permutations([1, 2, 3])]