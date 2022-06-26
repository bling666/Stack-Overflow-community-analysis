import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
from networkx.algorithms import community
filename1 = "./java_question.csv"
filename2 = "./java_answer.csv"
df1 = pd.read_csv(filename1)
df2 = pd.read_csv(filename2)
print(df1.shape[0])
print(df2.shape[0])
df = df1.append(df2)

filename3 = "./java_question_vote.csv"
filename4 = "./java_answer_vote.csv"

df3 = pd.read_csv(filename3)
print(df3.shape[0])

df4 = pd.read_csv(filename4)
print(df4.shape[0])
df_comment = df3.append(df4)


df = pd.merge(df,df_comment,left_on="Id",right_on="PostId")
print(df)
edgeList = []
for QuestionUser,AnswerUser in zip(df["OwnerUserId"],df['UserId']):
    if np.isnan(QuestionUser) or np.isnan(AnswerUser):
        continue
    edgeList.append((QuestionUser,AnswerUser))

H = nx.Graph(edgeList)
print(H.number_of_nodes())
print(H.number_of_edges())

