# Stack-Overflow-community-analysis

## 介绍

Stack Overflow作为广受欢迎的计算机领域的问答社区，积累了许多计算机领域的知识和经验，学习者可以将Stack Overflow中相关问题作为特殊的学习资源。然而对于想要通过Stack Overflow中丰富的知识和经验进行学习的学习者而言，Stack Overflow中知识分布杂乱，学习过程不具有连续性，通过现有的搜索机制以及筛选条件难以迅速获得感兴趣的学习资源。

为了解决这一问题，本文设计和实现了一种学习资源推荐系统。基于Stack Overflow中的用户以及问答数据建立了用户-用户网络，本文刻画了Stack Overflow中用户之间的关系。然后，本文利用社群检测算法识别出具有参考价值的相似用户群体，借助主题建模分析各个社群中主题关键词的演变情况，为用户的学习提供成熟的学习路径，推荐相应的学习资源。

本文首先对于Stack Overflow相关的各种网络研究、主题建模、资源推荐等相关工作进行了分析，探讨其共同的关注点以及不足之处。随后，本文详细介绍了用户-用户网络构建、社群检测以及主题建模算法的设计和实现流程。之后，本文基于面向对象的分析设计方法对系统进行了分析和设计，并阐述了客户端和服务器端的设计和实现。最后本文通过算法验证以及案例研究验证了系统的可行性和有效性。

Stack Overflow, as a popular Q&A community of computer science, has accumulated a lot of knowledge and experience in this field, and learners can use relevant questions from Stack Overflow as special learning resources. However, for learners who want to learn from the rich knowledge and experience in Stack Overflow, the knowledge distribution in Stack Overflow is chaotic, and the learning process is not continuous, so it is difficult for learners to get the wanted learning resources quickly through the existing search mechanism and filtering conditions.

In order to solve this problem, this thesis designs and implements a learning resource recommendation system. Based on the users and Q&A data in Stack Overflow, a social network graph is established to portray the relationship between users in Stack Overflow. At the same time,  the thesis uses community detection algorithms to identify similar user groups, analyzes the evolution of topic keywords in each community with the help of topic modeling, provides mature learning paths for users' learning, and recommends corresponding learning resources.

In this thesis, we first analyze the work related to Stack Overflow's network mapping research, topic modeling, and resource recommendation, and discuss their common concerns and shortcomings. Then, this thesis describes in detail the design and implementation process of social network graph construction, community detection and topic modeling algorithms. After that, this thesis analyzes and designs the system based on the object-oriented analysis and design method, and describes the design and implementation of the client and server. Finally, this thesis verifies the feasibility and effectiveness of the system through algorithm verification and case studies.


流程图如下

![](https://github.com/bling666/Stack-Overflow-community-analysis/blob/main/img/%E6%B5%81%E7%A8%8B%E5%9B%BE.png)

## 实现页面

![](https://github.com/bling666/Stack-Overflow-community-analysis/blob/main/img/%E4%B8%BB%E9%A1%B5%E9%9D%A2.png)
