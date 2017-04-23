#Nama   :   Fintanto Cendikia
#NRP    :   5114100098
#Kelas  :   KIJ-A
import string
import random
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def encrypt(text):
    tes = text_to_bits(text)
    xor = int(tes,2) ^ int(k0,2)
    addmod = (xor + int(k1,2)) % mod
    result = get_bin(addmod)
    return result

def decrypt(ciphertext):
    negasi = -int(k1, 2)
    addmod2 = (int(ciphertext, 2) + negasi) % mod
    tryxor2 = addmod2 ^ int(k0, 2)
    result = get_bin(tryxor2)
    return result


def take_input_and_enc(text):
    panjang = text.__len__()
    #print(panjang)
    diff = 8 - (panjang % 8)
    if (diff != 8):
        panjang = panjang + diff
        while (diff > 0):
            text += " "
            diff -= 1

    x = 0

    ciphertext = ""
    #print(len(text))
    while (x <= len(text)):
        comp = ""
        toenc = text[x:x+8]
        temp = encrypt(toenc)
        for j in range(0, 64 - len(temp)):
            comp += "0"
        comp += temp
        ciphertext = ciphertext + comp
        x += 8


    return ciphertext

def fix_missing_bits_and_decrypt(ciphertext):
    plaintext = ""
    decrypted = ""

    x=0
    y=64
    while(y<=ciphertext.__len__()):
        toenc = ciphertext[x:y]
        temp = decrypt(toenc)
        decrypted+=temp
        temp = text_from_bits(temp)
        plaintext+=temp
        x+=64
        y+=64
    print("Hasil decrypt = " + decrypted)
    return plaintext
def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

mod = pow(2,64)
get_bin = lambda x: format(x, 'b')

key = id_generator()
key = text_to_bits(key)
print("Random key = " + key)

k0 = key[0:64]
k1 = key[64:128]
print("K0 = " + k0)
print("K1 = " + k1)
text = input("Masukkan text : ")
ciphertext = take_input_and_enc(text)

print("Hasil encrypt = " + ciphertext)


plaintext = fix_missing_bits_and_decrypt(ciphertext)
print("Plaintext = " + plaintext)
