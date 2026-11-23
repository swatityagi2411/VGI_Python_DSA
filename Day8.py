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

#__________________________Quick Sort________________________________#
def partition(arr,low,high):
    pivot= arr[low]
    left=low+1
    right=high

    while True:
        while left<=right and arr[left]<=pivot:
            left=left+1
        while left<=right and arr[right]>pivot:
            right=right-1
        if left>right:
            arr[right],arr[low]=arr[low],arr[right]
        else:
       
            arr[right],arr[left]=arr[left],arr[right]
    return arr

def quick_sort(arr,low,high):
    if low<high:
        partion(arr,low,high)
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)