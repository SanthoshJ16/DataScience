import pandas as pd
class bivariate():
    ## Used to read and import csv data 
    ## returns dt object
    def importDataset():
        dt=pd.read_csv("PrePlacement.csv")
        return dt
        
    ## the below method is used to separate Qualitative and Qunatitative data 
    ## returns qual, quan list
    
    def quanQual(dataset):
        qual=[]
        quan=[]
        for columnName in dataset.columns:
            if(dataset[columnName].dtype=="O"):
                qual.append(columnName)
            else:
                quan.append(columnName)
        return quan, qual
        
    ## the below method is used to find Mean , Median , Mode, Percentile, IQR values
    ## returns descriptive table
    def findUnivariate(dataset,quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","Q4:100%",
                                       "IQR","1.5rule","LowerIQR","HigherIQR","Min","Max"],columns=quan)
        for columnName in quan:
            descriptive.loc["Mean",columnName]=dataset[columnName].mean().item()
            descriptive.loc["Median",columnName]=dataset[columnName].median()
            descriptive.loc["Mode",columnName]=dataset[columnName].mode()[0].item()
            descriptive.loc["Q1:25%",columnName]=dataset.describe()[columnName]["25%"].item()
            descriptive.loc["Q2:50%",columnName]=dataset.describe()[columnName]["50%"].item()
            descriptive.loc["Q3:75%",columnName]=dataset.describe()[columnName]["75%"].item()
            descriptive.loc["Q4:100%",columnName]=dataset.describe()[columnName]["max"].item()
            ## IQR Code changes Starts here
            descriptive.loc["IQR",columnName]=descriptive.loc["Q3:75%",columnName]- descriptive.loc["Q1:25%",columnName]
            descriptive.loc["1.5rule",columnName]=1.5 * descriptive.loc["IQR",columnName]
            descriptive.loc["LowerIQR",columnName]= descriptive.loc["Q1:25%",columnName] - descriptive.loc["1.5rule",columnName]
            descriptive.loc["HigherIQR",columnName]= descriptive.loc["Q3:75%",columnName] + descriptive.loc["1.5rule",columnName]
            descriptive.loc["Min",columnName]=dataset.describe()[columnName]["min"].item()
            descriptive.loc["Max",columnName]=dataset.describe()[columnName]["max"].item()
        return descriptive
        
    ## the below method is used to find outliers on the given data set
    ## returns higher outlier columnName list 
    ## returns lower outlier columnName list 
    def checkforOutliers(descriptive,quan):
        lower=[]
        higher=[]
        for columnName in quan:
            if(descriptive.loc["Min",columnName]<descriptive.loc["LowerIQR",columnName]):
                lower.append(columnName)
            if(descriptive.loc["Max",columnName]>descriptive.loc["HigherIQR",columnName]):
                higher.append(columnName)
        return lower, higher
        
    ## the below method is used to replace lower outliers with lower IQR value in dataset and
    ## is used to replace higher outliers with higher IQR value in dataset
    ## returns dataset
    def replaceOutliersWithIQRValues(dataset,descriptive,lower,higher):
        for columnName in lower:
            dataset.loc[dataset[columnName] < descriptive[columnName]["LowerIQR"],columnName] = descriptive[columnName]["LowerIQR"]
        
        ##Below logic Find values above HigherIQR and replaces them with HigherIQR
        for columnName in higher:
            dataset.loc[dataset[columnName] > descriptive[columnName]["HigherIQR"],columnName] = descriptive[columnName]["HigherIQR"]
        return dataset


    ## Creating a Class for frequency Table for the input Column
    ## returns Frequency Table with data unique values, frequency, Relative Frequency and cumulative relative frequency
    def freqTable(dataset,columnName):
        freqTable=pd.DataFrame(columns=["Unique_Values","Frequency","RelativeFrequency","CumSum"])
        freqTable["Unique_Values"]=dataset[columnName].value_counts().index
        freqTable["Frequency"]=dataset[columnName].value_counts().values
        freqTable["RelativeFrequency"]=freqTable["Frequency"]/103 # 103 is the total occurance
        freqTable["CumSum"]=freqTable["RelativeFrequency"].cumsum()
        return freqTable