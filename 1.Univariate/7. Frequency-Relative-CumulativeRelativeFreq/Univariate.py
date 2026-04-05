class Univariate():
    def quanQual(dataset):
        qual=[]
        quan=[]
        for columnName in dataset.columns:
            if(dataset[columnName].dtype=="O"):
                qual.append(columnName)
            else:
                quan.append(columnName)
        return quan, qual
    def freqTable(dataset,columnName):
        freqTable=pd.DataFrame(columns=["Unique_Values","Frequency","RelativeFrequency","CumSum"])
        freqTable["Unique_Values"]=dataset[columnName].value_counts().index
        freqTable["Frequency"]=dataset[columnName].value_counts().values
        freqTable["RelativeFrequency"]=freqTable["Frequency"]/103 # 103 is the total occurance
        freqTable["CumSum"]=freqTable["RelativeFrequency"].cumsum()
        return freqTable
    def univariate(dataset,quan):
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