from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction', methods=['GET','POST'])
def Predict():
    if request.method == 'POST':
        features = [float(request.form['SL']),
                    float(request.form['SW']),
                    float(request.form['PL']),
                    float(request.form['PW'])]
        model = pickle.load(open('model.pkl', 'rb'))
        result = model.predict([features])[0]
    return render_template('prediction.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)



