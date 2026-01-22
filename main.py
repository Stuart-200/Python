import tkinter as tk
import random
import string


def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(8):          # password length = 8
        password += random.choice(characters)

    result_label.config(text=password)





window = tk.Tk()
window.title("Password Generator")
window.geometry("300x200")


title = tk.Label(window, text="Random Password Generator")
title.pack(pady=10)


button = tk.Button(window, text="Generate Password", command=generate_password)
button.pack(pady=10)


result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)


window.mainloop()