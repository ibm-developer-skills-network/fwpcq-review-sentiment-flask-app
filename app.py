from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/getsentiment', methods=['POST'])
def getsentiment():
    # get the URL from the form
    url = request.form['url']

    # TODO:
    # Scape the url
    # reviews = scrape(url)

    # TODO:
    # Get the sentiment
    # sentiment = get_sentiment(reviews)

    # results = sentiment

    # Hard code pretend results for now to demonstrate the app
    reviews = ["This is terrible", "This is great", "This is ok"]
    results = { "sentiment": { "angry": 0.0, "disgusted": 0.0, "fearful": 0.0, "happy": 0.0, "neutral": 0.0, "sad": 0.0, "surprised": 0.0 } }

    # Return template with data
    return render_template('getsentiment.html', url=url, reviews=reviews, results=results)

if __name__ == '__main__':
    app.run()


