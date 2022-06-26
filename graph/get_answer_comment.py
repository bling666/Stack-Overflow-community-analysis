import csv
import os
import pandas as pd
import pymysql

def get_answer_comment(answer_file,comment_file):
    f = pd.read_csv(answer_file)

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
        sql = f"select * from Comments where PostId = {PostId}; "
        cursor.execute(sql)
        re_1 = cursor.fetchall()
        re.extend(re_1)
        if index % 10000 == 0:
            print("index=" + str(index) + " id=" + str(PostId) + " finished")

    fields = cursor.description
    fields = [x[0] for x in fields]
    fp = open(comment_file, "w")
    file_test = pd.DataFrame(columns=fields, data=re)
    print(file_test)
    file_test.to_csv(comment_file, encoding='utf-8', index=False)
    fp.close()
    cursor.close()
    connect.close()


if __name__ == "__main__":
    answer_file = "java_answer.csv"
    comment_file = "java_answer_comment.csv"
    get_answer_comment(answer_file,comment_file)