from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/Home')
def home_page():
    return render_template('home.html')


@app.route('/About')
@app.route('/about')
def about_page():
    items = [
        {'id':1,'name':'Phone','barcode':'893212299897','price':1000},
        {'id':2,'name':'Laptop','barcode':'123985473165','price':2000},
        {'id':3,'name':'TV','barcode':'231985128446','price':3000},


        ]

    return render_template('about.html',items=items)


if __name__ == '__main__' :
    app.run(debug=True)