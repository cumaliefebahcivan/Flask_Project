from flask import Flask, render_template ,request
import RPi.GPIO as GPIO
app = Flask(__name__)

led_1 = "Led yaniyor."
led_0 = "Led sonmus durumda."

anahtar = 0
def ledYak(pin):
    GPIO.output(pin,GPIO.HIGH)

def ledSondur(pin):
    GPIO.output(pin, GPIO.LOW)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(31, GPIO.OUT)

@app.route("/")
def hello():
    print("sanirim biri bizim sayfaya girdi baskanim")
    anahatar = 0
    return render_template('index.html', x = led_0)

@app.route("/ledYak")
def led_yak():
    print("led yak diye bir sayfa istegi atti efendim. ")
    anahatar = 1
    return render_template('index.html', x = led_1 )

@app.route("/ledSondur")
def led_sondur():
    print("led yak diye bir sayfa istegi atti efendim. ")
    anahatar = 0
    return render_template('index.html', x = led_0)

if anahtar == 0:
    ledSondur(31)
elif anahtar == 1:
    ledSondur(31)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
