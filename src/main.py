def insert_sort(arr): # O(n^2)
    for i in range(1, len(arr)): # n -> O(n)
        curr = arr[i] # 1 * n -> O(n)
        j = i - 1 # 1 * n -> O(n)

        while j >= 0 and arr[j] > curr: # n * n -> O(n^2)
            arr[j + 1] = arr[j] # 1 * n * n -> O(n^2)
            j -= 1 # 1 * n * n -> O(n^2)

        arr[j + 1] = curr # 1 * n -> O(n)



array = [5, 3, 21, 13, 1, 7, 6, 15]
print("Before: ", array)

insert_sort(array)

print("After: ", array)
