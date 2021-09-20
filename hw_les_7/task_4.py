def bubble(nums):
    for j in range(len(nums) - 1):
        for i in range(len(nums) - 1 - j):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


def insertion(nums):
    for i in range(len(nums)):
        j = i - 1
        key = nums[i]
        while nums[j] > key and j >= 0:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)


numbers = [random.randint(-100, 100) for _ in range(10)]

print('Исходный массив:', numbers)
print('Сортировка пузырьковая:', bubble(numbers[:]))
print('Сортировка вставками:  ', insertion(numbers[:]))
print('Сортировка быстрая:    ', quicksort(numbers[:]))

time_bubble = timeit.timeit("bubble(numbers)", setup="from __main__ import bubble, numbers", number=100)
time_insertion = timeit.timeit("insertion(numbers)", setup="from __main__ import insertion, numbers", number=100)
time_quicksort = timeit.timeit("quicksort(numbers)", setup="from __main__ import quicksort, numbers", number=100)
time_merge = timeit.timeit("merge_sort(numbers)", setup="from __main__ import merge_sort, numbers", number=100)

print(time_bubble)
print(time_insertion)
print(time_quicksort)
print(time_merge)
