from flask import Flask,request, render_template
import numpy as np
import pickle
import sklearn
import jsonpickle
print(sklearn.__version__)
#loading models
dtr = pickle.load(open('dtr.pkl','rb'))
preprocesser = pickle.load(open('preprocessor.pkl','rb'))

#flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route("/predict",methods=['POST'])
def predict():
    if request.method == 'POST':

        State_Name = request.form['State_Name']
        Crop_Type  = request.form['Crop_Type']
        Crop  = request.form['Crop']
        rainfall  = request.form['rainfall']
        temperature  = request.form['temperature']
        Area_in_hectares  = request.form['Area_in_hectares']
        Production_in_tons  = request.form['Production_in_tons']

        features = np.array(
            [[State_Name, Crop_Type, Crop, rainfall, temperature, Area_in_hectares, Production_in_tons]], dtype=object)

        # Transform the features using the preprocessor
        transformed_features = preprocesser.transform(features)

        # Make the prediction
        predicted_yield = dtr.predict(transformed_features).reshape(1, -1)



        return render_template('index.html',predicted_yield = predicted_yield)

if __name__=="__main__":
    app.run(debug=True)