# Bubble Sort

Consider we're sorting a list where elements from smaller to bigger. Here, we start with the first element on the left side & compare it with its adjacent element, if its bigger than adjacent one then swap positions of those values else move to the second position & repeat the previous step. Once you've done the first iteration the largest element in the container will be in the last position of the array & so by doing this with each iteration our right side of the container gets more sorted & soon the array is sorted.

```text
Examples: Sort - 40, 20, 50, 60, 30, 10

======================================
=========== 1st Iteration ============
======================================

40, 20, 50, 60, 30, 10
|   |

Swap since 40 is bigger than 20

20, 40, 50, 60, 30, 10
    |   |

Do nothing since 40 is smaller than 50

20, 40, 50, 60, 30, 10
        |   |

And so on...

20, 40, 50, 60, 30, 10
            |   |

20, 40, 50, 30, 60, 10
                |   |

20, 40, 50, 30, 10, 60

Now after the 1st iteration the biggest element 60 is at the end

======================================
=========== 2nd Iteration ============
======================================

20, 40, 50, 30, 10, 60
|   |

20, 40, 50, 30, 10, 60
    |   |

20, 40, 50, 30, 10, 60
        |   |

20, 40, 30, 50, 10, 60
            |   |

20, 40, 30, 10, 50, 60
                |   |

2nd iteration completed

======================================
=========== 3rd Iteration ============
======================================

20, 40, 30, 10, 50, 60
|   |

20, 40, 30, 10, 50, 60
    |   |

20, 30, 40, 10, 50, 60
        |   |

20, 30, 10, 40, 50, 60
            |   |

20, 30, 10, 40, 50, 60
                |   |

And so on...
Number of iterations will = number of elements in the array/list/etc...
```

An optimization can be done which to check in one iteration how many swapping are done, if 0 then stop because your array is sorted.

## Time Complexities

In Bubble Sort, n-1 comparisons will be done in the 1st pass, n-2 in 2nd pass, n-3 in 3rd pass and so on. So the total number of comparisons will be: (n-1) + (n-2) + (n-3) + ..... + 3 + 2 + 1, Sum = n(n-1)/2 i.e. O(n^2) Hence the time complexity of Bubble Sort is O(n^2).

- The main advantage of Bubble Sort is the simplicity of the algorithm.
- The space complexity for Bubble Sort is O(1), because only a single additional memory space is required i.e. for temporary variable.
- Also, the best case time complexity will be O(n), it is when the list is already sorted.

- Worst Case Time Complexity [ Big-O ] : O(n^2)
- Best Case Time Complexity [ Big-omega ]: O(n)
- Average Time Complexity [ Big-theta ] : O(n^2)
- Space Complexity : O(1)

In the worst case scenario (when the list is in reverse order), this algorithm would have to swap every single item of the array. Therefore, if we have n elements in our list, we would have n iterations per item - thus Bubble Sort's time complexity is O(n^2).
