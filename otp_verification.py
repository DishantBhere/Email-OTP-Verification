import os
import random
import smtplib

# Generate 6-digit OTP
digits = "0123456789"
OTP = ''.join(random.choice(digits) for _ in range(6))
msg = OTP + " is your OTP"

# Gmail SMTP setup
try:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    # Use environment variables for security
    sender_email = os.getenv("EMAIL_USER")   # set in system
    sender_pass = os.getenv("EMAIL_PASS")   # app password

    s.login(sender_email, sender_pass)

    # Input recipient email
    emailid = input("Enter your email: ")
    s.sendmail(sender_email, emailid, msg)
    s.quit()

    # OTP verification
    a = input("Enter Your OTP >>: ")
    if a == OTP:
        print("✅ Verified")
    else:
        print("❌ Incorrect OTP")
except Exception as e:
    print("Error:", e)
