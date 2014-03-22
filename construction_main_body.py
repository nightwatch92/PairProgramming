lists_name = []

def parse_command(command):
    return tuple(command.split(" "))


def is_command(command_tuple, command_string):
    return command_tuple[0] == command_string


def create_help():
    help = ["Here is a full list of commands:",
            "\t* \033[1mshow_lists \033[0m- Prints all lists to the screen. Each list is assigned with a unique identifier",
            "\t* \033[1mshow_list \033[0m<unique_list_identifier> - Prints all people, one person at a line, that are subscribed for the list. The format is: <Name> - <Email>",
            "\t* \033[1madd \033[0m<unique_list_identifier> - Starts the procedure for adding a person to a mail list. The program prompts for name and email.",
            "\t* \033[1mcreate \033[0m <list_name> - Creates a new empty list, with the given name.",
            "\t* \033[1msearch_email \033[0m<email> - Performs a search into all lists to see if the given email is present. Shows all lists, where the email was found.",
            "\t* \033[1mmerge_lists \033[0m<list_identifier_1> <list_identifier_2> <new_list_name> - merges list1 and list2 into a new list, with the given name.",
            "\t* \033[1mexport \033[0m<unique_list_identifier> - Exports the given list into JSON file, named just like the list. All white spaces are replaced by underscores.",
            "\t* \033[1mexit \033[0m- this will quit the program"]

    return "\n".join(help)

def print_all_groups(lists_name):
    a = 0
    for lists in lists_name:
        a = a + 1
        

def get_group():
    pass

def add_new_contact():
    pass

def create_new_group(command):
    global lists_name
    current_list = ' '.join(command[1:])
    lists_name.append(current_list)
    return "New list <" + current_list + "> was created"

def merge_lists():
    pass

def export_to_json():
    pass

def main():

    while True:
        command = parse_command(input("Enter command>"))

        if is_command(command, "help"):
            print(create_help())
        elif is_command(command, "show_lists"):
            print_all_groups(lists_name)
        elif is_command(command, "show_list"):
            print(get_group())
        elif is_command(command, "add"):
            add_new_contact()
        elif is_command(command, "create"):
            print(create_new_group(command))
        elif is_command(command, "merge_lists"):
            merge_lists()
        elif is_command(command, "export"):
            export_to_json()
        elif is_command(command, "exit"):
            break

if __name__ == '__main__':
    main()
