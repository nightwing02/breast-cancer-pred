from flask import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

import pickle
with open('fpmodel_pkl' , 'rb') as f:
    rg = pickle.load(f) #rg is the whole dataframe from the model
app = Flask(__name__) #creating the Flask class object

predacc=round(rg[1]*100,2) #predicated data
#assign columns to the data acc to their index
data={'worst_concaveps':rg[2],'worst_radius':rg[3],'worst_perimeter':rg[4],'mean_concaveps':rg[5],'mean_perimeter':rg[6],'mean_radius':rg[7],'worst_area':rg[8],'mean_concavity':rg[9],'mean_area':rg[10],'worst_concave':rg[11],'worst_texture':rg[12]}
#data have all the important features of dataset
@app.route('/') #decorator defines the   
def home():  
    return render_template("predpage.html",mydata=list(data.items()))


@app.route('/pred',methods=['GET','POST']) #decorator defines the   
def pred():
    #request data from the user form
    wcp=request.form['wcp']
    wr=request.form['wr']
    wp=request.form['wp']
    mcp=request.form['mcp']
    mp=request.form['mp']
    mr=request.form['mr']
    wa=request.form['wa']
    mc=request.form['mc']
    ma=request.form['ma']
    wc=request.form['wc']
    wt=request.form['wt']
    
    pred=[float(wcp),float(wr),float(wp),float(mcp),float(mp),float(mr),float(wa),float(mc),float(ma),float(wc),float(wt)]
   
    
    prediction=rg[0].predict([pred])[0]
    print(prediction)
    print(predacc)

    return render_template("predpage.html",mydata=list(data.items()),pred=prediction,acc=predacc)

if __name__ =='__main__':  
    app.run(debug = True)