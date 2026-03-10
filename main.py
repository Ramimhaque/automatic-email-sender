import smtplib


def automatic_email():
    s=None
    try:        # attempts to run the code, if an error occurs it passes it to except.
        user = input("Enter Your Name >>: ")
        if not user:
            user="valued customer"
        email = input("Enter Your Email Address >>: ")
        print("initialising mail".center(30,"-"))
        message = f"Subject: Automatic Email\n\nDear {user}, This is a test mail for automatic mail reply" #in this line there are both the subject and massege
        host_mail="your mail"             #sender email 
        app_password="app password"       #app password from google not your gmail password
    
        s = smtplib.SMTP('smtp.gmail.com', 587)  # Create a connection to Gmail's mail server (587 is the secure mail port)
        s.starttls()     # Encrypt the connection for security
        s.login(host_mail, app_password)    #login's to the host mail.
        s.sendmail(host_mail, email, message)   #sends the automated mail.
        print("Email Sent!".center(30,"-"))
    except Exception as err:      #for any unexpected error.
        print(f"Sorry there was an error and the error is {err}")
    finally:
        if s:          #checks if s something else than none.
            s.quit()    #close the connection from gmail server.
automatic_email()