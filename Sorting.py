import random
import time
import matplotlib.pyplot as plt
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return sorted(left + right)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
    
def measure_time(sorting_function, arr):
    start_time = time.time()
    sorted_arr = sorting_function(arr)
    end_time = time.time()
    return sorted_arr, end_time - start_time

def main():
    print("Choose a sorting algorithm:")
    print("1. Merge Sort")
    print("2. Quick Sort")
    print("3. Selection Sort")
    choice = int(input("Enter the number of your choice: "))

    input_str = input("Enter a list of numbers separated by spaces: ")
    input_list = list(map(int, input_str.split()))

    if choice == 1:
        sorting_function = merge_sort
        sorting_name = "Merge Sort"
    elif choice == 2:
        sorting_function = quick_sort
        sorting_name = "Quick Sort"
    elif choice == 3:
        sorting_function = selection_sort
        sorting_name = "Selection Sort"
    else:
        print("Invalid choice. Exiting.")
        return

    input_sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    sort_time = []
    for size in input_sizes:
        sorted_arr, execution_time = measure_time(sorting_function, input_list.copy())
        print(f"{size} Elements Sorted by {sorting_name} in {execution_time:.9f} seconds")
        sort_time.append(execution_time)
    print(f"Sorted Array: {sorted_arr}")
    
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (s)")
    plt.title("Run Time Analysis")
    plt.plot(input_sizes, sort_time, label=sorting_name, marker='o')
    plt.grid(True)
    plt.legend()
    plt.show()
if __name__ == "__main__":
    main(
