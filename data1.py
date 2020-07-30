import pandas as pd 
from pandas_profiling import ProfileReport
df=pd.read_csv('datacsv.csv')
print(df)
profile=ProfileReport(df,minimal=True)
profile.to_file(output_file="report.html")

