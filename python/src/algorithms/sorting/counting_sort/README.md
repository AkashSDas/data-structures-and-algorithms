# Count Sort

```text
Array = 5, 3, 2, 3, 6, 1
```

In counting sort you need to know the highest value in your array. In the above case its 6.

Now 6 is the highest value then create an empty array of length highest value + 1 (6 + 1). All the values in this new array should be that which is not in our array like 0 but a more safer approach will be `null` value.

```text
A = 5, 3, 2, 3, 6, 1

new_arr = None, None, None, None, None, None, None
indexes = 0     1     2     3     4     5     6
```

This method of sorting is powerful when you've repeating values.

Now go through each and every number and do the following step

```text
We're on index 0 i.e. 5 value

A           = 5, 3, 2, 3, 6, 1
              |

Add one in the 5th position since 5 has occurred one time

new_arr     =  None, None, None, None, None,    1, None
indexes     =  0     1     2     3     4        5     6

Then go to index 1 i.e. 3 and add 1 in index 3 in new_arr


A           = 5, 3, 2, 3, 6, 1
                 |

new_arr     =  None, None, None,    1, None,    1, None
indexes     =  0     1     2        3  4        5     6


A           = 5, 3, 2, 3, 6, 1
                    |

new_arr     =  None, None, 1, 1, None, 1, None
indexes     =  0     1     2  3  4     5  6

Now since 2 is repeated then add 1 in index 3 in new_arr

A           = 5, 3, 2, 3, 6, 1
                       |

new_arr     =  None, None, 1, 2, None, 1, None
indexes     =  0     1     2  3  4     5  6

A           = 5, 3, 2, 3, 6, 1
                          |

new_arr     =  None, None, 1, 2, None, 1, 1
indexes     =  0     1     2  3  4     5  6

A           = 5, 3, 2, 3, 6, 1
                             |

new_arr     =  None, 1, 1, 2, None, 1, 1
indexes     =  0     1  2  3  4     5  6
```

Once you have iterated through the entire array, we do the below operation.

```text
A           = 5, 3, 2, 3, 6, 1
new_arr     =  None, 1, 1, 2, None, 1, 1
indexes     =  0     1  2  3  4     5  6

Since 0 doesn't exists, move to index 1 in new_arr. Here 1 exists one time (count from new_arr) in original arr therefore replace 5 with 1.

A           = 1, 3, 2, 3, 6, 1
new_arr     =  None, 1, 1, 2, None, 1, 1
indexes     =  0     1  2  3  4     5  6

Count for 2 is one therefore replace 1 position value to 2

A           = 1, 2, 2, 3, 6, 1
new_arr     =  None, 1, 1, 2, None, 1, 1
indexes     =  0     1  2  3  4     5  6

Now since count for 3 is 2 therefore replace 2 position with 3

A           = 1, 2, 3, 3, 6, 1
new_arr     =  None, 1, 1, 2, None, 1, 1
indexes     =  0     1  2  3  4     5  6

A           = 1, 2, 3, 3, 5, 1
new_arr     =  None, 1, 1, 2, None, 1, 1
indexes     =  0     1  2  3  4     5  6

A           = 1, 2, 3, 3, 5, 6
new_arr     =  None, 1, 1, 2, None, 1, 1
indexes     =  0     1  2  3  4     5  6
```

Now the original array is sorted.

It is one of the efficient algorithm. Even if we're iterating a lot the time complexity for this is not like O(n^2) or O(n^3) since each loop is independent of the other.
