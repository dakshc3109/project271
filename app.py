# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define Verify_otp() function
@app.route('/login' , methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'verify' and password == '12345':   
        account_sid = 'ACef4804d6898104eaee5b57f14a74458f'
        auth_token = '2f67f88f51e3797ff6b6d012b79903da'
        client = Client(account_sid, auth_token)

        verification = client.verify \
            .services('Enter your service ID') \
            .verifications \
            .create(to=mobile_number, channel='sms')

        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return render_template('user_error.html')



app.route('/otp', methods=['POST'])
def get_otp():
    
    print('Processing')
    recived_otp = request.form['recived_otp']
    mobile_number = request.form['number']
    account_sid = 'ACef4804d6898104eaee5b57f14a74458f'
    auth_toke = '2f67f88f51e3797ff6b6d012b79903da'
    verification_check = client.verify \
        .services('ISf039883ea2eb4110b2b4470ba0e396b7') \
        .verification_checks \
        .create(to=mobile_number, code=received_otp)
    print(verification_check.status)
    if verification_check.status == "pending":
        print("Enterd otp is wrong")
    else:
        return(redirect('https://projectC71.onrender.com/'))

if __name__ == "__main__":
    app.run()

