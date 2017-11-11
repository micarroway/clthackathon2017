# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 18:29:48 2017

@author: Maritza.Mills

Goal of this file is to train a decision tree model based on Hack_BI_Claims data and Hack_Consumer_data_csv.csvf
Model will accept one row of data input by the user and use that information to estimate costs
"""
import csv
import pandas
import numpy as np


claims = pandas.read_csv("C:/Users/Micar/Desktop/Hack_BH_Claims_csv.csv", sep=',', header=0)
patients = pandas.read_csv("C:/Users/Micar/Desktop/Hack_Consumer_data_csv.csv", sep=',', header=0)
#print(claims)
#print(patients)
#with open('C:/Users/Micar/Desktop/Hack_BH_Claims_csv.csv') as csvfile:

def buildmodel(self,claims):
    #choose column with highest correlation(gender, race, ethnicity, diagnosis code, servicesummary)
    #split data set in half by rows, based on that column, for example, use average cost to split everything into two data sets above and below
    #recurse tree
        #recurse tree
            #recruse tree
    #if only one column left, and one row left return answer
    #if only one column left and multiple rows left, take average
    #return new dataframe with trained estimates

def chooseColumn(self,claims):
    #iterate dataframe to find column most highly correlated with cost
    #numpy correcoef may be useful here
    #return index of best column
    
def searchmodel(self,data):
    #use input data to search model
    #input will come from front end as user provides information about themselves
    #return closest estimate based on input data, this should be a single Y value
    
    