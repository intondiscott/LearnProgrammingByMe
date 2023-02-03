def main() -> any:
    # here we are going to learn about dictoionaries
    #dictionaries hold keys and values
    person = {
        'name': 'Jane',
        'age': 23,
        'gender': 'female'
    }
    # here we will print the information in the dictionary we made of person
    print(person)
    # notice how there are  keys(left side of colon) and a values(right side of colon) in each section of our person
    # let's say we want to just get part of the person for use in our program, how would we do that?
    print(person['name'])
    print(person['age'])
    print(person['gender'])
    # we can also set this information in a varible
    name = person['name']
    age = person['age']
    gender = person['gender']
    print(name)
    print(age)
    print(gender)
    # more advance way and something you will learn in the future
    name,age,gender = [val for val in person.values()]
    print(name,age,gender)



if __name__ == "__main__":
    print("Welcome to your second lesson into programming")
    main()