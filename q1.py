import sys
sys.setrecursionlimit(10**6)  # Set recursion limit to 10^6 or higher if needed

import time
import matplotlib.pyplot as plt

def sum_iterative(N):
    result = 0
    for i in range(1, N+1):
        result += i
    return result

def sum_recursive(N):
    if N == 0:
        return 0
    return N + sum_recursive(N - 1)

N_values = [10, 100, 1000, 10000, 100000]  
iterative_times = []
recursive_times = []

for N in N_values:
    start_time = time.time()
    sum_iterative(N)
    iterative_times.append(time.time() - start_time)

    start_time = time.time()
    sum_recursive(N)
    recursive_times.append(time.time() - start_time)

plt.plot(N_values, iterative_times, label='Iterative')
plt.plot(N_values, recursive_times, label='Recursive')
plt.xlabel('N')
plt.ylabel('Time (s)')
plt.title('Time taken to sum first N natural numbers')
plt.legend()
plt.show()
