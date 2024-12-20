import pickle
from flask import Flask,request 
api=Flask(__name__)

with open('ai.pkl','rb') as f:
    ai=pickle.load(f)

@api.route('/')
def home():
    return "API Server Running"

@api.route('/predict',methods=['GET'])
def predict():
    N=request.args.get('N')
    N=float(n)
    P=request.args.get('P')
    P=float(p)
    K=request.args.get('K')
    K=float(K)
    T=request.args.get('T')
    T=float(Temp)
    H=request.args.get('H')
    H=float(Hum)
    PH= T=request.args.get('PH')
    PH=float(PH)
    R=request.args.get('R')
    R=float(R)
    data=[[N,P,K,T,H,PH,R]]
    response=ai.predict(data)[0]
    return response
if __name__=="__main__":
    api.run(
        host='0.0.0.0',
        port=2000
    )
