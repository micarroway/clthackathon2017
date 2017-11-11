# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 18:29:48 2017

@author: Maritza.Mills

Goal of this file is to train a decision tree model based on Hack_BI_Claims data and Hack_Consumer_data_csv.csvf
Model will accept one row of data input by the user and use that information to estimate costs
"""
import pandas
import numpy as np
from sklearn import tree 
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
    
claims = pandas.read_csv("C:/Users/Micar/Desktop/Hack_BH_Claims_csv.csv", sep=',', header=0)
patients = pandas.read_csv("C:/Users/Micar/Desktop/Hack_Consumer_data_csv.csv", sep=',', header=0)

#some data cleaning
#drop columns we don't need
patientclaims = patients.merge(claims, on=['HackID'], how='inner')
patientclaims = patientclaims.drop(['Diagnosis','total_amount','numberofClaims','HackID'],axis=1)
#need to convert categorical data to numbers
le = preprocessing.LabelEncoder()
le.fit(claims['DiagnosisCode'])    
le.transform(claims['DiagnosisCode'])
x = patientclaims.iloc[:,:-1]
y = patientclaims.iloc[:,-1]
x = x.apply(le.fit_transform)

#putting x and y back together to use later as one dataframe
patientclaims = pandas.concat([x,y],axis=1) 
#print(claims.shape)
#print(x.shape)
#print(y.shape)
#print(claims)

def buildmodel(x,y):
    #choose column with highest correlation(gender, race, ethnicity, diagnosis code, servicesummary)
    #split data set in half by rows, based on that column, for example, use average cost to split everything into two data sets above and below
    #recurse tree
        #recurse tree
            #recurse tree
    #if only one column left, and one row left return answer
    #if only one column left and multiple rows left, take average
    #return new dataframe with trained estimates
    #x = claims.iloc[:,:-1]
    #y = claims.iloc[:,-1]
    healthcareTree = tree.DecisionTreeRegressor()
    healthcareTree.fit(x,y) 
   
    return healthcareTree

def estimatecost(healthcareTree,testx):
    #iterate dataframe to find column most highly correlated with cost
    #numpy correcoef may be useful here
    #return index of best column
    cost = healthcareTree.predict(testx)
    return cost
    
def testAccuracy(data):
    #use input data to search model
    #input will come from front end as user provides information about themselves
    #return closest estimate based on input data, this should be a single Y value
    #X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)
    #print("Accuracy is " + accuracy_score(y_test,y_pred)*100)
    pass

if __name__ == "__main__":
		#for testing
      #[70300,13,607]
      testx = x.iloc[1500,:] #np.random.randn(1, 3))
      
      #textx = testx.reshape(1,-1)
      #print(x)

      model = buildmodel(x,y)
      cost = estimatecost(model,testx)
      print(cost)
      #pass