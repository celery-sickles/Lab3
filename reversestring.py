def reverseString(str):
    newStr = ""
    for char in range(len(str)-1, -1, -1):
        newStr += str[char]
    return newStr

print(reverseString("hello world"))