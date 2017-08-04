from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def show_color(color):
    print color
    color = color
    if color == "blue" or color == "orange" or color == "purple" or color == "red":
        return render_template("ninjacolors.html", color=color)
    else:
        color = "notapril"
        return render_template("ninjacolors.html", color=color)

@app.errorhandler(404)
def page_not_found(color):
    color = "notapril"
    return render_template("ninjacolors.html", color=color)




app.run(debug=True)