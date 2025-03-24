# Expression Tree ADT

An Expression Tree Abstract Data Type (ADT) is a binary tree representation of an arithmetic expression. It consists of various operators (like +, -, \*, /, %) and operands, which can be single integer digits or single-letter variables. The expression is usually fully parenthesized.

In an Expression Tree, each node represents an operator or an operand. If a node represents an operator, its children represent the operands for that operator. If a node is an operand, it is a leaf node.

Here are some operations that can be performed on an Expression Tree:

Here are some operations that can be performed on an Expression Tree:

**ExpressionTree(expStr)**: This function builds an expression tree for the given expression string. It assumes the string contains a valid, fully parenthesized expression.

**evaluate(varDict)**: This function evaluates the expression tree and returns the numeric result. The values of the single-letter variables are extracted from the supplied dictionary structure. An exception is raised if there is a division by zero error or an undefined variable is used.

**toString()**: This function constructs and returns a string representation of the expression.

Expression Trees are used in compilers to parse expressions and compute their values. They can also be used to convert an expression from one notation to another (like infix to postfix).
