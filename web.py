from flask import Flask, request, render_template
# from app import eb_api_query
from app2 import tm_api
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
        # price = request.form.get('price')
        category = request.form.get('category')
        # acronym = func(category)
        # temp = [{
        # "name": "Marvin's Room",
        # "url": "www.google.com",
        # "description": "Wine and cheese night?",
        # "location": "Marvin's room",
        # "date": "2019-10-26T00:00:00",
        # "start_time": "19:00",
        # "end_time": "21:00",
        # "image": "https://static.spin.com/files/120319-drake-640x426.png"
        # },
        # {
        # "name": "Halloween Social",
        # "url": "www.google.com",
        # "description": "Celebrate halloween with Codeology!",
        # "location": "Campanille",
        # "date": "2019-10-31T00:00:00",
        # "start_time": "19:00",
        # "end_time": "24:00",
        # "image": "https://i.ticketweb.com/i/00/09/30/87/89_Edp.jpg?v=3"
        # },
        # ]
        temp = tm_api(location, date, radius, category)
        # print(temp)
        # print("=============================")
        return render_template('index.html', lst = temp)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
