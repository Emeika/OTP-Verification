import sys
import random
import time
from twilio.rest import Client
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class OTPVerificationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OTP Verification")

        self.generated_otp = None
        self.otp_expiry = 0

        self.account_sid = "ACab63003efa220ec00aecd5d58f7f5201"
        self.auth_token = "df9029bb0b6089f9f555f0a15b831f00"
        self.twilio_phone_number = "923104382249"
        
        self.setup_ui()


    def generate_otp(self):
        self.generated_otp = str(random.randint(1000, 9999))
        self.otp_expiry = time.time() + 600  # OTP expires in 10 minutes

    def send_otp_to_number(self):
        phone_number = self.phone_entry.text()  # Get phone number from the input field
        if self.send_otp(phone_number):
            self.generate_otp()
            self.result_label.setText("OTP sent! Please check your phone.")
        else:
            self.result_label.setText("Failed to send OTP. Please try again later.")


    def send_otp(self):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=f"Your OTP is: {self.generated_otp}",
            from_=self.twilio_phone_number,
            to=phone_number
        )
        return message.sid is not None

    def verify_otp(self):
        entered_otp = self.otp_entry.text()
        current_time = time.time()

        if current_time <= self.otp_expiry and entered_otp == self.generated_otp:
            self.result_label.setText("OTP Verified!")
        else:
            self.result_label.setText("Invalid OTP!")

    def setup_ui(self):
        layout = QVBoxLayout()

        self.phone_label = QLabel("Enter Phone Number:")
        layout.addWidget(self.phone_label)

        self.phone_entry = QLineEdit()
        layout.addWidget(self.phone_entry)

        self.send_otp_button = QPushButton("Send OTP")
        self.send_otp_button.clicked.connect(self.send_otp)
        layout.addWidget(self.send_otp_button)

        self.label = QLabel("Enter OTP:")
        layout.addWidget(self.label)

        self.otp_entry = QLineEdit()
        layout.addWidget(self.otp_entry)

        self.verify_button = QPushButton("Verify")
        self.verify_button.clicked.connect(self.verify_otp)
        layout.addWidget(self.verify_button)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OTPVerificationApp()
    window.show()
    sys.exit(app.exec_())

