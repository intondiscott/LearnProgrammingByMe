def main():
    """
    In this lesson we will learn about loops and how it can make our programming easier
    Two common loops in programming you will be learning is while loops and for loops
    """

    # while loop is a loop that does something until the condition is met
    condition = 9
    do_something = "I am doing something"
    completed = "finally out of loop :D"
    while int(f'{condition}') >= 0:
        print(f'{do_something} {10 - condition} times...')
        condition -= 1
    print(completed)

    # for loop is a loop you want to do something a specified number of times
    num_of_times = 10
    for idx in range(num_of_times):
        print(f'{do_something} {idx} times...')

    # let's do some loops with dictionaries
    family = {
        'grandparents':
            [
                {
                    'name': 'Bobby',
                    'age': 60

                },
                {
                    'name': 'Sally',
                    'age': 59
                }
            ],
        'kids':
            [
                {
                    'name': 'Scotty',
                    'age': 36
                },
                {
                    'name': 'Lisa',
                    'age': 35
                }
            ]
    }

    for person in family:
        for idx in range(len(family[person])):
            print(f"name of {person}: {family[person][idx]['name']}, age: {family[person][idx]['age']}")


if __name__ == "__main__":
    print("welcome to lesson number 3...")
    main()
