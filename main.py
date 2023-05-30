from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        my_email = request.form['email']
        password = request.form['password']
        recipient_email = request.form['recipient_email']
        message = request.form['message']

        try:
            connection = smtplib.SMTP("smtp.gmail.com", 587)
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=recipient_email, msg=f"Subject: Hello\n\n{message}")
            connection.quit()

            return 'Email sent successfully!'
        except smtplib.SMTPException as e:
            return f'Error: {str(e)}'
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
