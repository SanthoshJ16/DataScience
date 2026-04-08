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
        
    