from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Japanese to Hindi/English Translator Backend'

if __name__ == '__main__':
    app.run(debug=True)
