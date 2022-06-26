import csv
import os
import pandas as pd
import pymysql
import numpy as np
re = []
fields = []
connect_all = pymysql.Connect(
        host="162.105.16.191",
        port=3306,
        user='root',
        passwd='root',
        db='sotorrent20_03',
        charset='utf8'
    )

def get_user(filename,field_name):
    f = pd.read_csv(filename)
    print(filename)
    connect = pymysql.Connect(
        host="162.105.16.191",
        port=3306,
        user='root',
        passwd='root',
        db='sotorrent20_03',
        charset='utf8'
    )
    cursor = connect.cursor()

    for index, row in f.iterrows():
        UserId = row[field_name]
        if UserId is None or np.isnan(UserId):
            continue
        UserId = int(UserId)
        sql = f"select * from Users where Id = {UserId}; "
        cursor.execute(sql)
        one_user = cursor.fetchall()
        re.extend(one_user)


    cursor.close()
    connect.close()


if __name__ == "__main__":
    question_file = "java_question.csv"
    question_comment_file = "java_question_comment.csv"
    question_vote_file = "java_question_vote.csv"
    answer_file = "java_answer.csv"
    answer_comment_file = "java_answer_comment.csv"
    answer_vote_file = "java_answer_vote.csv"
    cursor = connect_all.cursor()
    sql = f"select * from Users limit 1;"
    cursor.execute(sql)
    fields = cursor.description
    fields = [x[0] for x in fields]
    get_user(question_file,"OwnerUserId")
    get_user(question_comment_file,"UserId")
    get_user(question_vote_file,"UserId")
    get_user(answer_file,"OwnerUserId")
    get_user(answer_comment_file,"UserId")
    get_user(answer_vote_file,"UserId")
    user_file = "java_user.csv"

    file_test = pd.DataFrame(columns=fields, data=re)
    file_test.to_csv(user_file, encoding='utf-8', index=False)
