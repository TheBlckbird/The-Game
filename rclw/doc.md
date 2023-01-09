# RCLW Documentation

## All commands:

`SET test_variable Hello World` sets the `test_variable` to `Hello World`

reference variables by writing them in two curly brackets like this: `{{variable}}`

`OUT text`: prints "text"  

`input test_variable What is your name?`: creates an input with the prompt `What is your name?` and saves the result into the variable `test_variable`

`// comment`: just a comment (must be at the start of the line)

`QUIT` or `EXIT`: quits the program

`PY print("Hello World")`: executes the python code (only that line)

`IF arg1 == arg2 t waypoint` compares arg1 and arg2 and then does t.  
Possible operators are: == and eq: equal and != and noteq: not equal  
possible things:
- t wp: jumps to waypoint `wp`
- r: when coming from a waypoint: jumps back to line after jump to waypoint
- c 3: jumps to line 3

`AT wp` defines waypoint `wp`  
`TO wp`: jumps to waypoint `wp`  
`RET`: when coming from waypoint: jumps back to line after jump to waypoint  
`CURSOR 3`: jumps to line 3

`RAND test_variable 0 100`: sets the variable `test_variable` to a random integer between 0 and 100

`MATH test_variable add 10 20`: does the operation with the two numbers and saves it in the variable `test_variable`  
- add: adds the two numbers together
- sub: substracts the second number from the first one
- mul: multiplies the two numbers
- div: divides the second number by the first one
- mod: uses module like: first_number mod second_number
- pow: multiplies the first number as many times by itself as the second number big is
- sqrt: creates the sqrt of the first number (second will be ignored)

`WAIT 10`: Waits for a certain amount of seconds

`CLEAR_TERM`: clears the terminal

## Other
for-loop: 
```
set counter 0

AT loop
    math counter add {{counter}} 1
    out {{counter}}
    if {{counter}} == 10 t after_loop
    TO loop

AT after_loop
```