
def translate(numb, b):
    numb = str(numb)
    dig = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = 0
    for i in range(len(numb)):
        ans += int(dig.index(numb[i])) * b ** (len(numb) - i - 1)
    return ans


def de_translate(numb, b):
    dig = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = ""
    while numb >= b:
        ans += str(dig[numb % b])
        numb //= b
    ans += str(dig[numb])
    return ans[::-1]


print(translate("127", 16))

''' for i in range(9, 32):
    print("{}+{}+{}+{}={}".format(translate(32, i), translate(22, i), translate(16, i), translate(17, i),
                                  translate(88, i)))
    if translate(32, i)+translate(22, i)+translate(16, i)+translate(17, i) == translate(88, i):
        print("YES", i)
'''