import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms import community
import pandas as pd
import numpy as np

filename = "./re_Q&A.csv"
df = pd.read_csv(filename)

edgeList = []
for QuestionUser,AnswerUser in zip(df['OwnerUserId'],df['OwnerUserId.1']):
    if np.isnan(QuestionUser) or np.isnan(AnswerUser):
        continue
    edgeList.append([int(QuestionUser),int(AnswerUser)])
H = nx.Graph(edgeList)

c = list(community.k_clique_communities(H,2))
print(len(c))
print(c)