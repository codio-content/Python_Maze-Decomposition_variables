The final string example shows a slightly different **use case**.

|||definition
## Use Case
A *use case* is a specific situation or example.
|||

On the left, you can see that we have 2 variables.

- `number = 10`
- `string = '100'`

So, what happens if we add these together using variable arithmetic?

Javascript will look at both variables and if one of them is a string, it will use string arithmetic and not number arithmetic.

Look at the message below the maze. The result is `10100` and **not** `110`.

## Experiment
Try changing `string` to be just `100` rather than `'100'`. What do you think will happen. And why does it happen?

Play around with different combinations of numbers and strings and see what happens.
