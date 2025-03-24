# Infix Postfix Prefix

In the context of arithmetic expressions, infix, prefix, and postfix are three different but equivalent notations.

## Infix

An infix expression is a single letter, or an operator, proceeded by one infix string and followed by another infix string.

```text
A
A + B
(A + B) + (C – D)
```

## Prefix

A prefix expression is a single letter, or an operator, followed by two prefix strings. Every prefix string longer than a single variable contains an operator, first operand and second operand.

```text
A
+ A B
+ + A B – C D
```

## Postfix

A postfix expression (also called Reverse Polish Notation) is a single letter or an operator, preceded by two postfix strings. Every postfix string longer than a single variable contains first and second operands followed by an operator.

```text
A
A B +
A B + C D –
```

## Notes

Prefix and Postfix notations are methods of writing mathematical expressions without parenthesis.

Time to evaluate a postfix and prefix expression is O(n), where n is the number of elements in the array.

## Example

| INFIX            | PREFIX         | POSTFIX        |
| ---------------- | -------------- | -------------- |
| A + B            | + A B          | A B +          |
| A + B – C        | – + A B C      | A B + C –      |
| (A + B) \* C – D | – \* + A B C D | A B + C \* D – |
