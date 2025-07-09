# Project 2
# Password Strength Checker

# Description:
  This project is a Password Strength Checker built using Python and Tkinter GUI, which evaluates the strengh of a user's password based on multiple facors like length, use of special charactes, digits, uppercase/lowercase letters, and dictionary words. 

  The tool gives real-time feedback to users, encouraging the creation of strong and secure passwords - a key element of cybersecurity hygiene.

 
# Features:
  --> Detects weak, medium, and strong passwords.
  --> Checks for uppercase, lowercase, digits, symbols.
  --> Uses NLTK corpus to avoid common dictionary words.
  --> Color-coded feedback:
     |--- Weak -> Red
     |--- Medium -> Blue
     |--- Strong -> Green

  --> Password visibility toggle (Show/Hide password)

# NLTK Corpus:
   This project uses the nltk.corpus.words to ensure that passwords aren't just regular English dictionary words, which are easier to guess or brute-force.

    Install NLTK (if not already installed):
      pip install nltk
    
    And download the word corpus (run once):
       import nltk
       nltk.download('words')

# How Password Strength is Determined:
  Strength               Criteria
  
-> Weak                  Length <=2 OR matches a dictionary word

-> Medium                Length  >=8, contains both letters and digits

-> Strong                Length  >=8, contains uppercase, lowercase, digits, and special characters


# GUI Features 
  --> Input field for password
  --> Toggle to Show/Hide password
  --> Button to check strength
  --> Label that displays result with color-coded strength

# Code Explanation:
   
   1. Imports:

      import tkinter as tk
      from tkinter import messagebox
      import re
      import nltk
      from nltk.corpus import words

    -> tkinter: For GUI
    -> nltk.corpus.words: To compae with dictionary words
    -> re : To use regular expressions for pattern checks
    
   2. Get Wod List from NLTK:

      nltk.download('words')
      english_words = set(words.words())
    
     -> Downloads the list of English words (one-time operation).
     -> Converts the list into a Python set for fast lookup 

   3. Strength Evaluation Function:
      
       def check_password_strength(password):
             score = 0
             suggestions = []

     -> Initializes:
         -> score: numeric score for password strength
         -> suggestions: a list of feedback to improve weak passwords.
    
      # length check
            if len(password) >= 8:
                score +=1
            else:
               suggestions.append("Use at least 8 chaacters")

    -> Adds 1 point if the password is 8 characters or longer.
    
      # Uppercase check
            if re.search(r"[A-Z]",password):
                score +=1
            else:
                suggestions.append("Add uppercase letters.")

    -> Adds 1 point if it has at least one uppercase letter.
        
      #Lowercase check
            if re.search(r"[a-b]",password):
                score +=1
            else:
                suggestions.append("Add lowercase letters.")

    -> Adds 1 point for lowercase letters.

       # Digit check
            if re.search(r"\d",password):
                score +=1
            else:
                suggestions.append("Include numbers.")

    -> Adds 1 point if it has digits.

       # Special chaacter check
            if re.search(r"[!@#$^&*(),.?\":{}|<>]",password):
                score +=1
            else:
               suggestions.append("Use special characters.")
    
    -> Adds 1 point for having special characters.

       # check for dictionary word
       lower_password = password.lower()
       for word in english_words:
            if word in lower_password and len(word) > 3:
                 suggestions.append("Avoid using dictionary words like:" + word)
                 score -= 1 #penalize score
                 break

       -> If password contains any dictionary word longer than 3 letters, it reduces the score.
       -> Adds a suggestion to avoid common English words. 

       # Strength label
       if score <=2:
           strength = "Weak"
       elif score <=4:
           strength = "Medium"
       else:
           strength = "Strong"
    
       return strength, suggestions
      
      ->Based on the total score, returns:
         -> Weak (score <= 2)
         -> Medium (score <= 4)
         -> Strong (5 or more)

    3. GUI setup
    
       root = tk.Tk()
       root.title("Password Stength Checker")
       root.geometry("400x350")  
       
       -> Initializes the GUI window.
       -> Set window title, size and background color.
    
    4. GUI Components
       
       # label
       label = tk.Label(root, text="enter your password:", font=("Arial", 12))
       label.pack(pady=10)

      # entery field
       entry = tk.Entry(root, show="*", width=30)
       entry.pack()

       -> Create a label that says "enter your password:".
       -> Input box where user types the password.

      # Show / Hide password toggle
       show_password = tk.BooleanVar(value = False)

  
      def toggle_password():
          if show_password.get():
              entry.config(show="")
              toggle_button.config(text="Hide")
          else:
              entry.config(show="*")
              toggle_button.config(text="show")
      
      -> I add a toggle to show or hide the passwod using a checkbox.

      toggle_button = tk.Checkbutton(root, text="Show", variable=show_password, command=toggle_password)
      toggle_button.pack()

      -> This is the checkbox that controls the visbility of the password input.
     
     # Result:

       result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
       result_label.pack(pady=10)

    -> This label will display the password strength after checking.

     # suggestions box:

        suggestion_text = tk.Text(root, height=6, width=45)
        suggestion_text.pack(pady=5)

    -> This is a boxthat shows suggestions to help improve the password.

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

    -> When the user clicks 'check strength', this fuction gets the password, checks the  strength and update the result label with a color. 
    -> it also clear and re-fill the suggestions box.

     # Button

       check_button = tk.Button(root, text="Check Strength", command=on_check)
       check_button.pack(pady=10)

    -> This is the 'Check strength' buton that runs the evalution fuctionwhen clicked 
    
    root.mainloop()

    -> starts the GUI loop - keeps he window running and waiting fo user interaction.


# key Learnings:
  --> Strength evaluation logic based on best secuity practices.
  --> Using NLP techniques for password filtering
  --> Tkinter for secure and interactive UX
  --> Real-world application of regex and corpus checking

# Author:
 Mobin Mathew
 Tamizhan Skills RISE Cybersecurity & Ethical Hacking Intern