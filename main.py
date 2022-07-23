
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request
import numpy as np
import pickle
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.

@app.route('/')
def home():
    return render_template('index.html')

# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 6)
    loaded_model = pickle.load(open("model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]
 
@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        parameter_list = request.form.to_dict()
        parameter_list = list(parameter_list.values())
        parameter_list_pred = list(map(float, parameter_list))
        result = ValuePredictor(parameter_list_pred)   
        print(result)    
        if int(result)== 1:
            prediction ='Bream'
        elif int(result)==2:
            prediction ='Roach'  
        elif int(result)==3:
            prediction='Whitefish'   
        elif int(result)==4:
            prediction='Parkki'
        elif int(result)==5:
            prediction='Perch'
        elif int(result)==6:
            prediction='Pike'
        elif int(result)==7:
            prediction='Smelt'
        return render_template("result.html", prediction = prediction)
# main driver function
if __name__ == '__main__':
    app.debug = True
    app.run()