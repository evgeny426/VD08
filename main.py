from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    excerpt = get_excerpt()
    return render_template('index.html', excerpt=excerpt)


def get_excerpt():
    url = 'https://api.quotable.io/random'
    response = requests.get(url, verify=False)
    data = response.json()
    return data

if __name__ == '__main__':
    app.run(debug=True)
