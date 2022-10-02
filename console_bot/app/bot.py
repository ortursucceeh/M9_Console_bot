contacts = {}

EXIT_WORDS = ["exit", "close", "good bye", "end"]


def input_error(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                func(*args, **kwargs)
                break
            except Exception:
                print("Incorrect input data.")
    return wrapper


@input_error
def add_contact():

    name, number = input("Enter name and number: ").split()
    if name in contacts:
        print("The contact with name '{name}' is already exists.")
    else:
        contacts[name] = number
        print(f"Contact {name} added.")


@input_error
def find_contact():

    name = input("Enter name: ")

    if name in contacts:
        print(f"{name}'s number: {contacts[name]}")
    else:
        print(f"Contact with name '{name}' doesn't exists.")


@input_error
def change_contact():

    name, number = input("Enter name and number: ").split()
    if name in contacts:
        print(
            f"The {name}'s number will be changed from {contacts[name]} to {number}")
        contacts[name] = number
    else:
        print(f"Contact with name '{name}' doesn't exists.")


@input_error
def show_all_contacts():
    print()
    if contacts:
        a = len(max(contacts.keys(), key=len))
        b = len(max(contacts.values(), key=len))
        print("All contacts:")
        print((a + b + 6) * "-")
        [print(f"{key} --->  {value}") for key, value in contacts.items()]
        print((a + b + 6) * "-")
    else:
        print("You don't have any contacts.")


@input_error
def remove_contact():

    name = input("Enter name: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} was removed.")
    else:
        print(f"Contact with name '{name}' doesn't exists.")


@input_error
def show_all_commands():
    print(*handler.keys(), sep=" # ")


handler = {
    "hello": lambda: print("Hello! How can I help you?"),
    "add": add_contact,
    "change": change_contact,
    "phone": find_contact,
    "show": show_all_contacts,
    "remove": remove_contact,
    "commands": show_all_commands
}


def main():
    while True:
        command = input("Enter command: ").lower().strip()
        if command in EXIT_WORDS:
            print("See ya!")
            exit()

        elif command in handler:
            handler[command]()
        else:
            print("Incorrect command. (To see all commands enter 'commands')")


if __name__ == "__main__":
    main()
