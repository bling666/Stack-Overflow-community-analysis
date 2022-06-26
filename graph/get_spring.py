import pandas as pd

df = pd.read_csv("E:/大四下/java_question.csv")
re = {}
data_list = df.loc[df['Tags'].str.contains('<spring-boot>')]
data_list['Title'].to_csv("java_spring-boot.csv",header=None,index=False)