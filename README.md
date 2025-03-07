# Sorting Algorithm Performance Comparison

## Overview
This project compares the performance of **Bubble Sort**, **Selection Sort**, and Python's **Built-in Sort** on datasets of different sizes. The execution times are measured and analyzed.

## Results
### **Small Dataset (50 elements):**
✅ Bubble Sort took **0.000000 seconds**.
✅ Selection Sort took **0.000000 seconds**.

### **Large Dataset (1000 elements):**
⚠️ Bubble Sort took **0.104695 seconds**.
✅ Selection Sort took **0.049108 seconds**.
🚀 Python Built-in Sort took **0.000000 seconds**.

## Conclusion
1. **Small Datasets:**
   - Both Bubble Sort and Selection Sort execute nearly instantly on small inputs.
   - The choice of sorting algorithm does not significantly impact performance for small datasets.

2. **Large Datasets:**
   - **Bubble Sort is significantly slower** due to its O(n²) time complexity.
   - **Selection Sort performs better than Bubble Sort** because it makes fewer swaps, but it is still O(n²).
   - **Python’s Built-in Sort (Timsort) is the best choice**, completing in negligible time thanks to its O(n log n) complexity.

## Recommendations
- **For small datasets** (≤ 50 elements), any sorting algorithm works fine.
- **For large datasets**, avoid Bubble Sort and Selection Sort. Use Python’s built-in `sorted()` or `list.sort()` for optimal performance.
- Consider **Merge Sort or QuickSort** for cases where a built-in sort is not available.

## Future Improvements
- Compare with **Merge Sort**, **QuickSort**, and **Insertion Sort**.
- Test on **different data distributions** (random, sorted, reversed, nearly sorted).
- Implement **optimized versions** of Bubble Sort (early termination) and Selection Sort (fewer swaps).

