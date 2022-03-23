from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password_clicked():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

 
    password_letters = [choice(letters) for _ in range(8, 10)]
    password_symbols = [choice(symbols) for _ in range(2, 4)]
    password_numbers = [choice(symbols) for _ in range(2, 4)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button_clicked():
    website = str(website_entry.get())
    e_mail = str(email_entry.get())
    password = str(password_entry.get())
    password_file = open("password_manager/passwords.txt", "a+")
    
    if(website == "" or password == "" or e_mail == ""):
        messagebox.showinfo(title = "Error", message = "All of the entries must contain some text")
    else:
        is_ok = messagebox.askokcancel(title = website, message = f"These are teh details entered: \nEmail: {e_mail} " f"Password {password} \nIs it ok to save?")

    if(is_ok):
        password_file.write(f"{website} | {e_mail} | {password} \n")
    
        website_entry.delete(0, END)
        password_entry.delete(0, END)


    password_file.close()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20,pady=20)
window.title("Password Manager")

canvas = Canvas(width="200", height="200")
logo_Img = PhotoImage(file = "password_manager/logo.png")
canvas.create_image(100, 100, image = logo_Img)
  
canvas.grid(column = 1, row = 0)

website_label = Label(text = "Website:")
website_label.grid(column = 0, row = 1)

email_label = Label(text = "Email/Username:")
email_label.grid(column = 0, row = 2)

password_label = Label(text="Password:")
password_label.grid(column = 0, row = 3)

website_entry = Entry(width = 35)
website_entry.focus()
website_entry.grid(column = 1, row = 1, columnspan = 2)

email_entry = Entry(width = 35)
email_entry.grid(column = 1, row = 2, columnspan = 2)
email_entry.insert(0, "alpalp@mail.com")
password_entry = Entry(width = 21)
password_entry.grid(column = 1, row = 3)

generate_password_button = Button(text = "Generate Password", command = generate_password_clicked)
generate_password_button.grid(column = 2, row = 3)

add_button = Button(text = "Add", width = 36, command = add_button_clicked)
add_button.grid(column = 1, row = 4, columnspan = 2)












window.mainloop()