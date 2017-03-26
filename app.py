from flask import Flask
import RPi.GPIO as GPIO
from time import sleep

###callout ip addresses
### pi zero 192.168.1.67
### port number 9990

app = Flask(__name__)

@app.route("/")
def hello():
    GPIO.setmode(GPIO.BOARD)

    Motor1A = 16
    Motor1B = 18
    Motor1E = 22
    
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)
    
    print "Going forwards"
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    
    sleep(2)
    
    print "Going backwards"
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    
    sleep(2)
    
    print "Now stop"
    GPIO.output(Motor1E,GPIO.LOW)
    
    GPIO.cleanup()
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9876, debug=True)