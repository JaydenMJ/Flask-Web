from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/Home')
def home_page():
    return render_template('home.html')


@app.route('/About')
@app.route('/about')
def about_page():
    return render_template('about.html',item_name='Phone')


if __name__ == '__main__' :
    app.run(debug=True)