def insertSort(nums):
    if not nums:
        return nums
    s = len(nums)
    for i in range(s-1):
        for j in range(i+1, 0, -1):
            if nums[j] > nums[j-1]:
                break
            nums[j], nums[j-1] = nums[j-1], nums[j]
    return nums


def shellSort(nums):
    gap = 1
    s = len(nums)
    while gap < s//3:
        gap = gap * 3 + 1

    while gap > 0:
        for i in range(gap, s):
            for j in range(i - gap, -1, -gap):
                if nums[j + gap] > nums[j]:
                    break
                nums[j], nums[j + gap] = nums[j + gap], nums[j]
        gap //= 3
    return nums


def selectSort(nums):
    s = len(nums)
    for i in range(s-1):
        temp = i
        for j in range(i + 1, s):
            if nums[temp] > nums[j]: temp = j
        nums[i], nums[temp] = nums[temp], nums[i]
    return nums


def heapSort(nums):
    for i in range(len(nums)-1, -1, -1):
        heapfy(nums, i)
        nums[0], nums[i] = nums[i], nums[0]
    return nums


def heapfy(nums, limit):
    if len(nums) <= 0 or len(nums) < limit+1:
        return
    for parentNode in range(limit//2, -1, -1):
        leftChild = min(2 * parentNode + 1, limit)
        rightChild = min(2 * parentNode + 2, limit)
        maxChild = leftChild if nums[leftChild] > nums[rightChild] else rightChild
        if nums[maxChild] > nums[parentNode]:
            nums[parentNode], nums[maxChild] = nums[maxChild], nums[parentNode]


def bubbleSort(nums):
    for i in range(len(nums), 0, -1):
        t = 0
        for j in range(0, i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                t += 1
        if t == 0: return nums
    return nums


def quickSort(nums, low, high):
    if len(nums) <= 1:return
    if low >= high: return
    left, right = low, high
    temp = nums[left]
    while left < right:
        while right > left and nums[right] >= temp:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= temp:
            left += 1
        nums[right] = nums[left]
    nums[left] = temp
    quickSort(nums, 0, left-1)
    quickSort(nums, left+1, high)


def mergeSort(nums):
    if len(nums) <= 1: return nums
    p = len(nums)//2
    nums1 = nums[:p].copy()
    nums2 = nums[p:].copy()
    a1 = mergeSort(nums1)
    a2 = mergeSort(nums2)
    return mergeTwoArray(a1, a2)


def mergeTwoArray(array1, array2):
    res = []
    i, j = 0, 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            res.append(array1[i])
            i += 1
        else:
            res.append(array2[j])
            j += 1
    while i < len(array1):
        res.append(array1[i])
        i += 1
    while j < len(array2):
        res.append(array2[j])
        j += 1
    return res