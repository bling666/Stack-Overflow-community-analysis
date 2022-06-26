import csv
import os
import pandas as pd
import pymysql

def get_question_comment(question_file,vote_file):
    f = pd.read_csv(question_file)

    connect = pymysql.Connect(
        host="162.105.16.191",
        port=3306,
        user='root',
        passwd='root',
        db='sotorrent20_03',
        charset='utf8'
    )
    cursor = connect.cursor()

    re = []
    for index, row in f.iterrows():
        PostId = row['Id']
        sql = f"select * from Votes where PostId = {PostId}; "
        cursor.execute(sql)
        re_1 = cursor.fetchall()
        re.extend(re_1)
        if index%10000==0:
            print("index="+str(index)+" id="+str(PostId)+" finished")

    fields = cursor.description
    fields = [x[0] for x in fields]
    fp = open(vote_file, "w")
    file_test = pd.DataFrame(columns=fields, data=re)
    file_test.to_csv(vote_file, encoding='utf-8', index=False)
    fp.close()
    cursor.close()
    connect.close()


if __name__ == "__main__":
    question_file = "java_question.csv"
    vote_file = "java_question_vote.csv"
    get_question_comment(question_file,vote_file)