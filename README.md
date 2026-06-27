# 🔐 Password Strength Analyzer

A simple and interactive **Password Strength Analyzer** built with **Python** and **Streamlit**. The application evaluates password strength using security best practices, estimates entropy, provides crack-time estimation, and offers personalized suggestions to create stronger passwords.

---

## 🚀 Features

* Password strength analysis
* Entropy calculation
* Crack time estimation
* Security checklist
* Password strength progress bar
* Strong password generator
* Personalized improvement suggestions
* Simple and responsive Streamlit interface

---

## 🛠️ Technologies Used

* Python 3
* Streamlit
* Regular Expressions (re)
* Math
* Random
* String

---

## 📂 Project Structure

```text
PasswordStrength/
│── PasswordStrengthAnalyzer.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/asipali/password_strength_analyzer.git
```

### Navigate to the project folder

```bash
cd password_strength_analyzer
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run PasswordStrengthAnalyzer.py
```

---

## 🔍 How It Works

The application checks whether the password contains:

* Minimum length (8+ characters)
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

It then calculates:

* Password entropy
* Overall strength
* Estimated crack time

Finally, it provides:

* Security recommendations
* Password improvement suggestions
* A randomly generated strong password

---

## 📸 Screenshots

Add screenshots of your application here.

Example:

```
screenshots/
├── home.png
├── analysis.png
```

---

## 🎯 Future Improvements

* Show/Hide password option
* Password breach detection (Have I Been Pwned API)
* Common password blacklist
* zxcvbn-based password scoring
* Password history check
* Copy generated password button
* Password strength visualization charts

---

## 👨‍💻 Author

**Asip Ali**

GitHub: https://github.com/asipali
