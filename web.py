from flask import Flask, render_template
import Occ

app= Flask(__name__)

@app.route("/")
def welcome():
    return "<h1 color= blue> WELCOME </h1>"

@app.route("/occupations")

def tablify():
    return render_template('tabletmpl.html',dict= Occ.makedict("occupations.csv"),rand= Occ.getRandom("occupations.csv")
    )


if __name__== "__main__":
    app.debug=True
    app.run()
