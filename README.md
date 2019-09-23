# Practise-Case-Model-Deployment
## 1. Deploy Model Credit Scoring 
This model is used to do credit scoring by using the Random Forest algorithm to predict whether a consumer will be late paying credit in the next month.
<br>
The variables that used to calculate credit scoring are:
<br>
* LIMIT_BAL: Customer's credit limits (in USD)
* SEX: Customer's gender (Man = 1, Woman = 2)
* AGE: Customer's age
* PAY_1: Customer late for first payment (in Month)
* PAY_2: Customer late for second payment (in Month)
* PAY_3: Customer late for third payment (in Month)
* BILL_AMT1: Customer's bill for first payment
* BILL_AMT2: Customer's bill for second payment
* BILL_AMT3: Customer's bill for third payment

<br>
The output's result are 0 or 1, namely:
<br>
0: Customer are predicted not to be late in making credit payments for next month
<br>
1: Customer are predicted to be late in making credit payments for next month
<br>

## 2. Make server on pythonanywhere
To create a deployment model, we use pythonanywhere to create a server for the model that was created. In pythonanywhere there are two files uploaded, there are:
<br>
* modelcs.pkl: file containing the Random Forest algorithm that used to to predict whether a consumer will be late paying credit in the next month.
* flask_app.py: file used as a "server" file stored in pythonanywhere.
<br>

## 3. 
