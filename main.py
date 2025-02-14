import tkinter
import random
import string
import pyperclip


def generatePassword():
    length = int(passwordLenght.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    passwordEntry.config(state='normal')
    passwordEntry.delete(0, tkinter.END)
    passwordEntry.insert(0, password)
    passwordEntry.config(state='disabled')

def copyPassword():
    pyperclip.copy(passwordEntry.get())

root = tkinter.Tk()
root.title("ProgrammingLearn - Password Generator")
root.geometry("400x300")
root.resizable(False, False)
root.config(bg="gray")

lenghtLable = tkinter.Label(root, text="Password Length: ", bg="gray", fg="white")
lenghtLable.grid(row=0, column=0, padx=50, pady=10)

passwordLenght = tkinter.Entry(root)
passwordLenght.grid(row=1, column=0, padx=50, pady=10)

generateButton = tkinter.Button(root, text="Generate Password", bd=1, bg="white", command=generatePassword)
generateButton.grid(row=2, column=0, padx=50, pady=20)

passwordEntry = tkinter.Entry(root, width=50, state='disabled')
passwordEntry.grid(row=3, column=0, padx=50, pady=10)

copyButton = tkinter.Button(root, text="Copy", bg="white", bd=1, command=copyPassword)
copyButton.grid(row=4, column=0, padx=50, pady=10)

root.mainloop()
