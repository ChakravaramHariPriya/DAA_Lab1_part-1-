import random
import time
import matplotlib.pyplot as plt

array = [random.randint(1, 1000) for _ in range(10000)]

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

search_keys = [random.randint(1, 1000) for _ in range(5)]  

linear_times = []
binary_times = []

for key in search_keys:
    start_time = time.time()
    linear_search(array, key)
    linear_times.append(time.time() - start_time)

    start_time = time.time()
    array.sort()  
    binary_search(array, key)
    binary_times.append(time.time() - start_time)

plt.plot(search_keys, linear_times, label='Linear Search')
plt.plot(search_keys, binary_times, label='Binary Search')
plt.xlabel('Search Key')
plt.ylabel('Time (s)')
plt.title('Time taken by Linear and Binary Search for 5 different search keys')
plt.legend()
plt.show()
