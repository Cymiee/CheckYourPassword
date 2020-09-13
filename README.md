# CheckYourPassword
Check if your password has been leaked on a public online database of 500m+ passwords

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
