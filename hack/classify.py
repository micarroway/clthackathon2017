# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 18:29:48 2017

@author: Maritza.Mills

Goal of this file is to train a decision tree model based on Hack_BI_Claims data and Hack_Consumer_data_csv.csvf
Model will accept one row of data input by the user and use that information to estimate costs
"""
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hack.settings")
django.setup()
import pandas
from sklearn import tree 
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from api.models import *
import numpy as np

claims = pandas.read_csv("/Users/jurobn/code/clthackathon2017/Hack_BH_claims_csv.csv", sep=',', header=0)
patients = pandas.read_csv("/Users/jurobn/code/clthackathon2017/Hack_Consumer_data_csv.csv", sep=',', header=0)
p = Patient.objects.latest('PatientId')
diag = Diagnosis.objects.latest('DiagnosisId')
#some data cleaning
#drop columns we don't need
patientclaims = patients.merge(claims, on=['HackID'], how='inner')
patientclaims = patientclaims.drop(['Diagnosis','total_amount','numberofClaims','HackID'],axis=1)
#need to convert categorical data to numbers
le = preprocessing.LabelEncoder()
x = patientclaims.iloc[:,:-1]
y = patientclaims.iloc[:,-1]
x = x.apply(le.fit_transform)

#putting x and y back together to use later as one dataframe
patientclaims = pandas.concat([x,y],axis=1)
xtrain, xtest, ytrain, ytest = train_test_split( x, y, test_size = 0.1, random_state = 100)
#print(claims.shape)
#print(x.shape)
#print(y.shape)
#print(claims)

def buildmodel(x,y):
    #use decision tree regressor to build a model that predicts estimated healthcare cost based on X values
    healthcareTree = tree.DecisionTreeRegressor(presort=True)
    healthcareTree.fit(x,y)

    return healthcareTree

def estimatecost(healthcareTree,x):
    #use our model to predict healthcare cost for a given set of X values
    cost = healthcareTree.predict(x)
    return cost

def calcsummaryinfo(gender,race,ethnicity,service,diagnosis):
    pass

def testAccuracy(model):
    #use input data to search model
    #input will come from front end as user provides information about themselves
    #return closest estimate based on input data, this should be a single Y value
    #y_pred = model.predict(X_test)
    print("Accuracy is...")
    print(model.score(x,y)*100)

if __name__ == "__main__":

      model = buildmodel(xtrain,ytrain)
      cost = estimatecost(model,xtest)
      print(cost)

      testAccuracy(model)
      #pass