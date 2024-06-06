import src.Caesar as Caesar

# パラメータ
key = 10  # 1 - 26 の範囲で指定


def encrypt(text, key):
    vector = key
    result = ""
    for c in text:
        # Caesar暗号化を適用した後にXOR操作を行う
        caesar_encrypted_char = Caesar.encrypt(c, key)
        temp = chr(ord(caesar_encrypted_char) ^ vector)
        result += temp
        vector = ord(temp)
    return result


def decrypt(text, key):
    vector = key
    result = ""
    for c in text:
        # XOR操作を行った後にCaesar復号を適用する
        temp = chr(ord(c) ^ vector)
        caesar_decrypted_char = Caesar.decrypt(temp, key)
        result += caesar_decrypted_char
        vector = ord(c)
    return result


if __name__ == "__main__":
    text = "HelloWorld"
    print("Text  : " + text)
    print("Key   : " + str(key))
    cipher = encrypt(text, key)
    print("Cipher: " + cipher)
    decrypted_text = decrypt(cipher, key)
    print("Decrypted Text: " + decrypted_text)
