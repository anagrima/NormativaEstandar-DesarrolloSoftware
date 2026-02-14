import string
from UC3MMoney import TransactionManager

#GLOBAL VARIABLES
LETTERS = string.ascii_letters + string.punctuation + string.digits
SHIFT = 3

def Encode(word):
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (LETTERS.index(letter) + SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[x]
    return encoded

def Decode(word):
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (LETTERS.index(letter) - SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[x]
    return encoded


def Main():
    mng = TransactionManager()
    res = mng.ReadProductCodeFromJson("test.json")
    str_res = str(res)
    print(str_res)
    encode_res = Encode(str_res)
    print("Encoded Res "+ encode_res)
    decode_res = Decode(encode_res)
    print("Decoded Res: " + decode_res)
    print("IBAN_FROM: " + res.IbanFrom)
    print("IBAN_TO: " + res.IbanTo)

if __name__ == "__main__":
    Main()
