from flask import Flask
from flask import render_template, request
from sentiment_analysis import sentiment_scores

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        blob = request.form['text']
        neg, neu, pos, analysis = sentiment_scores(blob)
        return render_template('output.html', analysis=analysis, negative=neg, neutral=neu, positive=pos)


if __name__ == '__main__':
    app.run(debug=True)
