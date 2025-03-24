# Quick Sort

Quick sort is a divide-and-conquer algorithm for sorting an array of elements. It works by selecting a "pivot" element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

Time complexity: O(n log n) average, O(n^2) worst case

Here's how the quick sort algorithm works:

Choose a pivot element from the array. This element will serve as the dividing point between the lower and higher elements.

Partition the array into two sub-arrays, one containing elements less than the pivot and the other containing elements greater than the pivot.

Sort the two sub-arrays recursively using the same quick sort algorithm.

Combine the sorted sub-arrays and the pivot element to obtain a fully sorted array.

The pivot element can be chosen in various ways, such as selecting the first, last, or middle element of the array, or using a random element as the pivot.

The time complexity of the quick sort algorithm is O(n log n) on average, where n is the number of elements in the array. This makes it a faster sorting algorithm than bubble sort or selection sort for large arrays. However, its time complexity can degrade to O(n^2) in the worst case scenario if the pivot is not chosen wisely, so careful consideration of the pivot selection strategy is important for optimizing the performance of the algorithm.
