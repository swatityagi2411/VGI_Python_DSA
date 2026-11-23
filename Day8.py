#___________Insertion Sort_______________#
def insertionSort(arr):
    for i in range(1,len(arr)):
        key=a[i]
        j=i-1
        while j>=0 && a[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr


#__________________Merge Sort_______________________________#
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
numbers = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(numbers))