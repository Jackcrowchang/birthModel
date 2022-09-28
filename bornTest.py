import random


# 出生测试，其中num为有多少对夫妻生育了子女，maxChild为这些夫妻能生育的最大数量子女
def bornTest(num=100, maxChild=5):
    bornOfMale_P = 0.5
    bornOfMale_num = 0
    bornOfFemal_num = 0
    for i in range(num):
        for j in range(maxChild):
            sex = random.random() < bornOfMale_P   # 0为女，1为男
            if sex:
                bornOfMale_num += 1
                break
            else:
                bornOfFemal_num += 1

    print('出生的男孩数量为'+str(bornOfMale_num))
    print('出生的男孩数量为' + str(bornOfFemal_num))
    print('性比比例为'+str(bornOfMale_num/bornOfFemal_num))


bornTest(1000, 4)