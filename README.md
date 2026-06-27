# 🔐 Password Strength Analyzer

A simple and interactive **Password Strength Analyzer** built with **Python** and **Streamlit**. The application evaluates password strength based on common security rules, estimates password entropy, provides an approximate crack-time assessment, and generates a strong recommended password.

## 🚀 Features

* Analyze password strength in real time
* Check for:

  * Minimum password length
  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Special characters
* Password entropy calculation
* Password strength progress bar
* Crack time estimation
* Secure random password generator
* Password security tips

## 🛠️ Technologies Used

* Python 3.x
* Streamlit
* Regular Expressions (`re`)
* Math
* Random
* String

## 📂 Project Structure

```
Password-Strength-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/Password-Strength-Analyzer.git
```

### Navigate to the project

```bash
cd Password-Strength-Analyzer
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

## 📊 Password Evaluation Criteria

| Check             | Requirement                   |
| ----------------- | ----------------------------- |
| Length            | At least 8 characters         |
| Uppercase         | At least one uppercase letter |
| Lowercase         | At least one lowercase letter |
| Number            | At least one digit            |
| Special Character | At least one special symbol   |

## 🔐 Security Features

* Password entropy estimation
* Strength classification (Weak / Medium / Strong)
* Crack-time estimation
* Secure password recommendation
* Password creation best practices

## 📸 Screenshot

*Add a screenshot of the application here.*

## 🤝 Contributing

Contributions are welcome. Feel free to fork the repository, create a feature branch, and submit a pull request.

## 📄 License

This project is open-source and available under the MIT License.
