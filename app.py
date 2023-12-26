from flask import Flask
app =Flask(__name__)

@app.route("/")
def home():
    return "hello Everyone, From Naima"

    if __name__ =='_main':
        app.run(debug=True,host='0.0.0.0',port=5000)
