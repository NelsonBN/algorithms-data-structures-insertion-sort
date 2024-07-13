def insert_sort(arr): # O(n^2)
    n = len(arr) # O(1)

    for i in range(1, n): # n -> O(n)
        j = i # 1 * n -> O(n)

        while j > 0 and arr[j - 1] > arr[j]: # n * n -> O(n^2)
            arr[j], arr[j - 1] = arr[j - 1], arr[j] # 1 * n * n -> O(n^2)
            j -= 1 # 1 * n * n -> O(n^2)



array = [5, 3, 21, 13, 1, 7, 6, 15]
print("Before: ", array)

insert_sort(array)

print("After: ", array)
