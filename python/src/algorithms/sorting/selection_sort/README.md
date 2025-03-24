# Selection Sort

Considering we're sorting to get container (list/array/etc...) where elements are from smaller to bigger.

- Here we start from the first element on the left side of our container (list/array/etc...)
- and then find the smallest element in remaining part on the right side of our container
- and then compare it with the current first element,
- if current first element is smaller than that then we move to the second element with making any changes,
- but if the first element is bigger then what we got as smaller element in the remaining container,
- then we exchange values in those positions
- and then move to the second element and repeat this step till we've went through all the elements.

```text
Example

// Sorting A
A = 5, 4, 1, 8, 3

5, 4, 1, 8, 3
|

Starting from 5, the smallest element in the remaining part is 1 (if we wouldn't have found one then we would've moved forward without making any changes)

5, 4, 1, 8, 3
|     |

So exchanging the values and we get

1, 4, 5, 8, 3

Now we're at 2nd position

1, 4, 5, 8, 3
   |

Now 3 is the smallest number in the remaining part on the right side

1, 4, 5, 8, 3
   |        |

Exchange those values and we get

1, 3, 5, 8, 4

And so on...

1, 3, 5, 8, 4
      |     |

1, 3, 4, 8, 5
         |  |

1, 3, 4, 5, 8  <-- sorted
```

## More info

- We can easily get the time complexity by examining the for loops in the Selection Sort algorithm.
- For an array with n elements, the outer loop iterates n times. The inner loop iterate n-1 when i is equal to 1, and then n-2 as i is equal to 2 and so forth.
- The amount of comparisons are (n - 1) + (n - 2) + ... + 1, which gives the Selection Sort a time complexity of O(n^2).
- Since, Sum = n-1 + n-2 + n-3 + ... + 3 + 2 + 1 = n(n-1)/2

## Time Complexities

- Worst Case Time Complexity [ Big-O ] : O(n^2)
- Best Case Time Complexity [ Big-omega ]: O(n^2)
- Average Time Complexity [ Big-theta ] : O(n^2)
- Space Complexity : O(1)
