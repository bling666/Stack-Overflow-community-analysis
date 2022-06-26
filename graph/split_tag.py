import pandas as pd

df = pd.read_csv("java_question.csv")
re = {}
for row in df["Tags"]:
    tags = row
    if tags is not None:
        st = tags[1:-1].split("><")
        for item in st:
            if item in re:
                re[item] = re[item]+1
            else:
                re[item] = 1
d_order=sorted(re.items(),key=lambda re:re[1],reverse=True)
print(d_order)