import csv
import os
import pandas as pd
import pymysql


def get_data(file):
    connect = pymysql.Connect(
        host="162.105.16.191",
        port=3306,
        user='root',
        passwd='root',
        db='sotorrent20_03',
        charset='utf8'
    )
    cursor = connect.cursor()
    sql = "select * from Posts where locate('<java>',Tags)<>0 limit 10; "
    cursor.execute(sql)
    print("exec finished")
    re = cursor.fetchall()
    fields = cursor.description
    fields = [x[0] for x in fields]
    fp = open(file,"w")
    file_test = pd.DataFrame(columns=fields, data=re)
    file_test.to_csv(file, encoding='utf-8', index=False)
    fp.close()
    cursor.close()
    connect.close()


if __name__ == "__main__":
    file = "java_question.csv"
    get_data(file)