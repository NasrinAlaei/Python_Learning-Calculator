# Simple Calculator


In this section, the tutorial on making a calculator with Python is presented in simple language.

we write a function called calculate() to create a simple command line calculator, and then we run the program by calling the function.

The first step, two numbers are received as input from the user. To do this, you can use Python's built-in function, input(). The input() function receives data as a string.
Based on the requirements of the calculator project with Python, the string received from the input () function can be converted either with an integer type (Integer) or a floating point type (Float).

After we receive two numbers from the user, we need to determine what operation the user wants to perform on the numbers for calculation and math operations. For this reason, we get the desired operator again with the input() command.

After receiving the user's numbers and operator, we must perform the user's requested mathematical operation on the numbers according to the input operator and using if, elif and else.

We want to make sure that when the program runs, we don't terminate it after finding the answer, so we add another function that asks the user whether to continue or terminate the program. We add this function at the end of the first function and before calling calculate(). In this function, we first ask the user to continue the execution by receiving yes and no. Then, according to the user's response, we continue, stop or repeat the program.
