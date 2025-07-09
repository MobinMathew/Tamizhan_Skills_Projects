# Password strength checker
import tkinter as tk
from tkinter import messagebox
import re
import nltk
from nltk.corpus import words

# download only once
nltk.download('words')

# load the list of english words
english_words = set(words.words())

def check_password_strength(password):
    score = 0
    suggestions = []
    
    # length check
    if len(password) >= 8:
        score +=1
    else:
        suggestions.append("Use at least 8 characters")
    
    # Uppercase check
    if re.search(r"[A-Z]",password):
        score +=1
    else:
        suggestions.append("Add uppercase letters.")
        
    # Lowercase check
    if re.search(r"[a-b]",password):
        score +=1
    else:
        suggestions.append("Add lowercase letters.")
        
    # Digit check
    if re.search(r"\d",password):
        score +=1
    else:
        suggestions.append("Include numbers.")
        
    # Special character check
    if re.search(r"[!@#$^&*(),.?\":{}|<>]",password):
        score +=1
    else:
        suggestions.append("Use special characters.")
        
    # check for dictionary word
    lower_password = password.lower()
    for word in english_words:
        if word in lower_password and len(word) > 3:
            suggestions.append("Avoid using dictionary words like:" + word)
            score -= 1 #penalize score
            break
    
    # Strength label
    if score <=2:
        strength = "Weak"
    elif score <=4:
        strength = "Medium"
    else:
        strength = "Strong"
    
    return strength, suggestions

# GUI setup
root = tk.Tk()
root.title("Password Stength Checker")
root.geometry("400x350")

# label
label = tk.Label(root, text="enter your password:", font=("Arial", 12))
label.pack(pady=10)

# entery field
entry = tk.Entry(root, show="*", width=30)
entry.pack()

# Show / Hide password toggle
show_password = tk.BooleanVar(value = False)

def toggle_password():
   if show_password.get():
       entry.config(show="")
       toggle_button.config(text="Hide")
   else:
       entry.config(show="*")
       toggle_button.config(text="show")

toggle_button = tk.Checkbutton(root, text="Show", variable=show_password, command=toggle_password)
toggle_button.pack()
        

# Result
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# suggestions box
suggestion_text = tk.Text(root, height=6, width=45)
suggestion_text.pack(pady=5)

def on_check():
    password = entry.get()
    strength, suggestions = check_password_strength(password)

    if strength == "Weak":
        result_label.config(text=f"Strength: {strength}" , fg="red")
    elif strength == "Medium":
        result_label.config(text=f"Strength: {strength}" , fg="blue")
    else:
        result_label.config(text=f"Strength: {strength}" , fg="green")
    
    suggestion_text.delete("1.0", tk.END)
    for tip in suggestions:
        suggestion_text.insert(tk.END,"- "+ tip + "\n")
    
# Button
check_button = tk.Button(root, text="Check Strength", command=on_check)
check_button.pack(pady=10)

root.mainloop()

