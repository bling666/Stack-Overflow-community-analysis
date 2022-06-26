import pandas as pd
filename1 = "./java_question.csv"
filename2 = "./java_answer.csv"
df1 = pd.read_csv(filename1)
df2 = pd.read_csv(filename2)

df = pd.merge(df1,df2,left_on="Id",right_on="ParentId")

temp = df.OwnerUserId_x.value_counts()
print(temp)
temp = df.OwnerUserId_y.value_counts()
print(temp)


df12 = df1.append(df2)
filename3 = "java_question_comment.csv"
df3 = pd.read_csv(filename3)
filename4 = "java_answer_comment.csv"
df4 = pd.read_csv(filename4)
df34 = df3.append(df4)

df = pd.merge(df12,df34,left_on="Id",right_on="PostId")
temp = df.OwnerUserId.value_counts()
print(temp)

temp = df.UserId.value_counts()
print(temp)

filename5 = "java_question_vote.csv"
df5 = pd.read_csv(filename5)
filename6 = "java_answer_vote.csv"
df6 = pd.read_csv(filename6)
df56 = df5.append(df6)
df = pd.merge(df12,df56,left_on="Id",right_on="PostId")
temp = df.OwnerUserId.value_counts()
print(temp)

temp = df.UserId.value_counts()
print(temp)