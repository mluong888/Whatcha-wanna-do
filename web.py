from flask import Flask, request, render_template
from app import eb_api_query
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST': #this block is only entered when the form is submitted

        location = request.form.get('location')
        date = request.form.get('date')
        radius = request.form.get('radius')
        price = request.form.get('price')
        category = request.form.get('category')
        # acronym = func(category)
        temp = eb_api_query(location, date, radius, price, category)
        print(temp)
        return render_template('index.html', lst = temp)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
