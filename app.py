from flask import Flask
import RPi.GPIO as GPIO
import time

###callout ip addresses
### pi zero 192.168.1.67
### port number 9990

app = Flask(__name__)

@app.route("/")
def hello():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    print "LED on"
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    print "LED off"
    GPIO.output(18,GPIO.LOW)
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9990, debug=True)