import smtplib

my_email = "test@gmail.com"
app_password = "password"  # Replace with your App Password

recipient_email = "recipient@gmail.com"
message = "Hello, World!"

# Establish a connection to the SMTP server
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()

    try:
        connection.login(user=my_email, password=app_password)
        print("Login successful!")
        
        # Send the email
        connection.sendmail(from_addr=my_email, to_addrs=recipient_email, msg=message)
        print("Email sent successfully!")
        
    except smtplib.SMTPAuthenticationError:
        print("Login failed. Please check your credentials.")
    
