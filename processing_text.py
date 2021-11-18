k = []
with open('test2.txt', 'r') as f:
    for a in f:
        k.append(a)
# print('文档txt:', k)#将txt变成列表保存在k

x = dict(name=str(k[1][:-1]), lei=str(k[2][:-1]))#先将没有变动的name和lei创建成字典
# print('字典x:', x)

k_change = k[3:]#将title和isin合成一个列表
# print('变动的部分k_change:', k_change)

isic = []
p = 0
w = 0
for i in k_change:#计算有几个title，每个title下有几个isin
    if i[0:2] != 'LU':
        w += 1
        isic.append(p)
        p = 0
    if i[0:2] == 'LU':
        p += 1
# print('一共有', w-1, '组title')#此时print(i)可以发现最后一个i == '''，所以title的个数=w-1
# print('每个title下isic个数:(第一个0不计入)', isic)

k_c = []#去掉'\n'，重新建立一个列表
for i in k_change:
    k_c.append(i[:-1])
# print(k_c)

l = len(k_c)
# print(l)
sub_fund = []
i = 0
j = 0
while i < l-1:#此时可以发现最后一个l == '''，所以长度为l-1
    sub_fun = dict()
    sub_fun['title'] = str(k_c[i])
    sub_fun['isic'] = str(k_c[i+1:i+1+isic[j+1]])
    # print('sub_fun:', sub_fun)#isic列表下的每个字典
    sub_fund.append(sub_fun)
    # print('sub_fund:', sub_fund)
    i = i+1+isic[j+1]
    j += 1
# print(sub_fund)

x['sub_fund'] = sub_fund#将sub_fund
print(x)