def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result


def decrypt(text, shift):
    result = ""
    for c in text:
        char = c
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) - shift - 97) % 26 + 97)
    return result


if __name__ == "__main__":
    text = "HelloWorld"
    shift = 3
    print("Text  : " + text)
    print("Shift : " + str(shift))
    print("Cipher: " + encrypt(text, shift))
    print("Text  : " + decrypt(encrypt(text, shift), shift))
