
def encrypt(text,shift):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    crypted_text = ""
    j=0
    for i in range(0,len(text)):
        
        while(text[i]!=letters[j]):
            j+=1

        if(j+shift <= 26):
            crypted_text = crypted_text + letters[(j%25)+shift]  
        else:
            crypted_text = crypted_text + letters[(j%25)+shift-1] 
        j=0
    print("Crypted text: " + crypted_text)







text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
encrypt(text,shift)