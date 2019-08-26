import numpy as np 

def heapSort(nums):
    length = len(nums)
    count = length
    for i in range((length-2) // 2, -1, -1):
        initHeap(nums, length, i)

    while count > 1:
        nums[0], nums[count - 1] = nums[count - 1], nums[0]
        count -= 1
        for i in range((count - 2) // 2, - 1, -1):
            initHeap(nums, count, i)

    return nums


def initHeap(nums, length, cur_node):
    left = 2 * cur_node + 1
    right = 2 * cur_node + 2

    if left < length and right < length:
        if nums[left] > nums[right]:
            next_node = left
        else:
            next_node = right
        if nums[cur_node] < nums[next_node]:
            nums[cur_node], nums[next_node] = nums[next_node], nums[cur_node]
            initHeap(nums, length, next_node)
    elif left < length:
        if nums[cur_node] < nums[left]:
            nums[cur_node], nums[left] = nums[left], nums[cur_node]
            initHeap(nums, length, left)

nums = list(np.random.randint(1, 200, size = 30))
print(nums)
nums = heapSort(nums)
print(nums)