word = input()

def detect(word):
    glasnie = ["a", "u", "e", "o", "y", "i"]
    soglasnie = ["j", "s", "b", "k", "t", "c", "l", "d", "v", "m", "n", "w", "f", "x", "g", "p", "h", "q", "z", "r"]
    l = len(word)
    for i in range(0, l):
        if word[i] in glasnie:
            print("Uhhh")
        elif word[i] in soglasnie:
            print("Umm")
        else:
            quit()
detect(word)
