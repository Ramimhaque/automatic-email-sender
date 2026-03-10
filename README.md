# 📧 Automatic Email Sender

A simple Python script that sends automated emails using Gmail's SMTP server. Just run the script, enter a name and email address, and it sends a personalised email automatically.

---

## 📋 Table of Contents

- [What It Does](#what-it-does)
- [Requirements](#requirements)
- [Setup Guide](#setup-guide)
- [How To Run](#how-to-run)
- [Intended Message and Subject](#intended-message-and-subject)
- [How It Works](#how-it-works)
- [Important Security Notes](#important-security-notes)
- [Common Errors](#common-errors)

---

## What It Does

- Asks for the recipient's name and email address
- Sends a personalised automated email to that address
- Handles errors gracefully — if something goes wrong it tells you what happened
- Safely closes the connection to Gmail's server after sending

---

## Requirements

- Python 3.x
- A Gmail account
- A Gmail App Password (not your normal Gmail password — see setup guide below)

No extra libraries needed. `smtplib` comes built into Python.

---

## Setup Guide

Before running the script you need to set up a Gmail App Password. Follow these steps carefully.

### Step 1 — Turn On 2-Step Verification
1. Go to your [Google Account](https://myaccount.google.com)
2. Click **Security** on the left
3. Under "How you sign in to Google" click **2-Step Verification**
4. Follow the steps to turn it on

### Step 2 — Create an App Password
1. Go to your [Google Account](https://myaccount.google.com)
2. Click **Security**
3. Under "How you sign in to Google" click **App Passwords**
4. Give it a name (example: "Python Email Script")
5. Click **Create**
6. Google will give you a 16 character password like: `abcd efgh ijkl mnop`
7. **Copy it — you only see it once**

### Step 3 — Add Your Details To The Script
Open `main.py` and find these two lines:

```python
host_mail = "your mail"
app_password = "app password"
```

Replace them with your real details:

```python
host_mail = "youremail@gmail.com"
app_password = "abcd efgh ijkl mnop"
```

---

## How To Run

1. Clone this repository
```
git clone https://github.com/Ramimhaque/automatic-email-sender.git
```

2. Navigate into the folder
```
cd automatic-email-sender
```

3. Run the script
```
python main.py
```

4. Follow the prompts
```
Enter Your Name >>: Ishmam
Enter Your Email Address >>: recipient@gmail.com
----------initialising mail----------
-----------Email Sent!-----------
```

---

## ✏️ Intended Message and Subject

By default the script sends this message with this subject:

```
Subject: Automatic Email

Dear {name}, This is a test mail for automatic mail reply
```

You can change both the subject and the message. Open `main.py` and find this line:

```python
message = f"Subject: Automatic Email\n\nDear {user}, This is a test mail for automatic mail reply"
```

The line has two parts separated by `\n\n` —

| Part | What it is |
|---|---|
| `Subject: Automatic Email` | The subject line — change this to anything |
| `Dear {user}...` | The message body — change this to anything |

The `\n\n` in the middle is important — it separates the subject from the body. **Do not remove it.**

**Examples:**

Welcome email:
```python
message = f"Subject: Welcome!\n\nDear {user}, Welcome to our platform! We are glad to have you."
```

Reminder email:
```python
message = f"Subject: Reminder\n\nDear {user}, This is a reminder that your appointment is tomorrow."
```

Custom announcement:
```python
message = f"Subject: Big News\n\nDear {user}, We have exciting news to share with you!"
```

---

### ⚠️ Emoji Warning

This script sends **plain text emails only.** If you add emojis or special characters like `é ü ñ 😊 🎉` the email server may display them as broken symbols like this:

```
Dear Ishmam, Great news! ð??
```

**Stick to basic English letters and punctuation** to keep the email looking clean. Emoji support requires a more advanced email format called MIME which is not covered in this version of the script.

---

## How It Works

```
1. Script asks for recipient's name and email
2. Connects to Gmail's SMTP server on port 587
3. Encrypts the connection using TLS security
4. Logs into the sender's Gmail account
5. Sends the personalised email
6. Closes the connection safely
```

### Port 587
Port `587` is the worldwide standard port for sending emails securely. You do not need to change this.

### TLS Encryption
The script uses `starttls()` to encrypt the connection before sending any login details. This keeps your password safe during transmission.

---

## Important Security Notes

⚠️ **Never commit your real App Password to GitHub.**

If you accidentally push your App Password to GitHub:
1. Go to your Google Account immediately
2. Delete that App Password
3. Create a new one

Your main Gmail password stays safe — App Passwords only have limited access.

**Better practice** — use environment variables instead of hardcoding your credentials:

```python
import os

host_mail = os.environ.get("HOST_MAIL")
app_password = os.environ.get("APP_PASSWORD")
```

---

## Common Errors

| Error | Cause | Fix |
|---|---|---|
| `socket.gaierror` | No internet connection | Check your connection |
| `SMTPAuthenticationError` | Wrong App Password | Double check your App Password |
| `ConnectionRefusedError` | Gmail server unreachable | Try again later |
| `NameError: s not defined` | Connection failed before opening | Already handled in the script |

---

## Author

Made by [Ramimhaque](https://github.com/Ramimhaque)

---

## License

This project is open source and free to use.
