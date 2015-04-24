'''
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
import uuid
import compiler
from math import *
import re
from scipy.optimize import curve_fit
import mlpy
from scipy.cluster.vq import kmeans,vq

'''
#This is a test method to see if numpy works and if data can be passed to this file's function
'''
def testAnalytics(query):
    return query + " reached analytics file"

'''
#1.  Parses the input file. 
#2.  Format should be : values separted by commas for each input. Inputs are separted by ';'
#3.  The supervised flag denotes if learning is supervised or unsupervised
#4.  If supervised, The last entry of each entry is assumed to be the output/label.
#5.  If values are not convertible to floats or length of inputs are different, then two empty lists are returned. 
#6.  Else one list(unsupervised)/two lists x and y(supervised) are returned
'''
def parseFile(filename,supervised):
    incorrectFormat = False #incorrect input flag
    x = [] #features
    y = [] #outputs
    with open(filename,'r+') as source:    
        for line in source:
            input = line.split(';')#there should ideally be just one line
            for counter in range(0,len(input)):
                currElement = input[counter].split(',')#split each element
                xTemp = []
                yTemp = []
                if supervised:
                    for counterElement in range(0,len(currElement)-1):#iterate till 1 before the final element. That element is output
                        try:
                            xTemp.append(float(currElement[counterElement]))
                        except ValueError:
                            incorrectFormat = True #if conversion was not possible
                    try:
                        yTemp.append(float(currElement[len(currElement)-1]))
                    except ValueError:
                        incorrectFormat = True 
                    if not incorrectFormat:
                        x.append(xTemp)
                        y.append(yTemp)
                else:
                    for counterElement in range(0,len(currElement)):#iterate till end as there is no y value
                        try:
                            xTemp.append(float(currElement[counterElement]))
                        except ValueError:
                            incorrectFormat = True #if conversion was not possible
                    if not incorrectFormat:
                        x.append(xTemp)

        #before returning, check if all features are of the same length or not
        lengthToCheck = len(x[0])
        for element in x:
            if len(element)!=lengthToCheck:
                incorrectFormat = True
        if not incorrectFormat:
            return x
        else:
            #check length when received. If length is 0, something was wrong.
            return []

'''
#Creates a unique Filename
'''
def getFilename():
    #return filename
    return str(uuid.uuid4())

'''
#learns a linear regression model over the data. If there is an error in parsing the file,
#returns empty list. Otherwise returns coefficients and intercept with filename of plotted image
'''
def linearRegressionLearn(filename):
    x,y = parseFile(Filename)
    if len(x) == 0 or len(y) == 0:
        return []
    else:
        # Create linear regression object
        regr = linear_model.LinearRegression()
        # Train the model using the training sets
        regr.fit(x,y)
        #generate plot of the fitted model. Only possible for 2D data
        if len(x[0])==1:    
            plt.scatter(x,y,color='black')
            plt.plot(x, regr.predict(x), color='blue',linewidth=3)
            plt.xticks(())
            plt.yticks(())
            #generate a filename
            filename = getFilename()+".png" 
            plt.savefig(filename)
            return [regr.coef_,regr.intercept_,filename]
        else:
            return [regr.coef_,regr.intercept_]

'''
#learns a non-linear regression model over the data. If there is an error in parsing the file,
#returns empty list. Otherwise returns coefficients and intercept with filename of plotted image
#Currently only 1D features can be handled using the model y = a + b*x+ c*x**2
'''
def nonLinearRegressionLearn(filename):
    x=[]
    y=[]
    incorrectFormat = False
    xTemp,yTemp = parseFile(filename,False)
    for element in xTemp:
        if len(element[0]!=1):
            incorrectFormat = True
        x.append(element[0])
    for element in yTemp:
        if len(element[0]!=1):
            incorrectFormat = True
        y.append(element[0])
    if not incorrectFormat:
        parameters, paramCov = curve_fit(pevalNonLinearReg,x,y)
        #give inputs from 0 to 1000 at the moment
        testx = [random.random() for _ in range(0, 1000)]
        testxArray = np.array(testx)
        predictedPoly = []
        for element in testx:
            predictedPoly.append(peval(element,parameters[0],parameters[1],parameters[2]))
        # Plot outputs
        pl.scatter(X,Y,  color='red', s = 5)
        pl.scatter(testx,predictedPoly,  color='black', s = 1)
        filenameToSave = getFilename()+".png" 
        plt.savefig(filenameToSave)
        pl.savefig(filenameToSave)
        return [parameters, paramCov, filenameToSave]
    else:
        return []

'''
#return evaluated value for x
'''
def pevalNonLinearReg(x,a,b,c):
    #return evaluated value for x
    return a + b*x+ c*x**2

'''
#Does Logistic regression and returns weights for the input variables
'''
def logisticRegressionLearn(filename):
    x,yTemp = parseFile(filename,False)
    y = []
    for element in yTemp:
        y.append(element[0])
    logisticReg = mlpy.LibLinear(solver_type='l1r_lr')
    logisticReg.learn(x,y)
    weights = logisticReg.w()
    return weights

'''
#Does k-means clustering on the data and returns 
'''
def kMeansLearn(filename,k):
    x = parseFile(filename,False)
    xArr = np.array(x)
    cent,var = kmeans(xArr,k)
    return cent,var
   
'''
