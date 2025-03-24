# Stack

A stack is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out).

## When & where to use?

- Used by undo mechanisms in text editors
- Used in compiler syntax checking for matching brackets and braces
- Can be used to model a pile of books and plates
- Used behind the scenes to support recursion by keeping track of previous function calls
- Can be used to do a Depth First Search (DFS) on a graph

## Time complexity

| Operations | Complexity |
| ---------- | ---------- |
| Pushing    | O(1)       |
| Popping    | O(1)       |
| Peeking    | O(1)       |
| Searching  | O(n)       |
| Size       | O(1)       |

## Example

Problem - Given a string made up of the following brackets: ()[]{}, determine whether the brackets properly match

```text
[{}]     --> Valid
(()())   --> Valid
{]       --> Invalid
[()]))() --> Invalid
[]{}({}) --> Valid
```

```text
Algorithm:
    Let S be a stack
    For bracket in bracket_strings:
        rev = getReversedBracket(bracket)
        If isLeftBracket(bracket):
            S.push(bracket)
        Else If S.isEmpty() or S.pop() != rev:
            return false //Invalid
    return S.isEmpty() //Valid if S is empty
```
