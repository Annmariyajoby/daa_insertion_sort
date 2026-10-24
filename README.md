# Insertion Sort Algorithm

## 1. Aim

Implement the **Insertion Sort** algorithm using Python and analyze its time and space complexity using asymptotic notations.

## 2. Algorithm

Insertion Sort is a simple comparison-based sorting algorithm. It builds the sorted portion of an array one element at a time.

### Step-by-Step Algorithm

1. Start from the second element of the array.
2. Store the current element in a variable called `key`.
3. Compare `key` with the elements before it.
4. Shift all elements greater than `key` one position to the right.
5. Insert `key` into its correct position.
6. Repeat the process until the complete array is sorted.

## 3. Source Code

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Shift elements greater than key
        # one position to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key at the correct position
        arr[j + 1] = key

    return arr


# Sample input
arr = [12, 11, 13, 5, 6]

print("Input:", arr)

insertion_sort(arr)

print("Output:", arr)
```

## 4. Sample Input

```text
[12, 11, 13, 5, 6]
```

## 5. Sample Output

```text
[5, 6, 11, 12, 13]
```

## 6. Time Complexity Analysis

| Case | Condition | Time Complexity |
|---|---|---|
| Best Case | Array is already sorted | **O(n)** |
| Average Case | Elements are in random order | **O(n²)** |
| Worst Case | Array is sorted in reverse order | **O(n²)** |

### Best Case – O(n)

When the array is already sorted, each element only needs to be compared with the previous element. No shifting is required.

**Time Complexity: O(n)**

### Average Case – O(n²)

For randomly arranged elements, several elements may need to be shifted before inserting the current element.

**Time Complexity: O(n²)**

### Worst Case – O(n²)

When the array is sorted in descending order, every element needs to be shifted through the entire sorted portion.

**Time Complexity: O(n²)**

## 7. Space Complexity

Insertion Sort is an **in-place sorting algorithm**. It requires only a constant amount of extra memory.

**Space Complexity: O(1)**

## 8. Complexity Summary

```text
Best Case:     O(n)
Average Case:  O(n²)
Worst Case:    O(n²)
Space:         O(1)
```

## 9. Execution Steps

For the input:

```text
[5, 2, 4, 6, 1, 3]
```

The sorting process is:

```text
Initial:  [5, 2, 4, 6, 1, 3]

Insert 2: [2, 5, 4, 6, 1, 3]

Insert 4: [2, 4, 5, 6, 1, 3]

Insert 6: [2, 4, 5, 6, 1, 3]

Insert 1: [1, 2, 4, 5, 6, 3]

Insert 3: [1, 2, 3, 4, 5, 6]
```

## 10. Properties of Insertion Sort

- **In-place:** Yes
- **Stable:** Yes
- **Adaptive:** Yes
- **Simple to implement:** Yes
- **Suitable for small datasets:** Yes

## 11. Conclusion

Insertion Sort is a simple and efficient sorting algorithm for small or nearly sorted datasets. Its best-case time complexity is **O(n)**, while its average and worst-case time complexity is **O(n²)**. It requires only **O(1)** auxiliary space.

## 12. Course Outcome

**CO1:** Analyze and express the time and space complexities of an algorithm using asymptotic notations.
