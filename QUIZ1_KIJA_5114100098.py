#Fintanto Cendikia
#5114100098
#KIJ-A

name = "hzcpoiimgjzizrocwplvunqdqidjoauhclirjbefyjyetwszrgamdvaktdcjaavykwsssxzccxcajihbiycilmsftluzupwnssjghufxuvshbpzvfqzuycibuweaaldjntjexqqjojlepufqphhfyvaunvaqfjuzccolwduqdhmcrxegrdoxftfiyeiyzjlamukxpnvaebecqfyrmxzpjjiygdkbsvotuekbkfrwihiausdypdbuttqsoijcufcdrvzocalnwkualflfrridxycofnaitjaqhhmhyadiflmrtwmicrxoshjnbqsievcgcbvudvfnlpafpidpkyuqqrakrkensngalnijwvanvqbqoanhcndjqqjcxrsxscfnatjcmwfvhieoayszmudubxnfvvdzlztpxbzqtoxmcoqmwitkizeazxyfjfcqyjfesmcambeqmfahzxvctdkgiukvlznzmhbbfaizsgbolcdkooqdiefswrbvldwbjwjk"
#Convert string to binary
#http://stackoverflow.com/questions/18815820/convert-string-to-binary-in-python
x = 0
y = 8
index = 0
result ="0"
teks = []
#128bitKey
angka = "01000010011000010101000011011111111111000100111001110100010001000100011010010001011110110110100010000101110100001011100100010100"
k0 = angka[0:64]
k1 = angka[64:128]
print("K = " + angka)
print("K0 = " + k0)
print("K1 = " + k1)
while(x<512) :
    text = name[x:y]
    binarytext = '0'.join(format(ord(x), 'b') for x in text)
    #print("Chars = " + binarytext)

    # xor text dengan k0
    xor = int(binarytext, 2) ^ int(k0, 2)
    xorstring = '{:b}'.format(xor)
    # print("Half encrypted = " + xorstring)
    # addition mod dengan k1
    mod = pow(2, 64)
    addmod = (xor + int(k1, 2)) % mod
    enc = '{:b}'.format(addmod)
    # hasil

    result += enc
    teks.append(enc)

    y+=8
    x+=8

print("Result =         " + result)
print(teks)
#pangkat =pow(2,127) + 9
#angka = "{0:b}".format(pangkat)

#128bit key
#angka = "01000010011000010101000011011111111111000100111001110100010001000100011010010001011110110110100010000101110100001011100100010100"

#k0 dan k1
#k0 = angka[0:64]
#k1 = angka[64:128]
#print("K = " + angka)
#print("K0 = " + k0)
#print("K1 = " + k1)

#xor text dengan k0
#xor = int(binarytext , 2)^ int(k0 , 2)
#xorstring = '{:b}'.format(xor)
#print("Half encrypted = " + xorstring)
#addition mod dengan k1
#mod = pow(2,64)
#addmod = (xor + int(k1,2))%mod
#enc = '{:b}'.format(addmod)
#hasil
#print("Result =         " + enc)


#decrypt
x=0
text = ""
plaintext = ""
batas = len(result)
print(len(result))
while(x<64):
    text = teks[x]
    c = int(k1, 2) - 1
    d = ~c
    #print(d)
    addmoddecrypt = (int(text, 2) + d) % mod
    add = '{:b}'.format(addmoddecrypt)
    # xor
    xordecrypt = addmoddecrypt ^ int(k0, 2)
    hasil = '{:b}'.format(xordecrypt)
        # hasil
    print(end="Hasil decrypt block ")
    print(x+1)
    #print(hasil)

    bits = "0" + hasil
    print(bits)
    n = int(bits, 2)
    karakter = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    print(karakter)

    plaintext += karakter

    y+=64
    x+=1
    batas-=63

print("Plaintext = " + plaintext)