import csv
import os
import pandas as pd
import pymysql


def get_answer(question_file,answer_file):

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
        print(PostId)
        sql = f"select * from Posts where ParentId = {PostId}; "
        cursor.execute(sql)
        print("exec finished")
        re_1 = cursor.fetchall()
        re.extend(re_1)

    fields = cursor.description
    fields = [x[0] for x in fields]
    fp = open(answer_file, "w")
    file_test = pd.DataFrame(columns=fields, data=re)
    file_test.to_csv(answer_file, encoding='utf-8', index=False)
    fp.close()
    cursor.close()
    connect.close()


if __name__ == "__main__":
    question_file = "java_question.csv"
    answer_file = "java_answer.csv"
    get_answer(question_file,answer_file)