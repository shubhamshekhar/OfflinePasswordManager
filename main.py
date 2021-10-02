from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [letters[random.randint(0, len(letters) - 1)] for _ in range(nr_letters)]
    password_list += [symbols[random.randint(0, len(symbols) - 1)] for _ in range(nr_symbols)]
    password_list += [numbers[random.randint(0, len(numbers) - 1)] for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_text.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_text.get()
    email = email_text.get()
    password = password_text.get()
    if website == "" or password == "":
        messagebox.showinfo(title="Invalid Input", message="You have left one or more fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Storing below details:\nEmail: {email}\nPassword: "
                                                              f"{password}\n\nContinue?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password} \n")
                website_text.delete(0, END)
                email_text.delete(0, END)
                password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Offline Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(window, width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_text = Entry(width=52)
website_text.grid(row=1, column=1, columnspan=2, pady=10)
website_text.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_text = Entry(width=52)
email_text.grid(row=2, column=1, columnspan=2)
email_text.insert(0, "")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_text = Entry(width=34)
password_text.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, pady=10)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()
