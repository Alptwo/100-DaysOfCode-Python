from cgitb import text

def encrypt(text,shift):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    crypted_text = ""

    for i in range(0,len(text)):
        if(len(text)+shift <= 26):
            text[i] = letters[i + shift]
        else:
            i%26
        







text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
encrypt(text,shift)