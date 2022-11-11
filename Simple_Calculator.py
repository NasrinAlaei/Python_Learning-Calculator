# Define our function
def calculate():
    try:
        num1 = float(input("Please Enter Num1: "))
        num2 = float(input("Please Enter Num2: "))
        operator = input("'''"
                         "Please type in the math operation you would like to complete:\n"
                         "+ for addition\n"
                         "- for subtraction\n"
                         "* for multiplication\n"
                         "/ for division\n"
                         "'''")

        if operator == '+':
            output = num1 + num2
            print(f"Result: {num1} + { num2} = {output}")
        elif operator == '-':
            output = num1 - num2
            print(f"Result: {num1} - {num2} = {output}")
        elif operator == '*':
            output = num1 * num2
            print(f"Result: {num1} * {num2} == {output}")
        elif operator == '/':
            try:
                output = num1 / num2
                print(f"Result: {num1} / {num2} = {output}")
            except ZeroDivisionError:
                print("Result: Can Nat Divide By Zero")
        else:
            egainRun()
        egainRun()
    except ValueError:
        print("value error!!\n You have not typed a valid operator, please run the program again.")
        egainRun()

# Define again() function to ask user if they want to use the calculator again
def egainRun():
    n = input("'''Do you want to calculate again?"
              "Please type Y for YES or N for NO.'''")

    # If user types Y, run the calculate() function
    if n.upper() == 'Y':
        calculate()
        egainRun()

    # If user types N, end the program
    elif n.upper() == 'N':
        print("Exit...")

    # If user types another key, run the function again
    else:
        egainRun()


# Call calculate() outside of the function
calculate()











