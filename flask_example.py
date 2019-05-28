from flask import Flask, render_template ,request

app = Flask(__name__)

sayi = 0

@app.route("/")
def hello():
    print("sanirim biri bizim sayfaya girdi baskanim")
    return render_template('index.html', x = sayi)

@app.route("/ledYak")
def led_yak():
    print("led yak diye bir sayfa istegi atti efendim. ")
    return render_template('index.html', x = 1 )

@app.route("/ledSondur")
def led_sondur():
    print("led yak diye bir sayfa istegi atti efendim. ")
    return render_template('index.html', x = 0 )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
