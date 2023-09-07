n = int(input("Enter the length of the array: "))
my_array = [int(input(f"Enter an integer for element {i + 1}: ")) for i in range(n)]
print("Array Items:", my_array)

index = int(input(f"Enter the index (0-{n- 1}) to access an element: "))
if 0 <= index < n:
    print(f"Element at index {index}: {my_array[index]}")
else:
    print(f"Invalid index. Please enter an index between 0 and {n - 1}.")
