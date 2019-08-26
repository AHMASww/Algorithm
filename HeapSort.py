import numpy as np 

def heapSort(nums):
    length = len(nums)
    count = length
    # 初始化最大堆
    for i in range((length-2) // 2, -1, -1):
        initHeap(nums, length, i)
    # 将nums[0]和nums[count-1]两个元素交换，长度减1，即将最大元素下沉到合适位置，再次重新初始化最大堆
    # 直到只剩下一个元素，排列完成
    while count > 1:
        nums[0], nums[count - 1] = nums[count - 1], nums[0]
        count -= 1
        for i in range((count - 2) // 2, - 1, -1):
            initHeap(nums, count, i)

    return nums


def initHeap(nums, length, cur_node):
    # 当前节点的左孩子节点
    left = 2 * cur_node + 1
    # 当前节点的右孩子节点
    right = 2 * cur_node + 2

    # 如果left和right都存在，则要和其中一个最大的判断
    if left < length and right < length:
        if nums[left] > nums[right]:
            next_node = left
        else:
            next_node = right
        if nums[cur_node] < nums[next_node]:
            nums[cur_node], nums[next_node] = nums[next_node], nums[cur_node]
            # 交换后，要判断交换后的点对其孩子的影响，采用递归方式
            initHeap(nums, length, next_node)
    # 如果只有left存在
    elif left < length:
        if nums[cur_node] < nums[left]:
            nums[cur_node], nums[left] = nums[left], nums[cur_node]
            initHeap(nums, length, left)
    # left，right都不存在

# 测试，随机产生列表， np.random.randint(low, hight, size)即[low, high)之间的size容量大小的张量
nums = list(np.random.randint(1, 200, size = 30))
print(nums)
nums = heapSort(nums)
print(nums)
