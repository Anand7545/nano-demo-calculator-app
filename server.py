from flask import Flask

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data= json.data
    first= data['first']
    second= data['second']
    return first+second

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data= json.data
    first= data['first']
    second= data['second']
    return first-second

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
