f = open("E:/大四下/毕业论文/log.txt","r")
for i in range(0,4):
    f.readline()
re = {}
for line in f.readlines():
    line = line[:-1]
    node_num,community_num = line.split(":")
    if community_num in re.keys():
        re[community_num] = re[community_num]+1
    else:
        re[community_num] = 1
av = 0
for value in re.values():
    if value>100:
      av = av +1
d_order=sorted(re.items(),key=lambda x:x[1],reverse=True)
print(d_order)
print(len(re))
print(av)

