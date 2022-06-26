import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
import community as community_louvain
from matplotlib import cm

filename1 = "./java_question.csv"
filename2 = "./java_answer.csv"
df1 = pd.read_csv(filename1)
df2 = pd.read_csv(filename2)

df = pd.merge(df1,df2,left_on="Id",right_on="ParentId")
print("question and answer read in")
H = nx.Graph()
index = 0
for one_item in df.iterrows():
    if np.isnan(one_item[1]["OwnerUserId_x"]) or np.isnan(one_item[1]["OwnerUserId_y"]):
        continue
    question_user = int(one_item[1]["OwnerUserId_x"])
    answer_user = int(one_item[1]["OwnerUserId_y"])
    if not H.has_node(question_user):
        H.add_node(question_user,questions =[])
    if not H.has_node(answer_user):
        H.add_node(answer_user,questions=[])
    if H.has_edge(question_user,answer_user):
        H[question_user][answer_user]["relation"].append({"type":"answer",
        "CreationDate":one_item[1]["CreationDate_y"], "Score":one_item[1]["Score_y"], "Text":one_item[1]["Body_y"]})
    else:
        H.add_edge(question_user, answer_user)
        H[question_user][answer_user]["relation"] = [{"type": "answer",
                                                          "CreationDate": one_item[1]["CreationDate_y"],
                                                          "Score": one_item[1]["Score_y"],
                                                          "Text": one_item[1]["Body_y"]}]
    one_question = {"CreationDate": one_item[1]["CreationDate_x"],
                                          "Score": one_item[1]["Score_x"],
                                          "ViewCount":one_item[1]["ViewCount_x"],
                                          "Body": one_item[1]["Body_x"],
                                          "Title":one_item[1]["Body_x"],
                                          "Tags":one_item[1]["Tags_x"],
                                          "AnswerCount":one_item[1]["AnswerCount_x"],
                                          "CommentCount":one_item[1]["CommentCount_x"],
                                          "FavouriteCount":one_item[1]["FavoriteCount_x"]}
    H.nodes[question_user]["questions"].append(one_question)
print("answer relation finished")
# n_sub_graphs=nx.number_connected_components(H)
# sub_graphs=list(nx.connected_components(H))
#
# print("the num of connected sub graph is "+str(len(sub_graphs)))
# for i,sub_graph in enumerate(sub_graphs):
#     n_nodes=len(sub_graph)
#     print("Subgraph {0} has {1} nodes".format(i,n_nodes))

filename3 = "java_question_comment.csv"
df3 = pd.read_csv(filename3)
df = pd.merge(df1,df3,left_on="Id",right_on="PostId")

for one_item in df.iterrows():
    if np.isnan(one_item[1]["OwnerUserId"]) or np.isnan(one_item[1]["UserId"]):
        continue
    question_user = int(one_item[1]["OwnerUserId"])
    answer_user = int(one_item[1]["UserId"])
    if not H.has_node(question_user):
        H.add_node(question_user,questions =[])
    if not H.has_node(answer_user):
        H.add_node(answer_user,questions=[])
    if H.has_edge(question_user,answer_user):
        H[question_user][answer_user]["relation"].append({"type":"comment",
        "CreationDate":one_item[1]["CreationDate_y"], "Score":one_item[1]["Score_y"], "Text":one_item[1]["Text"]})
    else:
        H.add_edge(question_user, answer_user)
        H[question_user][answer_user]["relation"] = [{"type": "comment",
                                                          "CreationDate": one_item[1]["CreationDate_y"],
                                                          "Score": one_item[1]["Score_y"],
                                                          "Text": one_item[1]["Text"]}]

filename4 = "java_answer_comment.csv"
df4 = pd.read_csv(filename4)
df = pd.merge(df2,df4,left_on="Id",right_on="PostId")

for one_item in df.iterrows():
    if np.isnan(one_item[1]["OwnerUserId"]) or np.isnan(one_item[1]["UserId"]):
        continue
    question_user = int(one_item[1]["OwnerUserId"])
    answer_user = int(one_item[1]["UserId"])
    if not H.has_node(question_user):
        H.add_node(question_user,questions =[])
    if not H.has_node(answer_user):
        H.add_node(answer_user,questions=[])
    if H.has_edge(question_user,answer_user):
        H[question_user][answer_user]["relation"].append({"type":"comment",
        "CreationDate":one_item[1]["CreationDate_y"], "Score":one_item[1]["Score_y"], "Text":one_item[1]["Text"]})
    else:
        H.add_edge(question_user, answer_user)
        H[question_user][answer_user]["relation"] = [{"type": "comment",
                                                          "CreationDate": one_item[1]["CreationDate_y"],
                                                          "Score": one_item[1]["Score_y"],
                                                          "Text": one_item[1]["Text"]}]

print("comment relation finished")

filename5 = "java_question_vote.csv"
df5 = pd.read_csv(filename5)
df = pd.merge(df1,df5,left_on="Id",right_on="PostId")

for one_item in df.iterrows():
    if np.isnan(one_item[1]["OwnerUserId"]) or np.isnan(one_item[1]["UserId"]):
        continue
    question_user = int(one_item[1]["OwnerUserId"])
    answer_user = int(one_item[1]["UserId"])
    if not H.has_node(question_user):
        H.add_node(question_user,questions =[])
    if not H.has_node(answer_user):
        H.add_node(answer_user,questions=[])
    if H.has_edge(question_user,answer_user):
        H[question_user][answer_user]["relation"].append({"type":"vote",
        "CreationDate":one_item[1]["CreationDate_y"], "Score":None, "Text":None})
    else:
        H.add_edge(question_user, answer_user)
        H[question_user][answer_user]["relation"] = [{"type": "comment",
                                                          "CreationDate": one_item[1]["CreationDate_y"],
                                                          "Score": None,
                                                          "Text": None}]

filename6 = "java_answer_vote.csv"
df6 = pd.read_csv(filename6)
df = pd.merge(df2,df6,left_on="Id",right_on="PostId")


for one_item in df.iterrows():
    if np.isnan(one_item[1]["OwnerUserId"]) or np.isnan(one_item[1]["UserId"]):
        continue
    question_user = int(one_item[1]["OwnerUserId"])
    answer_user = int(one_item[1]["UserId"])
    if not H.has_node(question_user):
        H.add_node(question_user,questions =[])
    if not H.has_node(answer_user):
        H.add_node(answer_user,questions=[])
    if H.has_edge(question_user,answer_user):
        H[question_user][answer_user]["relation"].append({"type":"vote",
        "CreationDate":one_item[1]["CreationDate_y"], "Score":None, "Text":None})
    else:
        H.add_edge(question_user, answer_user)
        H[question_user][answer_user]["relation"] = [{"type": "comment",
                                                          "CreationDate": one_item[1]["CreationDate_y"],
                                                          "Score": None,
                                                          "Text": None}]
print("all relations finished")
nx.write_gpickle(H,"./graph.pkl")
partition = community_louvain.best_partition(H)
# for key in partition.keys():
#        print(key,':',partition[key],sep="")
pos = nx.spring_layout(H)
# color the nodes according to their partition
cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
nx.draw_networkx_nodes(H, pos, partition.keys(), node_size=40,cmap=cmap, node_color=list(partition.values()))
nx.draw_networkx_edges(H, pos, alpha=0.5)
plt.savefig("path.png")
