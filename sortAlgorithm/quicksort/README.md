# Info

QuickSort is a Divide and Conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.
 - Always pick the first element as a pivot.
 - Always pick the last element as a pivot (implemented below)
 - Pick a random element as a pivot.
 - Pick median as the pivot.

The key process in quickSort is a partition(). The target of partitions is, given an array and an element x of an array as the pivot, put x at its correct position in a sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.

## Partition Algorithm

There can be many ways to do partition, following pseudo-code adopts the method given in the CLRS book. The logic is simple, we start from the leftmost element and keep track of the index of smaller (or equal to) elements as i. While traversing, if we find a smaller element, we swap the current element with arr[i]. Otherwise, we ignore the current element.

## Pseudo Code for recursive QuickSort function:

```math
/* low  –> Starting index,  high  –> Ending index */
quickSort(arr[], low, high) {

    if (low < high) {

        /* pi is partitioning index, arr[pi] is now at right place */

        pi = partition(arr, low, high);

        quickSort(arr, low, pi – 1);  // Before pi

        quickSort(arr, pi + 1, high); // After pi

    }

}
```

## Pseudo code for partition()  

```math
/* This function takes last element as pivot, places the pivot element at its correct position in sorted array, and places all smaller (smaller than pivot) to left of pivot and all greater elements to right of pivot */
partition (arr[], low, high)
{
    // pivot (Element to be placed at right position)
    pivot = arr[high];  

    i = (low – 1)  // Index of smaller element and indicates the 
    // right position of pivot found so far

    for (j = low; j <= high- 1; j++){

        // If current element is smaller than the pivot
        if (arr[j] < pivot){
            i++;    // increment index of smaller element
            swap arr[i] and arr[j]
        }
    }
    swap arr[i + 1] and arr[high])
    return (i + 1)
}
```

## Following are the implementations of QuickSort

```python
# Python3 implementation of QuickSort


# Function to find the partition position
def partition(array, low, high):

 # Choose the rightmost element as pivot
 pivot = array[high]

 # Pointer for greater element
 i = low - 1

 # Traverse through all elements
 # compare each element with pivot
 for j in range(low, high):
  if array[j] <= pivot:
   # If element smaller than pivot is found
   # swap it with the greater element pointed by i
   i = i + 1

   # Swapping element at i with element at j
   (array[i], array[j]) = (array[j], array[i])

 # Swap the pivot element with
 # e greater element specified by i
 (array[i + 1], array[high]) = (array[high], array[i + 1])

 # Return the position from where partition is done
 return i + 1

# Function to perform quicksort


def quick_sort(array, low, high):
 if low < high:

  # Find pivot element such that
  # element smaller than pivot are on the left
  # element greater than pivot are on the right
  pi = partition(array, low, high)

  # Recursive call on the left of pivot
  quick_sort(array, low, pi - 1)

  # Recursive call on the right of pivot
  quick_sort(array, pi + 1, high)


# Driver code
array = [10, 7, 8, 9, 1, 5]
quick_sort(array, 0, len(array) - 1)

print(f'Sorted array: {array}')

```

## Analysis of QuickSort

Time taken by QuickSort, in general, can be written as follows.

```math
 T(n) = T(k) + T(n-k-1) + \theta (n)
```

The first two terms are for two recursive calls, the last term is for the partition process. k is the number of elements that are smaller than the pivot.
The time taken by QuickSort depends upon the input array and partition strategy. Following are three cases.

## Worst Case

The worst case occurs when the partition process always picks the greatest or smallest element as the pivot. If we consider the above partition strategy where the last element is always picked as a pivot, the worst case would occur when the array is already sorted in increasing or decreasing order. Following is recurrence for the worst case.  

```math
 T(n) = T(0) + T(n-1) + \theta (n)
 which is equivalent to T(n) = T(n-1) + \theta (n)
```

The solution to the above recurrence is `(n^2)`.

## Best Case

The best case occurs when the partition process always picks the middle element as the pivot. The following is recurrence for the best case.

```math
 T(n) = 2T(n/2) + \theta (n)
```

## Average Case

To do average case analysis, we need to consider all possible permutation of array and calculate time taken by every permutation which doesn’t look easy.
We can get an idea of average case by considering the case when partition puts O(n/9) elements in one set and O(9n/10) elements in other set. Following is recurrence for this case.  

```math
 T(n) = T(n/9) + T(9n/10) + \theta (n)
```

The solution of above recurrence is also `O(nLogn)`:

## Advantages of Quick Sort

 - It is a divide-and-conquer algorithm that makes it easier to solve problems.
 - It is efficient on large data sets.
 - It has a low overhead, as it only requires a small amount of memory to function.

## Disadvantages of Quick Sort

 - It has a worst-case time complexity of O(n^2), which occurs when the pivot is chosen poorly.
 - It is not a good choice for small data sets.
 - It can be sensitive to the choice of pivot.
 - It is not cache-efficient.
 - It is not stable sort, meaning that if two elements have the same key, their relative order will not be preserved in the sorted output in case of quick sort, because here we swapping of elements according to pivot’s position (without considering their original positions).

