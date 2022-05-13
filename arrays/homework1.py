#Homework 1:
#Given an array a of n numbers and a count k find the k largest values in the array a.
#Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  ⇒  [6, 8, 7]

def n_largest(arr, n):
    """find n largest items in array using heap sort for time efficiency""" #you could also use merge sort here for the same time complexity
    if n >= len(arr):
        return arr
    arr = heap_sort(arr)
    return arr[len(arr)-n:len(arr)]

#o(nlog(n))
def heap_sort(arr):
    """heap sort algorithm for arrays""" 
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heap(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  #swap
        heap(arr, i, 0)

    return arr

def heap(arr, n, i):
    """simple heaping algorithm to assist in heap sort"""
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
 
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] #swap
 
        heap(arr, n, largest) #recursive heaping

a=[5, 1, 3, 6, 8, 2, 4, 7]
k=3
print(n_largest(a,k))