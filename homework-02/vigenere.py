def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """Encrypts plaintext using a Vigenere cipher."""
    ciphertext = list(plaintext)

    shift = list(keyword.casefold())
    equalizer = ord('a')
    for i in range(len(shift)):
        shift[i] = ord(shift[i]) - equalizer
    
    count = 0
    for i in range(len(ciphertext)):
        code = ord(ciphertext[i])

        if code in range(65, 91):
            code += shift[count]
            if (code > 90):
                code -= (shift[count] // 26) * 26 + 26
            ciphertext[i] = chr(code)

        if code in range(97, 123):
            code += shift[count]
            if (code > 122):
                code -= (shift[count] // 26) * 26 + 26
            ciphertext[i] = chr(code)
        if count == (len(shift) - 1):
            count = 0
        else:
            count += 1
    return ''.join(ciphertext)

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """Decrypts a ciphertext using a Vigenere cipher."""
    plaintext = list(ciphertext)

    shift = list(keyword.casefold())
    equalizer = ord('a')
    for i in range(len(shift)):
        shift[i] = ord(shift[i]) - equalizer
    
    count = 0
    for i in range(len(plaintext)):
        code = ord(plaintext[i])

        if code in range(65, 91):
            code -= shift[count]
            if (code < 65):
                code += (shift[count] // 26) * 26 + 26
            plaintext[i] = chr(code)

        if code in range(97, 123):
            code -= shift[count]
            if (code < 97):
                code += (shift[count] // 26) * 26 + 26
            plaintext[i] = chr(code)
        if count == (len(shift) - 1):
            count = 0
        else:
            count += 1
    return ''.join(plaintext)