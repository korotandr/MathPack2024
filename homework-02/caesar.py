import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """Encrypts plaintext using a Caesar cipher."""
    ciphertext = list(plaintext)

    for i in range(len(ciphertext)):
        code = ord(ciphertext[i])
        if code in range(65, 91):
            code += shift
            if (code > 90):
                code -= (shift // 26) * 26 + 26
            ciphertext[i] = chr(code)

        if code in range(97, 123):
            code += shift
            if (code > 122):
                code -= (shift // 26) * 26 + 26
            ciphertext[i] = chr(code)

    return ''.join(ciphertext)

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """ Decrypts a ciphertext using a Caesar cipher."""
    plaintext = list(ciphertext)

    for i in range(len(plaintext)):
        code = ord(ciphertext[i])
        if code in range(65, 91):
            code -= shift
            if (code < 65):
                code += (shift // 26) * 26 + 26
            plaintext[i] = chr(code)

        if code in range(97, 123):
            code -= shift
            if (code < 97):
                code += (shift // 26) * 26 + 26
            plaintext[i] = chr(code)

    return ''.join(plaintext)

def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """Brute force breaking a Caesar cipher."""
    best_shift = 0
    while True:
        estimated = decrypt_caesar(ciphertext, best_shift)
        if estimated in dictionary:
            break
        best_shift += 1

    return best_shift