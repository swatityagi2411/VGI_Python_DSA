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