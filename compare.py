import time
import random
import matplotlib.pyplot as plt
import numpy as np

# Bubble Sort Implementation
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        counter = 0
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                counter += 1
        if counter == 0:
            return arr
    return arr

# Selection Sort Implementation
def selection_sort(arr):
    for i in range(len(arr) - 1):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

# Insertion Sort Implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Function to test sorting performance
def test_sorting_performance():
    """
    Generates a list of random numbers and tests the execution time of both sorting algorithms.
    """
    small_dataset = [random.uniform(1, 100) for _ in range(50)]
    large_dataset = [random.uniform(1, 100) for _ in range(10000)]
    
    print("\n🔹 Small Dataset (50 elements):")
    
    # Bubble Sort test
    bubble_test = small_dataset.copy()
    start_time = time.time()
    bubble_sort(bubble_test)
    end_time = time.time()
    print(f"✅ Bubble Sort took {end_time - start_time:.6f} seconds.")
    
    # Selection Sort test
    selection_test = small_dataset.copy()
    start_time = time.time()
    selection_sort(selection_test)
    end_time = time.time()
    print(f"✅ Selection Sort took {end_time - start_time:.6f} seconds.")
    
    # Insertion sort test
    insertion_test = small_dataset.copy()
    start_time = time.time()
    insertion_sort(selection_test)
    end_time = time.time()
    print(f"✅ Insertion Sort took {end_time - start_time:.6f} seconds.")
    
    print("\n🔹 Large Dataset (1000 elements):")
    
    # Bubble Sort test
    bubble_test = large_dataset.copy()
    start_time = time.time()
    bubble_sort(bubble_test)
    end_time = time.time()
    print(f"⚠️ Bubble Sort took {end_time - start_time:.6f} seconds.")
    
    # Selection Sort test
    selection_test = large_dataset.copy()
    start_time = time.time()
    selection_sort(selection_test)
    end_time = time.time()
    print(f"✅ Selection Sort took {end_time - start_time:.6f} seconds.")
    
    # Insertion Sort test
    insertion_test = large_dataset.copy()
    start_time = time.time()
    insertion_sort(insertion_test)
    end_time = time.time()
    print(f"✅ Insertion Sort took {end_time - start_time:.6f} seconds.")
    
    # Python Built-in Sort
    python_sort_test = large_dataset.copy()
    start_time = time.time()
    sorted(python_sort_test)
    end_time = time.time()
    print(f"🚀 Python Built-in Sort took {end_time - start_time:.6f} seconds.")

# New function to plot sorting algorithm performance
def plot_sorting_performance():
    """
    Plot the performance of different sorting algorithms with increasing input sizes.
    """
    # Input sizes to test
    input_sizes = [100, 500, 1000, 2000, 3000, 4000, 5000]
    
    # Initialize dictionaries to store execution times
    bubble_times = []
    selection_times = []
    insertion_times = []
    python_times = []
    
    # Test each input size
    for size in input_sizes:
        print(f"Testing with input size: {size}")
        
        # Generate a dataset for this size
        dataset = [random.uniform(1, 100) for _ in range(size)]
        
        # Bubble Sort
        bubble_test = dataset.copy()
        start_time = time.time()
        bubble_sort(bubble_test)
        end_time = time.time()
        bubble_times.append(end_time - start_time)
        
        # Selection Sort
        selection_test = dataset.copy()
        start_time = time.time()
        selection_sort(selection_test)
        end_time = time.time()
        selection_times.append(end_time - start_time)
        
        # Insertion Sort
        insertion_test = dataset.copy()
        start_time = time.time()
        insertion_sort(insertion_test)
        end_time = time.time()
        insertion_times.append(end_time - start_time)
        
        # Python's built-in sort
        python_test = dataset.copy()
        start_time = time.time()
        sorted(python_test)
        end_time = time.time()
        python_times.append(end_time - start_time)
    
    # Create the plot
    plt.figure(figsize=(12, 8))
    
    # Plot each algorithm with different colors
    plt.plot(input_sizes, bubble_times, 'ro-', label='Bubble Sort', linewidth=2)
    plt.plot(input_sizes, selection_times, 'go-', label='Selection Sort', linewidth=2)
    plt.plot(input_sizes, insertion_times, 'bo-', label='Insertion Sort', linewidth=2)
    plt.plot(input_sizes, python_times, 'mo-', label='Python Built-in Sort', linewidth=2)
    
    # Add labels and title
    plt.xlabel('Input Size', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    plt.title('Sorting Algorithm Performance Comparison', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=12)
    
    # Add a text annotation about time complexity
    complexity_text = "Time Complexity:\nBubble Sort: O(n²)\nSelection Sort: O(n²)\nInsertion Sort: O(n²)\nPython Sort: O(n log n)"
    plt.annotate(complexity_text, xy=(0.02, 0.97), xycoords='axes fraction', 
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8),
                 va='top', fontsize=10)
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    # Create a second plot with a more suitable scale for comparing the faster algorithms
    plt.figure(figsize=(12, 8))
    
    # Plot only selection, insertion and Python's built-in sort
    plt.plot(input_sizes, selection_times, 'go-', label='Selection Sort', linewidth=2)
    plt.plot(input_sizes, insertion_times, 'bo-', label='Insertion Sort', linewidth=2)
    plt.plot(input_sizes, python_times, 'mo-', label='Python Built-in Sort', linewidth=2)
    
    # Add labels and title
    plt.xlabel('Input Size', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    plt.title('Sorting Algorithm Performance (Excluding Bubble Sort)', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=12)
    
    # Show the plot
    plt.tight_layout()
    plt.show()

# Run the performance test
test_sorting_performance()

# Run the plotting function
plot_sorting_performance()