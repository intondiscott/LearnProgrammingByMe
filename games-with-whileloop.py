import datetime
import time

locked_out = True
in_use = True
password = str(datetime.date.today())  # use the date today for password (YYYY-MM-DD)


def guess_password(access: str) -> str:
    global password
    print(password)
    if access == password:
        return "Access Granted..."
    else:
        return "Access Denied"


def tasks(working):
    commands = input("What do you want to do? options are (quit,check emails, browse internet)... ").lower()
    if commands == 'quit':
        print("quiting program...")
        time.sleep(3)
        working = False
    elif commands == "check emails":
        print("Checking emails...")
        time.sleep(3)
        print("No emails found...")
    elif commands == "browse internet":
        print("Browsing the internet...")
        time.sleep(3)
        print("404 error...")
    return working


def main():
    global locked_out, in_use

    while locked_out:
        guess = guess_password(str(input("enter password...")))
        print(guess)
        if guess == "Access Granted...":
            locked_out = False

    while in_use:
        in_use = tasks(in_use)


if __name__ == "__main__":
    main()
