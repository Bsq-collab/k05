from flask import Flask, render_template
app = Flask(__name__)


#assign following fxn to run when root route requested
@app.route("/")
def hello_world():
    retStr = "No hablo queso!"
    return retStr

'''
@app.route("/my_foist_template")
def test_tmplt():
    return render_template( 'model_tmplt.html', foo ="foooooo", collection=coll)
    return retStr
'''
if __name__ == "__main__":
    app.debug = True
    app.run()
