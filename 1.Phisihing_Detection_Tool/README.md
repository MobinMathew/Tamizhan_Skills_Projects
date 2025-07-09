# Project 1
# Phishing URL Detection Tool

# Descripion:

this project detects phishing URLs using machine learning and provides a user-friendly Tkiner GUI to test URLs in real time. It rains a model on labeled URLs and predicts whether an input is safe or phishing based on various chaacterisics.

# Features:
-> Extracts featues like @, -, length, HTTPS, IP usage, etc.
-> Trains a RandomForestClassifie to detect phishing.
-> Live URL checking via graphical interface.
-> Prints accuracy and classification metrics to console.
-> "Phishing detected" in red, "Safe" in green - for clear UX.

# Dataset:
File: phishing_data.csv
Formate: CSV
Columns:
  -> url: the websie URL
  -> label: 1 for phishing, 0 for safe

# Machine Learning Model:
 -> Model: RandomForestClassifier
 -> Training/Test Split: 80/20
 -> Evaluation: accuracy_score , classification_report

# GUI Functionality:
 -> User inputs a URL.
 -> On clicking "Check URL":
    -> Features are extracted.
    -> Model predicts.
    -> Result shown in red(phishing) or green(safe).

# Code Explanation:

 1. Import Libraries:
    
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score, classification_report
    import tkinter as tk
    from tkinter import messagebox
  
  -> pandas: Load and process CSV data.
  -> scikit-learn: Train/test ML model.
  -> tkinter: Build GUI
  -> messagebox: show pop-up alert

2. Load Dataset:
   
   df = pd.read_csv('C:/Users/Mobin/Desktop/internship_Projects/1.Phisihing_Detection_Tool/phishing_data.csv')

 -> Loads the dataset of URLs and their labels.

 3. Feature Extraction Function

    def extract_features(url):
    features ={}
    features ['url_length'] = len(url)
    features ['has_at_sybmoble'] = 1 if '@' in url else 0
    features ['has_hypen'] = 1 if '-' in url else 0
    features ['num_dots'] = url.count('.')
    features ['uses_https'] = 1 if url.startswith('https') else 0
    features ['has_ip'] = 1 if url.replace('.','').isdigit() else 0
    
    return features
  
  -> Extracts 6 useful features from each URL:
     -> Length
     -> Use of @
     -> Use of -
     -> Dot count
     -> HTTPS or not
     -> IP-based URL detection

4. Apply Feature Extraction:

   features = df['url'].apply(extract_features)
   features_df = pd.DataFrame(features.tolist()) 
   final_df = pd.concat([features_df, df['label']], axis=1)
   
 -> apply feature extraction to all urls
 -> converting the list of dictionaries into a data farmes
 -> combine features with labels

5. Train the Model:
  
   inputData = final_df.drop('label',axis =1)
   target = final_df['label']
   inputData_train, inputData_test, target_train, target_test = train_test_split(inputData,target, test_size=0.2, random_state=42)
   model = RandomForestClassifier()
   model.fit(inputData_train,target_train)

 -> Splits data into training and testing sets.
 -> Trains a Random Forest classifier on the training data.

6. Evaluate the model
   
   target_pred = model.predict(inputData_test)
   print("Accuracy:", accuracy_score(target_test,target_pred))
   print("\nClassification Report:\n",classification_report(target_test,target_pred, zero_division=1))

 -> Predicts on test set and prints evaluation metrics.

7. Build GUI Using Tkinter:
   
   root = tk.Tk()
   root.title("Phishing URL Detector")
   root.geometry("400x300")
   root.config(bg="#f0f0f0")

  -> Initializes a GUI Window with title and size.

8.  GUI Component:

    label = tk.Label(root, text="Enter url:", font=("Arial", 12), bg="#f0f0f0")
    label.pack(pady=10)

    url_entry = tk.Entry(root, width=40, font=("Arial", 12))
    url_entry.pack(pady=5)

    result_label = tk.Label(root, text="", font=("Arial",14), bg="#f0f0f0", fg="blue")
    result_label.pack(pady=20) 

 -> Adds label, input field and result label.

9. Prediction function:

  def predict_url():
    url = url_entry.get()
    if not url:
        messagebox.showwnarning("Input Error","Please enter a URL.")
        return
    features = extract_features(url)
    features_df = pd.DataFrame([features])
    predication = model.predict(features_df)[0]
    
    if predication == 1:
        result_label.config(text=" !!! Phishing URL Detected !!!", fg="red")
    else:
        result_label.config(text="This URL is SAFE", fg="green")

 -> This fuction run only when the user click on button
 -> Grabs the URL, extracts features, make a predicition.
 -> Updates the label based on prediction.
        
10. Button:

    predict_button = tk.Button(root, text="Check", command=predict_url, font=("Arial", 12), bg="#4CAF50", fg="white")
    predict_button.pack(pady=10)

  -> Add button

11. Start GUI:
  
   root.mainloop()

  -> Runs the GUI loop - keeps the window open.

# Key Learnings:
 -> Extracting and engineering feactures from real-world URLs.
 -> Training ML models using scikit-learn
 -> Creating functional GULs with tkinter
 -> Building real-time, inteactive security tools

# Author:
 Mobin Mathew
 Tamizhan Skills RISE Cybersecurity & Ethical Hacking Intern