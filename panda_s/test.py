# importing pandas module
import pandas as pd 
   
# Define a dictionary with column A
data1 = {'A': [1, 2]} 
     
# Define another dictionary with column B
data2 = {'B': ['a', 'b', 'c']}  
   
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1, index =[0, 1])
print('df: ', df)
   
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2, index =[2, 3, 4]) 
print('df1: ', df1)
  
# Now to perform cross join, we will create
# a key column in both the DataFrames to 
# merge on that key.
df['key'] = 1
df1['key'] = 1

# to obtain the cross join we will merge 
# on the key and drop it.
result = pd.merge(df, df1, on ='key').query('A<=1')
print('result: ', result)
