import pickle
import numpy
from flask import Flask, render_template, request

app = Flask(__name__)

model = pickle.load(open("model.pickle", "rb"))


@app.route('/home')
def hello_world():
    return render_template("homepage.html")


@app.route("/predict", methods=['GET', 'POST'])
# @cross_origin()
def predict():
    if request.method == "POST":
        # pclass = int(request.form['pclass'])
        pclass = request.form['pclass']
        pclass = int(pclass)
        sex = request.form['sex']

        age = float(request.form['age'])

        sibsp = int(request.form['sibsp'])
        parch = int(request.form['parch'])
        fare = float(request.form['fare'])
        embarked = request.form['embark']

        if sex == "female":
            sex = 0
        else:
            sex = 1
        c = 0
        q = 0
        s = 0
        if embarked == "C":
            c = 1
        elif embarked == "Q":
            q = 1
        else:
            s = 1

        # inputs = [pclass, [sex], [age], [sibsp], [parch], [fare], [c], [q], [s]]
        inputs = [[pclass, sex, age, sibsp, parch, fare, c, q, s]]
        inputs = numpy.array(inputs)
        pred = model.predict(inputs)
        print(pred)
        output = pred
        print(output[0])
        if output[0] ==0:
            return render_template("dead.html")
        else:
            return render_template("alive.html")
    return render_template("prediction.html")


if __name__ == '__main__':
    app.run(debug=True)
