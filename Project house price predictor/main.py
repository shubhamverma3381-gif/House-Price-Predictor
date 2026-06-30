from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

model = pickle.load(open(r"D:\Project 2\RidgeModel_Best.pkl", 'rb'))
df = pd.read_csv(r'D:\Project 2\Cleaned_data.csv')

@app.route('/')
def index():
    locations = sorted(df['location'].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['post'])
def predict():
    location = request.form.get('location')
    sqft = float(request.form.get('sqft'))
    bath = float(request.form.get('bath'))
    bhk = float(request.form.get('BHK'))

    input_data = pd.DataFrame([[location, sqft, bath, bhk]],
                              columns=['location', 'total_sqft', 'bath', 'BHK'])
    
    prediction = model.predict(input_data)[0]
    return str(round(prediction, 2))

if __name__=="__main__":
    app.run(debug=True, port=5001)

    