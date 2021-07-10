from flask import Flask,request,jsonify,render_template
import numpy as np
import pickle

app=Flask(__name__)
model=pickle.load(open('internship_selection_or_not.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():

    int_feature1=request.form['cgpi']
    int_feature2=request.form['12th percentage']
    int_feature3=request.form['10th percentage']
    prediction=model.predict([[int_feature1,int_feature2,int_feature3]])
    if prediction==True:
        return render_template('index.html',prediction_text='you got selected for the internship')
    else:
        return render_template('index.html', prediction_text='sorry work hard u are not selected for our internship program')


if __name__=='__main__':
    app.run()