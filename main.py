from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
    return "Merhaba Dunya! Ben bir Python dosyasından geldim!"

if __name__ == "__main__":
    # Uygulama 0.0.0.0 IP'sine bağlanmalı ki Docker'da dışarıdan erişilebilsin
    app.run(host='0.0.0.0', port=5000)
