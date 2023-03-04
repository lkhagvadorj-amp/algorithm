# Info
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.

# How does Bubble Sort Work
## Input: 
```
arr[] = {5, 1, 4, 2, 8}
```

## First Pass:

Bubble sort starts with very first two elements, comparing them to check which one is greater.
```
( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.
```

## Second Pass:

Now, during second iteration it should look like this:
```
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
```

## Third Pass:

Now, the array is already sorted, but our algorithm does not know if it is completed.
The algorithm needs one whole pass without any swap to know it is sorted.
```
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
```

# Follow the below steps to solve the problem:

 - Run a nested for loop to traverse the input array using two variables `i` and `j`, such that `0 ≤ i < n-1` and `0 ≤ j < n-i-1`
 - If arr[j] is greater than arr[j+1] then swap these adjacent elements, else move on
 - Print the sorted array

Below is the implementation of the above approach:
```python
# Python program for implementation of Bubble Sort


def bubbleSort(arr):
 n = len(arr)

 # Traverse through all array elements
 for i in range(n):

  # Last i elements are already in place
  for j in range(0, n-i-1):

   # traverse the array from 0 to n-i-1
   # Swap if the element found is greater
   # than the next element
   if arr[j] > arr[j+1]:
    arr[j], arr[j+1] = arr[j+1], arr[j]


# Driver code to test above
if __name__ == "__main__":
arr = [5, 1, 4, 2, 8]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
 print("%d" % arr[i], end=" ")

```

## Complexity
Time Complexity: `O(N^2)`
Auxiliary Space: `O(1)`

# Optimized Implementation of Bubble Sort
The above function always runs O(N2) time even if the array is sorted. It can be optimized by stopping the algorithm if the inner loop didn’t cause any swap.

Below is the implementation for the above approach:
```python
# Optimized Python program for implementation of Bubble Sort

def bubbleSort(arr):
 n = len(arr)
 # Traverse through all array elements
 for i in range(n):
  swapped = False

  # Last i elements are already in place
  for j in range(0, n-i-1):

   # traverse the array from 0 to n-i-1
   # Swap if the element found is greater
   # than the next element
   if arr[j] > arr[j+1]:
    arr[j], arr[j+1] = arr[j+1], arr[j]
    swapped = True
  if (swapped == False):
   break


# Driver code to test above
if __name__ == "__main__":
 arr = [64, 34, 25, 12, 22, 11, 90]

 bubbleSort(arr)

 print("Sorted array is:")
 for i in range(len(arr)):
  print("%d" % arr[i], end=" ")

```

## Complexity

Time Complexity: `O(N^2)`
Auxiliary Space: `O(1)`

# Worst Case Analysis for Bubble Sort
The worst-case condition for bubble sort occurs when elements of the array are arranged in decreasing order.
In the worst case, the total number of iterations or passes required to sort a given array is `(n-1)`. where ‘n’ is a number of elements present in the array.

```
  At pass 1 :  Number of comparisons = (n-1)
                     Number of swaps = (n-1)

  At pass 2 :  Number of comparisons = (n-2)
                     Number of swaps = (n-2)

  At pass 3 :  Number of comparisons = (n-3)
                    Number of swaps = (n-3)
                              .
                             .
                             .
  At pass n-1 :  Number of comparisons = 1
                        Number of swaps = 1

Now , calculating total number of comparison required to sort the array
= (n-1) + (n-2) +  (n-3) + . . . 2 + 1
= (n-1)*(n-1+1)/2  { by using sum of N natural Number formula }
= n (n-1)/2
```

For the Worst case:
```
Total number of swaps = Total number of comparison
Total number of comparison (Worst case) = n(n-1)/2
Total number of swaps (Worst case) = n(n-1)/2
```
```
Worst and Average Case Time Complexity: O(N2). The worst case occurs when an array is reverse sorted.
Best Case Time Complexity: O(N). The best case occurs when an array is already sorted.
Auxiliary Space: O(1)
```

# Algorithm
 1. Start with an array of unsorted numbers
 1. Define a function called “bubbleSort” that takes in the array and the length of the array as parameters
 1. In the function, create a variable called “sorted” that is set to false
 1. Create a for loop that iterates through the array starting at index 0 and ending at the length of the array -1
 1. Within the for loop, compare the current element with the next element in the array
 1. If the current element is greater than the next element, swap their positions and set “sorted” to true
 1. After the for loop, check if “sorted” is true
 1. If “sorted” is true, call the “bubbleSort” function again with the same array and length as parameters
 1. If “sorted” is false, the array is now sorted and the function will return the sorted array
 1. Call the “bubbleSort” function with the initial unsorted array and its length as parameters to begin the sorting process.


# What is the Boundary Case for Bubble sort?
Bubble sort takes minimum time (Order of n) when elements are already sorted. Hence it is best to check if the array is already sorted or not beforehand, to avoid O(N2) time complexity.

# Does sorting happen in place in Bubble sort?
Yes, Bubble sort performs the swapping of adjacent pairs without the use of any major data structure. Hence Bubble sort algorithm is an in-place algorithm.

# Is the Bubble sort algorithm stable?
Yes, the bubble sort algorithm is stable.

# Where is the Bubble sort algorithm used?
Due to its simplicity, bubble sort is often used to introduce the concept of a sorting algorithm.
In computer graphics, it is popular for its capability to detect a tiny error (like a swap of just two elements) in almost-sorted arrays and fix it with just linear
complexity (2n).

Example: It is used in a polygon filling algorithm, where bounding lines are sorted by their x coordinate at a specific scan line (a line parallel to the x-axis), and with incrementing y their order changes (two elements are swapped) only at intersections of two lines

## Advantages:
 - Bubble sort is easy to understand and implement.
 - It does not require any additional memory space.
 - It’s adaptability to different types of data.
 
## Disadvantages
 - Bubble sort has a time complexity of O(n^2) which makes it very slow for large data sets.
 - It is not efficient for large data sets, because it requires multiple passes through the data.
 - It is not a stable sorting algorithm, meaning that elements with the same key value may not maintain their relative order in the sorted output.
