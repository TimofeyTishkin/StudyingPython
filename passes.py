from random import *


digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
chars = ""
print("What is the amount of passwords we need to create?")
amount = input()
while not amount.isdigit():
    print("That is not a number. Try to type again.")
amount = int(amount)
print("What is the length of a password?")
length = input()
while not length.isdigit():
    print("That is not a number. Try to type again.")
length = int(length)
remove_some_cases = False
print("Need numbers?")
will_di = input()
if will_di.upper() == "YES":
    will_di = True
else:
    will_di = False
print("Need uppercase letters?")
will_upp_let = input()
if will_upp_let.upper() == "YES":
    will_upp_let = True
else:
    will_upp_let = False
print("Need lowercase letters?")
will_low_let = input()
if will_low_let.upper() == "YES":
    will_low_let = True
else:
    will_low_let = False
print("Need punctuations")
will_punc = input()
if will_punc.upper() == "YES":
    will_punc = True
else:
    will_punc = False
print("Remove unclear cases like: il1Lo0O?")
remove_some_cases = input()
if remove_some_cases.upper() == "YES":
    remove_some_cases = True
else:
    remove_some_cases = False
if will_di:
    chars += digits
if will_punc:
    chars += punctuation
if will_low_let:
    chars += lowercase_letters
if will_upp_let:
    chars += uppercase_letters


def generate_password(le, abc):
    pas = ""
    for _ in range(le):
        pas += choice(abc)
    return pas


for i in range(amount):
    print(generate_password(length, chars))

