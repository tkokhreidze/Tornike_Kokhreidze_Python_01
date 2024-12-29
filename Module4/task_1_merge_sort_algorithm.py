def merge_sort(collection):
  if len(collection) <= 1:
    return collection

  mid = len(collection) // 2
  left_half = merge_sort(collection[:mid])  
  right_half = merge_sort(collection[mid:])  

  return merge(left_half, right_half)

def merge(left, right):
  merged = []
  i = j = 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1

  merged += left[i:]
  merged += right[j:]

  return merged


# Test cases
test_cases = [
    [],  # Empty list
    [1],  # Single-element list
    [5, 2, 8, 1, 9, 4],  # Unsorted list
    [1, 2, 3, 4, 5],  # Already sorted list
    [5, 4, 3, 2, 1],  # Reverse sorted list
    [5, 2, 8, 2, 9, 4, 2], # List with duplicates
    [-1, 0, 5, -3, 2] # List with negative numbers
]

expected_results = [
    [],
    [1],
    [1, 2, 4, 5, 8, 9],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [2, 2, 2, 4, 5, 8, 9],
    [-3, -1, 0, 2, 5]
]

for i, test_case in enumerate(test_cases):
    sorted_list = merge_sort(test_case)
    print(f"Test Case {i+1}: Input: {test_case}, Output: {sorted_list}, Expected: {expected_results[i]}")
    assert sorted_list == expected_results[i], f"Test Case {i+1} failed"

print("All simple test cases passed!")
