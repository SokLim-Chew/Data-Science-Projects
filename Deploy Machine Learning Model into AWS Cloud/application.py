from flask import Flask
import joblib

application = Flask(__name__)

vector = joblib.load("vectorizer.pkl")
spam_ham_model = joblib.load("spam_ham_model.pkl")

@application.route('/')
def hello_world():
    return "Hello World"

@application.route('/spamorham', methods=['GET','POST'])
def spamorham():
    message = request.args.get("message")
    vect_message = vectorizer.transform([message])
    result = span_ham_model.predict(vect_message)[0]
    return result

    if __name__ == '__main__':
        application.run()
