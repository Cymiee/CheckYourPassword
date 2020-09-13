import urllib.request
import hashlib

about_str = r'''
This program checks if your password is anywhere in a public database of over half a billion passwords.
The program never sends out your full password in plain text into the internet, instead, this program uses a k-Anonymity
model by only sending the first five characters of your password's SHA-1 hash out to the pwnedpasswords API
to check if your password could possibly appear in the database, then manually goes through the remaining results to 
make sure.

This program was made using Python3 and built-in libraries-:
urllib
hashlib

api.pwnedpasswords/range was used to get the passwords
Pycharm was used as an IDE.

You are allowed to use, read, modify and redistribute this code.
'''

commands_str = r'''
Use / followed by the command name to use the command.

help-: Shows the commands, and the about page
commands-: Shows the commands
about-: Shows the about page
exit-: Exits the program

If your password starts with a slash,
use ` followed by your password to send it out as a raw password.
You can also press enter to exit the program.
'''


def get_data(pre_hash):
    return str(urllib.request.urlopen("https://api.pwnedpasswords.com/range/" + pre_hash).read().decode("utf-8"))


def process_data(data_string):
    unprocessed_list = data_string.splitlines()
    processed_list = []
    for item in unprocessed_list:
        item_separated = item.split(":")
        item_separated[1] = int(item_separated[1])
        processed_list.append(item_separated)
    return processed_list


def check_for_password(password):
    digest = hashlib.sha1(password.encode("utf-8")).hexdigest()
    digest_start = digest[0:5]
    data = get_data(digest_start)
    processed_data = process_data(data)
    for item in processed_data:
        if digest_start + item[0].lower() == digest:
            item[0] = digest_start.upper() + item[0]
            return item
    return None


if __name__ == "__main__":
    print("Welcome to password checker. Type /help for more information.")
    while True:
        i = input("Enter your password:")
        if i == "":
            break
        elif i[0] == "/":
            if i == "/help":
                print(about_str, commands_str)
            elif i == "/commands":
                print(commands_str)
            elif i == "/about":
                print(about_str)
            elif i == "/exit":
                break
            else:
                print("That is not a valid command. Use ` followed by your password if it starts with  a '/'.")
        else:
            if i[0] == "`":
                i = i[1:]
            result = check_for_password(i)
            if result is None:
                print(i + " could not be found in the stolen passwords database.")
            else:
                print(f"Your password ({i}) was found in the stolen password database {result[1]} times "
                      f"with hash-: {result[0]}")
