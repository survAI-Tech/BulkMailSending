import flask
from flask_mail import Mail, Message
import os
import numpy as np
from threading import Thread
import json
from config import *

import codecs
from os.path import join

app = flask.Flask(__name__)

app.config.update(mail_settings)
mail = Mail(app)

def load_process():
    print("serving ....")

@app.route("/api/verifyEmail", methods=["POST"])
def verifyEmail():

    if flask.request.method == "POST":
        response = {"success":False}
        data = flask.request.json
        # response['code'] = np.random.randint(1111,10000)
        with app.app_context():
            msg = Message(subject="Email Verification",
                          sender=app.config.get("MAIL_USERNAME"),
                          recipients=[data['email']]) # replace with your email for testing
            msg.html = codecs.open("templates/email.html", 'r', 'utf-8').read()
            # msg.attach('School_output.jpg','image/jpg',open(join('', 'School_output.jpg'), 'rb').read(), 'inline', headers=[['Content-ID','<image1>'],])
            # msg.attach('School_output1.jpg','image/jpg',open(join('', 'School_output1.jpg'), 'rb').read(), 'inline', headers=[['Content-ID','<image2>'],])
            mail.send(msg)
            response['success'] = True

    return json.dumps(response)

if __name__ == "__main__":
    # load the function used to classify input images in a *separate*
    # thread than the one used for main classification
    print("* Starting verifyEmail service...")
    t = Thread(target=load_process, args=())
    t.daemon = True
    t.start()
    # start the web server
    app.run()