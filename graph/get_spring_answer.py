import pandas as pd

df = pd.read_csv("E:/大四下/java_answer.csv")
re = {}
data_list = df.loc[df['ParentId']==8569]
data_list['Body'].to_csv("java_spring_answer.csv",index=False,header=None)