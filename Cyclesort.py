# Filename: cycle_sort.py

def cycle_sort(arr: list[int]) -> list[int]:
    """
    Sorts a list using the Cycle Sort algorithm, minimizing memory writes.
    """
    writes = 0
    
    # Iterate through the array to find cycles for each element.
    for cycle_start_index in range(len(arr) - 1):
        item = arr[cycle_start_index]
        
        # Find the correct position where the item should be.
        pos = cycle_start_index
        for i in range(cycle_start_index + 1, len(arr)):
            if arr[i] < item:
                pos += 1
        
        # If the item is already in the correct position, do nothing.
        if pos == cycle_start_index:
            continue
            
        # Skip over any duplicates to find the final correct position.
        while item == arr[pos]:
            pos += 1
            
        # Place the item in its correct position.
        arr[pos], item = item, arr[pos]
        writes += 1
        
        # Continue rotating the rest of the cycle until it's complete.
        while pos != cycle_start_index:
            pos = cycle_start_index
            for i in range(cycle_start_index + 1, len(arr)):
                if arr[i] < item:
                    pos += 1
            
            while item == arr[pos]:
                pos += 1

            if item != arr[pos]:
                arr[pos], item = item, arr[pos]
                writes += 1
                
    # print(f"Total writes to memory: {writes}")
    return arr

# --- Example Usage ---
my_list = [0, 1, 2, 8, 3, 7, 4, 6, 5]
print(f"Original: {my_list}")
cycle_sort(my_list)
print(f"Sorted:   {my_list}")


another_list = [5, 2, 8, 1, 9, 4, 3]
print(f"\nOriginal: {another_list}")
sorted_list = cycle_sort(another_list)
print(f"Sorted:   {sorted_list}")
