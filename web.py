from flask import Flask, render_template
import util.Occ as occ

app= Flask(__name__)

#default homepage
@app.route("/")
def welcome():
    return "<h1> WELCOME </h1><br>Go to /occupations for a glimpse into your future..."

#the occupations route
@app.route("/occupations")
def tablify(): #uses template to show page with table
    return render_template('tabletmpl.html',dict= occ.makedict("data/occupations.csv"),rand= occ.getRandom("data/occupations.csv")
    )


if __name__== "__main__":
    app.debug=True
    app.run()
