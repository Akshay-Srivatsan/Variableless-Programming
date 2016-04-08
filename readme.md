# Variableless Programming
## Overview:
A programming language which doesn't have any user-definable variables. You have two stacks to store your data and code (a main stack and a data stack). The data stack is local to each "block" of code, while the main stack is global.

## Operations:
Note: "the stack" refers to the main stack.
* `exit`: terminates the program
* `{ [...] }`: defines a block of code, which will be pushed onto the stack without being evaluated
* `call`: evaluates a block of code on the top of the stack
* `return`: returns the value at the top of the stack
* `return if`: evaluates the top value of the stack, and returns the value under it if the top value was the boolean True. Otherwise, discards both values.
* `push`: pops a value from the main stack and pushes it onto the data stack
* `pop`: pops a value from the data stack and pushes it onto the main stack
* `duplicate`: creates a copy of the value at the top of the stack, and pushes the copy onto the top of the stack
* `swap`: switches the first and second elements on the stack
* `less`: compares the top two elements on the stack, pushing True if the first is less than the second and pushing False otherwise. The two original elements are discarded.
* `greater`: compares the top two elements on the stack, pushing True if the first is greater than the second and pushing False otherwise. The two original elements are discarded.
* `discard`: pops a value from the main stack, but doesn't store it anywhere
* `add`: adds the top two values on the stack and push the result onto the stack
* `negate`: replaces the top value on the stack with its additive inverse
* `print`: writes the top value on the stack to stdout. The value is then discarded.
