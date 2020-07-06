import pickle
from flask import Flask, render_template, request
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
filename="car_price_model.pkl"
model=pickle.load(open(filename,'rb'))
app = Flask(__name__)

#app.config['SEND_FILE_MAX_AGE_DEFAULT']=0

@app.route('/')
def home():
   return render_template('home.html')
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if(request.method == 'POST'):
      Present_Price=float(request.form['Present_Price'])
      Kms_Driven=int(request.form['Kms_Driven'])
      Owner=int(request.form['hm'])
      Year=int(request.form['Year'])
      no_year=2020-Year
      fule=str(request.form['fule_type'])
      if(fule=='petrol'):
         Fuel_Type_Diesel=0
         Fuel_Type_Petrol=1
      elif(fule=='cng'):
         Fuel_Type_Diesel=0
         Fuel_Type_Petrol=0
      else:
         Fuel_Type_Diesel=1
         Fuel_Type_Petrol=0
      seller=str(request.form["di"])
      if(seller=='individual'):
         Seller_Type_Individual=1
      else: Seller_Type_Individual=0
      transmission=str(request.form['tt'])
      if(transmission=='manual'):
        Transmission_Manual=1
      else: Transmission_Manual=0
      pred=model.predict([[Present_Price, Kms_Driven, Owner, no_year, Fuel_Type_Diesel,Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual]])
      output=str(round(pred[0],2))
      return render_template('home.html',val="Predicted price is "+output+" lakh")

if __name__ == '__main__':
   app.run(debug = True)
