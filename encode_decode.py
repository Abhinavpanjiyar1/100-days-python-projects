alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=input("type 'encode' to encrypt, type 'decode' to decrypt:\n" )
text= input('enter your message:\n')
shift=int(input("type your shift number:\n"))
shift = shift%26
def encrypt(plain_text, shift_number):
    cipher_text = ""
    for letter in plain_text:
       position= alphabet.index(letter)
       new =position + shift_number
       new_letter=alphabet[new]
       cipher_text+=new_letter
    print(f"the encode text is {cipher_text}")
   

def decrypt(cipher_text, shift_number):
    plain_text=""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new=position-shift_number
        new_letter=alphabet[new]
        plain_text+= new_letter
    print(f"the decrypt text is {plain_text}")  
if direction=="encode":
    encrypt(plain_text=text, shift_number=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_number =shift)