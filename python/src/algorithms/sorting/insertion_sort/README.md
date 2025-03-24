# Insertion Sort

Consider the following example where we're sorting the array (min-to-max).

```text
Example - 9, 6, 7, 3, 2

Divide the array into 2 part - one from where you are to extreme left and other from the next element from where you are to the extreme right

9 | 6, 7, 3, 2

As we're in position 0 i.e. 9
Now compare the current position element with the adjacent element on the left side. Since here we don't have one, our 1st iteration is done. This also tells that the 1st iteration will alway be useless as there will be no element on the left adjacent to our 1st element

Now we're in 2nd position (i.e. 6) and 2nd iteration. Do the same thing as above

9, 6 | 7, 3, 2

Now compare 6 with its left adjacent element and check if 6 is smaller than it, if yes then swap else not this iteration. As 6 is smaller than 9 so swap and we get.

6, 9, 7, 3, 2

Now we're in 3rd iteration

6, 9, 7 | 3, 2

Compare 7 with 9 and swap as (7 < 9)
6, 7, 9 | 3, 2
Compare 7 with 6 and do nothing as (7 > 6) and now we've
6, 7, 9, 3, 2

Iteration 4
6, 7, 9, 3 | 2

Do the same steps
6, 7, 3, 9 | 2
6, 3, 7, 9 | 2
3, 6, 7, 9 | 2

Iteration 5
3, 6, 7, 9, 2
3, 6, 7, 2, 9
3, 6, 2, 7, 9
3, 2, 6, 7, 9
2, 3, 6, 7, 9

And now the array is sorted.
```

## Time Complexities

- Insertion sort is an efficient sorting algorithm, as it does not run on preset conditions using for loops, but instead it uses one while loop, which avoids extra steps once the array gets sorted.
- Even though insertion sort is efficient, still, if we provide an already sorted array to the insertion sort algorithm, it will still execute the outer for loop, thereby requiring n steps to sort an already sorted array of n elements, which makes its best case time complexity a linear function of n.

- Worst Case Time Complexity [ Big-O ] : O(n^2)
- Best Case Time Complexity [ Big-omega ]: O(n)
- Average Time Complexity [ Big-theta ] : O(n^2)
- Space Complexity : O(1)

- In the worst case scenario, an array would be sorted in reverse order. The outer for loop in the Insertion Sort function always iterates n-1 times.
