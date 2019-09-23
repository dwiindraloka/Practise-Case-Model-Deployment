import numpy as np
from flask import Flask, request, jsonify
from sklearn.externals import joblib

app = Flask(__name__)

model = joblib.load(open('/home/dwiindraloka/mysite/rf.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    datas = request.get_json(force=True)
    output = []
    no = 1
    for data in datas:
        # Make prediction using model loaded from disk as per the data.
        prediction = model.predict([np.array([data['a'],data['b'],data['c'],data['d'],data['e'],data['f'],data['g'],data['h'],data['i'],data['j']])])
        if prediction == 0:
            out = ("PERSON " + str(no) + ": HER/HIS NEXT MONTH PAYMENT WILL " + "NOT LATE")
            output.append(out)
            no += 1
        else:
            out = ("PERSON " + str(no) + ": HER/HIS NEXT MONTH PAYMENT WILL " + "LATE")
            no += 1
            output.append(out)
    return jsonify(output)