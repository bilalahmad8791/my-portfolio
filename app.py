from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
CORS(app)  # Allow frontend to call backend

# Your Email Credentials (Use App Password)
EMAIL_ADDRESS = "bilalahmad858657@gmail.com"
EMAIL_PASSWORD = "aqir fhwo veam lkhh"  # App Password from Google

@app.route("/send_email", methods=["POST"])
def send_email():
    try:
        data = request.get_json()
        name = data["name"]
        sender_email = data["email"]
        subject = data["subject"]
        message_body = data["message"]

        # Email Content
        msg = EmailMessage()
        msg["Subject"] = f"New Message from {name}: {subject}"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS  # Send to your own email
        msg.set_content(f"Name: {name}\nEmail: {sender_email}\n\nMessage:\n{message_body}")

        # Send Email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        return jsonify({"message": "Email sent successfully!"}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"message": "Error sending email!"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

