#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyperclip


# In[1]:


import random
import string
import tkinter as tk
import pyperclip as pc

def generate():
    entry.delete(0, tk.END)
    length = lengthInput.get()
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbol = string.punctuation
    
    lowerChoice = lower+upper
    mediumChoice = lowerChoice+num
    strongChoice = mediumChoice+symbol
    password = ""
    
    if strengthInput.get() == 1:
        for i in range(length):
            password = password+random.choice(lowerChoice)
    elif strengthInput.get() == 2:
        for i in range(length):
            password = password+random.choice(mediumChoice)
    elif strengthInput.get() == 3:
        for i in range(length):
            password = password+random.choice(strongChoice)
    entry.insert(0, password)

def copy():
    randomPassword = entry.get()
    pc.copy(randomPassword)


root = tk.Tk()
lengthInput = tk.IntVar()
strengthInput = tk.IntVar()

root.title("Random Password Generator")

lengthLabel = tk.Label(root, text = "Preferred Length").grid(row = 0,column = 0)
lenghtChoice = tk.Spinbox(root, from_ = 4, to = 10, textvariable = lengthInput).grid(row = 0,column = 1)

strengthLabel = tk.Label(root, text = "Preferred Length").grid(row = 0,column =2)
lowStrength = tk.Radiobutton(root, text = "Low",variable = strengthInput, value = 1).grid(row = 0,column = 3)
mediumStrength = tk.Radiobutton(root, text = "Medium",variable = strengthInput, value = 2).grid(row = 0,column = 4)
strongStrength = tk.Radiobutton(root, text = "Strong",variable = strengthInput, value = 3).grid(row = 0,column = 5)

randomPassword = tk.Label(root, text = "Password").grid(row = 1,column = 0)
entry = tk.Entry(root)
entry.grid(row = 1,column = 1)

generateButton = tk.Button(root, text = "Generate", command = generate).grid(row = 1,column = 2)
copyButton = tk.Button(root, text = "Copy", command = copy).grid(row = 1,column = 3)


root.mainloop()

quit()

