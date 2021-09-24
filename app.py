# importing necessary dependdencies

from flask import Flask,render_template,request
from flask_cors import cross_origin
import pickle

app = Flask(__name__) # intializing the flask app

@app.route('/', methods=['GET']) # route to display homepage
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            preg = int(request.form['pregnancies'])
            glucose = int(request.form['glucose'])
            bp = int(request.form['bloodpressure'])
            st = int(request.form['skinthickness'])
            insulin = int(request.form['insulin'])
            bmi = float(request.form['bmi'])
            dpf = float(request.form['dpf'])
            age = int(request.form['age'])
            filename = 'diabetic_prediction_final_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))  # loading the model file from the storage
            # predictions using the loaded model file
            prediction = loaded_model.predict([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
            print('prediction is', prediction)
            # showing the prediction result in a UI
            return render_template('result.html', prediction= prediction)
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'
        # return render_template('results.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
     #app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)  # running the app


