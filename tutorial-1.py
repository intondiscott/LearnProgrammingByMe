def main() -> any:
    # first program to write as a passage into programming
    print("Hello World")
    """
    In this lesson we will be learning variables and how to use them to make changes in programs easier
    the purpose of varibles is to give readability to our program so as to not get lost in what is being done
    """

    """
    making your first variable 
    in python you must give a value to a varible so there is no errors
    varibles should be named in a way that makes sense (e.g., if you were making a number, then number varible 
    would be appropiate) variables should be in snake case when there is more than one word in thge variable 
    (e.g., first_second)
    """
    number = 0
    word = "Hello World"
    floating_number = 3.8
    variable_that_has_been_declared = word
    isTrue = False

    print(number)
    print(word)
    print(floating_number)
    print(variable_that_has_been_declared)
    print(isTrue)

    """
    One thing to note is that when you are creating varibles, that you understand the type it is you are creating
    such as making a string(series of letters) varible, a integer(whole number) varible, a float(decimal point) variable
    or a boolean(True/False) variable
    using the method (type()) will give you the type of variable that has been declared 
    """

    print(type(number))
    print(type(word))
    print(type(floating_number))
    print(type(variable_that_has_been_declared))
    print(type(isTrue))

if __name__ == "__main__":
    print("Welcome to your first lesson...")
    main()