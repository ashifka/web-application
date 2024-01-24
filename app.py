from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the pre-trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(request.form['SL']),
                float(request.form['SW']),
                float(request.form['PL']),
                float(request.form['PW'])]

    # Make prediction using the loaded model
    prediction = model.predict([features])[0]

    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)


