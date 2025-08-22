# Email OTP Verification (Python)

This is a simple Python script that generates a 6-digit One-Time Password (OTP) and sends it to the user's email using Gmail SMTP. The user then enters the OTP in the console to verify their identity.


  ## 🍋‍🟩Features 

1.Generates a random 6-digit OTP

2.Sends OTP securely via Gmail (SMTP + TLS)

3.Verifies user input against generated OTP

4.Uses App Passwords for secure login

 ## 🍉Requirements

1.Python 3.x

2.Gmail account with App Password enabled



Install dependencies:

```
pip install secure-smtplib
```

## 🌶️ Setup

1.Generate an App Password in your Google Account.

2.Store credentials as environment variables:

```
export EMAIL_USER=youremail@gmail.com
export EMAIL_PASS=yourapppassword
```
3.Run the Script:
```
python otp_verification.py

```
## 🍋 Example 
```
Enter your email: user@example.com
Enter Your OTP >>: 123456
✅ Verified
```
