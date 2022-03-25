
from flask import Flask, render_template, request
from twilio.rest import Client

app = Flask(__name__)

account_sid = "TWILIO_ACC_SID"
auth_token  = "TWILIO_AUTH_TOKEN"

client = Client(account_sid, auth_token)

@app.route('/',  methods=["GET", "POST"])
def home():
    if request.method == "POST":
        number = request.form['num']
        mess = request.form['mes']
        password = request.form['pass']
        if(password == 'yoursecret'):
            message = client.messages.create(
            body=mess,
            from_="+(twilio number)",
            to=number)
            s = 'Message Sent to ' + number + ' with ID: ' + message.sid
            return render_template('index.html', status=s)
        if(password == 'yoursecret'):
            call = client.calls.create(
            url="http://demo.twilio.com/docs/voice.xml",
            to=number,
            from_="+18174820691")
            print(call , call.sid)
            s = 'Call initiated: ' + call.sid
            return render_template('index.html', status=s)
        return render_template('index.html', status="You are not AUTHORIZED!!")
    return render_template('index.html')




if __name__ == '__main__':
  app.run(debug=True)