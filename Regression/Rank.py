# Rank Predictor

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import xlsxwriter 

# Import Datasets
datasets = pd.read_csv("MHTCET.csv")
dataset = np.array(datasets)
# per = datasets.iloc[:,1].values
# rank = datasets.iloc[:,0].values

# For Converting to excel
workbook = xlsxwriter.Workbook('Rank_Predictor.xlsx') 
worksheet = workbook.add_worksheet()  
z = 0
column = 0
row=0
count=0
percentile = 100
per_array=[]
content = ([])
c = 0 
total = 0
    
for j in range(99,0,-1):
    print(z)
    for i in range(0,86820):
        if math.floor(dataset[i][1]) == j:
            count+=1
    num = z
    total += count
    z = z+total
    for k in range(num,z):
        k += c
        if k > 86820:
            break
        if k <= (z):
            content.append(dataset[k])
            c += 9
            # print(dataset[c])
        else:
            break
    print(num ,"......." , z)
    for Rank,PCM,M,P,C in content:
        worksheet.write(row, column, Rank) 
        worksheet.write(row, column+1, PCM) 
        worksheet.write(row, column+2, M) 
        worksheet.write(row, column+3, P) 
        worksheet.write(row, column+4, C) 
        row+=1
    per_array.append(count)
    count=0
    content=[]
workbook.close()
    
    
    
