def main():
    """
    Here we will learn about making functions in python and how they organise our code
    we will also learn how to pass info into functions that are called parameters
    """

    # functions are made by putting def before our naming of a function
    def first_function():
        print('i am a function...')

    # functions can return info passed to them through its parameters
    def make_a_word(word: str) -> str:
        """
        :param word:
        :return:
        a string value
        """
        return word

    def add_two_nums(num1: int, num2: int) -> int:
        """

        :param num1:
        :param num2:
        :return:
        return the sum of two numbers
        """
        return num1 + num2

    # in order for a function to work we must call it like so
    first_function()
    print(make_a_word("Hello World"))
    print(f"the sum of num1 and num2 is {add_two_nums(23, 44)}")


if __name__ == "__main__":
    print("welcome to lesson number 4...")
    main()
