# PRACTISE CASE MODEL DEPLOYMENT
## 1. Deploy Model Credit Scoring 
This model is used to do credit scoring by using the Random Forest algorithm to predict whether a consumer will be late paying credit in the next month. The variables that used to calculate credit scoring are:
<br>
* LIMIT_BAL: Customer's credit limits (in USD)
* SEX: Customer's gender (Man = 1, Woman = 2)
* AGE: Customer's age
* PAY_1: Customer late for first payment (in Month)
* PAY_2: Customer late for second payment (in Month)
* PAY_3: Customer late for third payment (in Month)
* BILL_AMT1: Customer's bill for first payment (in USD)
* BILL_AMT2: Customer's bill for second payment (in USD)
* BILL_AMT3: Customer's bill for third payment (in USD)

The output's result are:
<br>
0 for Customer are predicted not to be late in making credit payments for next month
<br>
1 for Customer are predicted to be late in making credit payments for next month
<br>

## 2. Make server on pythonanywhere
To create a deployment model, we use pythonanywhere to create a server for the model that was created. In pythonanywhere there are two files uploaded, there are:
<br>
* modelcs.pkl: file containing the Random Forest algorithm that used to to predict whether a consumer will be late paying credit in the next month.
* flask_app.py: file used as a "server" file stored in pythonanywhere.

## 3. Instruction for Model Testing
> 1. Download the `request_online.py` file
> 2. Move the file `request_online.py` to the local disk directory D
> 3. Open the Anaconda Prompt
> 4. Type `d:`
> 5. Type `python request_online.py`
> 6. Input the number of observation (number of customer that want to be predict) then click enter
> 7. Input the value of every variable according to the explanation on poin "1. Deploy Model Credit Scoring"
> 8. Always click enter after input the value of every variable
> 9. Complete all the input
> 10. Wait for a few seconds, and the results will appear

## THANK YOU
