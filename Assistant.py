phone_book = {}

def parse_command(string):
    parts = string.split()
    command = parts[0]
    args = parts[1:]
    return command, args

def handle_hello(args):
    return "How can I help you?"

def handle_add(args):
    if len(args) < 2:
        raise ValueError("Please provide a name and phone number.")
    name = args[0]
    phone_number = " ".join(args[1:])
    phone_book[name] = phone_number
    return "Contact added successfully."

def handle_change(args):
    if len(args) < 2:
        raise ValueError("Please provide a name and new phone number.")
    name = args[0]
    if name not in phone_book:
        raise KeyError(f"No contact found with the name '{name}'.")
    phone_number = " ".join(args[1:])
    phone_book[name] = phone_number
    return "Phone number updated successfully."

def handle_phone(args):
    if len(args) < 1:
        raise ValueError("Please provide a name to retrieve the phone number.")
    name = args[0]
    if name not in phone_book:
        raise KeyError(f"No contact found with the name '{name}'.")
    return f"The phone number for {name} is {phone_book[name]}."

def handle_show_all(a):
    if len(phone_book) == 0:
        return "The phone book is empty."
    contacts = "\n".join([f"{name}: {phone}" for name, phone in phone_book.items()])
    return f"Phone book contacts:\n{contacts}"

def handle_close(a):
    return "Good bye!"

command_list = {
    "hello": handle_hello,
    "hi": handle_hello,
    "add": handle_add,
    "change": handle_change,
    "phone": handle_phone,
    "show_all": handle_show_all,
    "close": handle_close,
    "good bye": handle_close,
    "exit": handle_close
}

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f"No contact found: {str(e)}"
        except ValueError as e:
            return f"Invalid input: {str(e)}"
        except IndexError as e:
            return f"Invalid input: {str(e)}"
    return wrapper

@input_error
def handle_command(command, args):
    if command in command_list:
        return command_list[command](args)
    else:
        raise ValueError("Invalid command.")

def main():
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_command(user_input)
        if command.lower() in ["good bye", "close", "exit"]:
            print(handle_command("close", []))
            break
        else:
            print(handle_command(command.lower(), args))

if __name__ == "__main__":
    main()
