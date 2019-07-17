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
        return render_template('index.html', lst = temp)

    return render_template('index.html')

def func(acronym):
    if acronym=="bp":
        return "101"
    elif acronym=="st":
        return "102"
    elif acronym=="m":
        return "103"
    elif acronym=="fme":
        return "104"
    elif acronym=="pva":
        return "105"
    elif acronym=="fb":
        return "106"
    elif acronym=="hw":
        return "107"
    elif acronym=="sf":
        return "108"
    elif acronym=="to":
        return "109"
    elif acronym=="fd":
        return "110"
    elif acronym=="cc":
        return "111"
    elif acronym=="gp":
        return "112"
    elif acronym=="coc":
        return "113"
    elif acronym=="rs":
        return "114"
    elif acronym=="fe":
        return "115"
    elif acronym=="sh":
        return "116"
    elif acronym=="hl":
        return "117"
    elif acronym=="aba":
        return "118"
    elif acronym=="hsi":
        return "119"
    elif acronym=="sa":
        return "120"
    elif acronym=="o":
        return "199"
    else:
        # return "101,102"
        return "101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,199"

if __name__ == '__main__':
    app.run()
