

def code(stp, txt, l1):
    ll = 0
    if l1 == "ру":
        ll = 32
    else:
        ll = 26
    ans = ""
    for i in txt:
        order = ord("A")
        if l1 == "ру":
            if i.islower():
                order = ord("а")
            else:
                order = ord("А")
        if i.islower() and l1 == "en":
            order = ord("a")
        if not i.isalpha():
            ans += i
            continue
        if not ord(i)+stp-order >= ll:
            ans += chr(ord(i)+stp)
        else:
            ans += chr(ord(i)+stp-ll)
    return ans


def decode(stp, txt, l1):
    ll = 0
    if l1 == "ру":
        ll = 32
    else:
        ll = 26
    ans = ""
    for i in txt:
        order = ord("A")
        if l1 == "ру":
            if i.islower():
                order = ord("а")
            else:
                order = ord("А")
        if i.islower() and l1 == "en":
            order = ord("a")
        if not i.isalpha():
            ans += i
            continue
        if not ord(i)-stp-order < 0:
            ans += chr(ord(i)-stp)
        else:
            ans += chr(ord(i)-stp+ll)
    return ans


print("What do we need to do?")
print("1. Code")
print("2. Decode")
co_deco = int(input())
# I will only use english because it's the same thing, and I don't mind
print("What's a step?")
step = int(input())
print("What's the language?('en'/'ру')")
lan = input().lower()
print("What do you want to code/decode?")
text = input()
if co_deco == 1:
    print(code(step, text, lan))
else:
    print(decode(step, text, lan))

for i in range(26):
    print(decode(i+1, "Hawnj pk swhg xabkna ukq nqj.", "en"))
