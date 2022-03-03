
def encrypt(text,shift):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    encrypted_text = ""
    j=0
    for i in range(0,len(text)):
        
        while(text[i]!=letters[j]):
            j+=1

        if(j+shift <= 26):
            encrypted_text = encrypted_text + letters[(j%25)+shift]  
        else:
            encrypted_text = encrypted_text + letters[(j%25)+shift-1] 
        j=0
    return encrypted_text

def decrypt(encrypted_text,shift):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    decrypted_text = ""
    j=0
    for i in range(0,len(encrypted_text)):

        while(encrypted_text[i]!=letters[j]):
            j+=1
        
        if(j-shift >= 0):
            decrypted_text = decrypted_text + letters[(j%25)-shift]
        else:
            decrypted_text = decrypted_text + letters[(j+26)-shift]
        j=0

    return decrypted_text
            


text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
print(encrypt(text,shift))

crypted_text = input("Type your crypted message:\n").lower()
shift = int(input("Type the shift number:\n"))
print(decrypt(crypted_text,shift))

