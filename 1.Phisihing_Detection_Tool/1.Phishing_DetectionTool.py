import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import tkinter as tk
from tkinter import messagebox

# Load dataset
df = pd.read_csv('C:/Users/Mobin/Desktop/internship_Projects/1.Phisihing_Detection_Tool/phishing_data.csv')

def extract_features(url):
    features ={}
    features ['url_length'] = len(url)
    features ['has_at_sybmoble'] = 1 if '@' in url else 0
    features ['has_hypen'] = 1 if '-' in url else 0
    features ['num_dots'] = url.count('.')
    features ['uses_https'] = 1 if url.startswith('https') else 0
    features ['has_ip'] = 1 if url.replace('.','').isdigit() else 0
    
    return features

# apply feature extraction to all urls
features = df['url'].apply(extract_features)

# converting the list of dictionaries into a data farmes
features_df = pd.DataFrame(features.tolist()) 

# combine features with labels
final_df = pd.concat([features_df, df['label']], axis=1)

# Train model
#  final_df full dataframe with feactures+label 
# .drop('label',axis =1) removes the cloumn label from the dataframe axis = 1 cloumn
inputData = final_df.drop('label',axis =1)

target = final_df['label']

inputData_train, inputData_test, target_train, target_test = train_test_split(inputData,target, test_size=0.2, random_state=42)

# deafult testing RandomForestClassifier()
model = RandomForestClassifier()

model.fit(inputData_train,target_train)

target_pred = model.predict(inputData_test)

print("Accuracy:", accuracy_score(target_test,target_pred))
print("\nClassification Report:\n",classification_report(target_test,target_pred, zero_division=1))

#GUI SETUP
root = tk.Tk()
root.title("Phishing URL Detector")
root.geometry("400x300")
root.config(bg="#f0f0f0")

# GUI Component
label = tk.Label(root, text="Enter url:", font=("Arial", 12), bg="#f0f0f0")
label.pack(pady=10)

url_entry = tk.Entry(root, width=40, font=("Arial", 12))
url_entry.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial",14), bg="#f0f0f0", fg="blue")
result_label.pack(pady=20)

# Prediction function
def predict_url():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Input Error","Please enter a URL.")
        return
    features = extract_features(url)
    features_df = pd.DataFrame([features])
    predication = model.predict(features_df)[0]
    
    if predication == 1:
        result_label.config(text=" !!! Phishing URL Detected !!!", fg="red")
    else:
        result_label.config(text="This URL is SAFE", fg="green")
        
# Button
predict_button = tk.Button(root, text="Check", command=predict_url, font=("Arial", 12), bg="#4CAF50", fg="white")
predict_button.pack(pady=10)

#Run GUI loop
root.mainloop()
