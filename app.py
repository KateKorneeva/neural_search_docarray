from flask import Flask, render_template, request, redirect, url_for
from main import search_document

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    # Call your search function from main.py
    citations = search_document(query)
    return render_template('results.html', citations=citations)

if __name__ == '__main__':
    app.run(debug=True)  # You can set debug=False for production
