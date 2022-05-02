# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mjxd-ajjlslRXnzIwPKj4H86hw8qynh1
"""

import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

app=Flask(__name__,template_folder='templates')
model = pickle.load(open('coursepro.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='result : {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)