from flask import Flask, render_template, request
import joblib

app = Flask(__name__)


def get_encoded(age, trestbps, chol, fbs, thalach, oldpeak, sex, cp, restecg, exang, slope, ca, thal):
    args = []
    args.append(age)
    args.append(trestbps)
    args.append(chol)
    args.append(thalach)
    args.append(oldpeak)
    if sex == 0:
        args.append(1)
        args.append(0)
    elif sex == 1:
        args.append(0)
        args.append(1)
    if cp == 0:
        args.append(1)
        args.append(0)
        args.append(0)
        args.append(0)
    elif cp == 1:
        args.append(0)
        args.append(1)
        args.append(0)
        args.append(0)
    elif cp == 2:
        args.append(0)
        args.append(0)
        args.append(1)
        args.append(0)
    elif cp == 3:
        args.append(0)
        args.append(0)
        args.append(0)
        args.append(1)
    if restecg == 0:
        args.append(1)
        args.append(0)
        args.append(0)
    elif restecg == 1:
        args.append(0)
        args.append(1)
        args.append(0)
    elif restecg == 2:
        args.append(0)
        args.append(0)
        args.append(1)

    if exang == 0:
        args.append(1)
        args.append(0)
    elif exang == 1:
        args.append(0)
        args.append(1)

    if slope == 0:
        args.append(1)
        args.append(0)
        args.append(0)
    elif slope == 1:
        args.append(0)
        args.append(1)
        args.append(0)
    elif slope == 2:
        args.append(0)
        args.append(0)
        args.append(1)

    # ca 5
    if ca == 0:
        args.append(1)
        args.append(0)
        args.append(0)
        args.append(0)
        args.append(0)
    elif ca == 1:
        args.append(0)
        args.append(1)
        args.append(0)
        args.append(0)
        args.append(0)
    elif ca == 2:
        args.append(0)
        args.append(0)
        args.append(1)
        args.append(0)
        args.append(0)
    elif ca == 3:
        args.append(0)
        args.append(0)
        args.append(0)
        args.append(1)
        args.append(0)
    elif ca == 4:
        args.append(0)
        args.append(0)
        args.append(0)
        args.append(0)
        args.append(1)

    # thal 4
    if thal == 0:
        args.append(1)
        args.append(0)
        args.append(0)
        args.append(0)
    elif thal == 1:
        args.append(0)
        args.append(1)
        args.append(0)
        args.append(0)
    elif thal == 2:
        args.append(0)
        args.append(0)
        args.append(1)
        args.append(0)
    elif thal == 3:
        args.append(0)
        args.append(0)
        args.append(0)
        args.append(1)

    # fbs 2
    if fbs == 0:
        args.append(1)
        args.append(0)
    elif fbs == 1:
        args.append(0)
        args.append(1)
    return args


@app.route('/')
def home():
    return render_template('original.html')


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        age = float(request.form['age'])
        sex = float(request.form['sex'])
        cp = float(request.form['cp'])
        trestbps = float(request.form['trestbps'])
        chol = float(request.form['chol'])
        fbs = float(request.form['fbs'])
        restecg = float(request.form['restecg'])
        thalach = float(request.form['thalach'])
        exang = float(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = float(request.form['slope'])
        ca = float(request.form['ca'])
        thal = float(request.form['thal'])

        mul_reg = open('svm_model', 'rb')
        ml_model = joblib.load(mul_reg)
        model_predcition = ml_model.predict([get_encoded(age=age, trestbps=trestbps, chol=chol, fbs=fbs, thalach=thalach,
                                            oldpeak=oldpeak, sex=sex, cp=cp, restecg=restecg, exang=exang, slope=slope, thal=thal, ca=ca)])
        if model_predcition == 1:
            res = 'Affected'
        else:
            res = 'Not affected'
    return render_template('predict.html', prediction=res)


if __name__ == '__main__':
    app.run()
