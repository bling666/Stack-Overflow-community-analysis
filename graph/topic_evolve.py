from gensim.corpora import Dictionary
from gensim.models import LdaModel,ldaseqmodel
import networkx as nx
from datetime import datetime
G = nx.read_gpickle("graph.pkl")

f = open("log.txt","r")
for i in range(0,4):
    f.readline()

nodes = []
for line in f.readlines():
    line = line[:-1]
    node_num,community_num = line.split(":")
    if community_num is '11':
        nodes.append(G.nodes[int(node_num)]["questions"])
f.close()

set1 = 0
set2 = 0
set3 = 0
train_set1 = []
train_set2 = []
train_set3 = []
year_num ={}
for node in nodes:
    temp = []
    for one_question in node:
        time = datetime.strptime(one_question["CreationDate"], "%Y-%m-%d %H:%M:%S")
        year = time.date().year
        st = one_question["Tags"][1:-1].split("><")
        for item in st:
            temp.append(item)
        if len(temp) == 0:
            continue
        if year >= 2008 and year<=2012:
            train_set1.append(temp)
        elif year >=2013 and year <= 2016:
            train_set2.append(temp)
        else:
            train_set3.append(temp)

train_set = []
train_set.extend(train_set1)
train_set.extend(train_set2)
train_set.extend(train_set3)
print("train_set is done")
print(train_set1,train_set2,train_set3)
dictionary = Dictionary(train_set)
corpus = [dictionary.doc2bow(text) for text in train_set]

#lda模型训练
lda = ldaseqmodel.LdaSeqModel(corpus=corpus, id2word=dictionary,time_slice=[len(train_set1),len(train_set2),len(train_set3)], num_topics=20)
num_topics = 20
top_topics = lda.top_topics(corpus) #, num_words=20)
lda.print_topic_times(0, top_terms=20)
# Average topic coherence is the sum of topic coherences of all topics, divided by the number of topics.
