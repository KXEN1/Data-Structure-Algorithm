#!/usr/bin/env python
# coding: utf-8

# In[18]:


def quickSort(arr, start, end, duplicates):
    if end <= start: #base case
        return

    low = start
    high = end
    pivot = arr[(start + end) // 2]

    while low <= high:
        while arr[low] < pivot:
            low += 1

        while arr[high] > pivot:
            high -= 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low + 1, high - 1

    mid = low  # pivot

    # 중복된 숫자를 찾아 duplicates 리스트에 추가
    if mid - start > 1:
        for i in range(start, mid - 1):
            if arr[i] == arr[mid - 1] and arr[i] not in duplicates:
                duplicates.append(arr[i])

    if end - mid > 1:
        for i in range(mid + 1, end):
            if arr[i] == arr[mid + 1] and arr[i] not in duplicates:
                duplicates.append(arr[i])

    quickSort(arr, start, mid - 1, duplicates) # 왼쪽 부분 배열을 재귀적으로 정렬
    quickSort(arr, mid + 1, end, duplicates) # 오른쪽 부분 배열을 재귀적으로 정렬

if __name__ == "__main__":
    arr = [random.randint(1, 50) for _ in range(300)]
    print("랜덤 숫자 리스트:", arr)
    print()

    duplicates = []
    quickSort(arr, 0, len(arr) - 1, duplicates)

    if duplicates:
        print("중복된 숫자:", duplicates)
    else:
        print("중복된 숫자 없음")


# In[ ]:




