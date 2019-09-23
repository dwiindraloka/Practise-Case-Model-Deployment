import requests
import json

# URL
url = 'https://dwiindraloka.pythonanywhere.com/api'

x = input('INPUT THE NUMBER OF OBSERVATION: ')
print("")
y = int(x)
r1 = []
# Code for inputting the variables
for i in range (0, y):
    print("PLEASE INPUT THE VALUES OF SOME VARIABLES BELLOW FOR PESRON", i+1)
    a = input('LIMIT_BAL (IN USD): ')
    b = input('SEX (MAN = 1, WOMAN = 2): ')
    c = input('AGE: ')
    d = input('PAY_1 (LATE PAYMENT IN MONTH): ')
    e = input('PAY_2 (LATE PAYMENT IN MONTH): ')
    f = input('PAY_3 (LATE PAYMENT IN MONTH): ')
    TOTAL_TIME_PAY = int(d) + int(e) + int(f)
    h = input('BILL_AMT1 (IN USD): ')
    i = input('BILL_AMT2 (IN USD): ')
    j = input('BILL_AMT3 (IN USD): ')
    BILL1_PER_LIMIT = int(h) / int (a)
    BILL2_PER_LIMIT = int(i) / int (a)
    BILL3_PER_LIMIT = int(j) / int (a)
    print("")
    user = {'a':float(a),'b':float(b),'c':float(c),'d':float(d),'e':float(e),'f':float(f), 'g':float(TOTAL_TIME_PAY),'h':float(BILL1_PER_LIMIT),'i':float(BILL2_PER_LIMIT),'j':float(BILL3_PER_LIMIT)}
    r1.append(user)
r = requests.post(url, json = (r1))
r = r.json()
if y == 1:
    print("RESULT: ")
else:
    print("RESULTS: ")
for i in r:
    print(i)