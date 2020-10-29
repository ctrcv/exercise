import sys
import math

first_line = sys.stdin.readline().rstrip().split('\t')
# M N d，M是训练集的大小，N是测试集的大小，d是数据维数。
train_size = int(first_line[0])
test_size = int(first_line[1])

train_data = []
train_label = []
for i in range(train_size):
    line = sys.stdin.readline().rstrip().split('\t')
    line = [int(x) for x in line]
    train_data.append(line[1:])
    train_label.append(line[0])

test_data = []
for i in range(test_size):
    line = sys.stdin.readline().rstrip().split('\t')
    line = [int(x) for x in line[1:]]
    test_data.append(line)


# print(train_data, train_label, test_data)

def trainNB(train_data, train_label):
    train_size = len(train_data)
    num_feature = len(train_data[0])
    pAbusive = sum(train_label) / float(train_size)
    p0Num = [1] * num_feature
    p1Num = [1] * num_feature
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(train_size):
        if train_label[i] == 1:
            for j in range(num_feature):
                p1Num[j] += train_data[i][j]
            p1Denom += sum(train_data[i])
        else:
            for j in range(num_feature):
                p0Num[j] += train_data[i][j]
            p0Denom += sum(train_data[i])
    p1Vect = [math.log(x / p1Denom) for x in p1Num]
    p0Vect = [math.log(x / p0Denom) for x in p0Num]
    return p0Vect, p1Vect, pAbusive


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = 0
    p0 = 0
    for i in range(len(vec2Classify)):
        p1 += vec2Classify[i] * p1Vec[i]
        p0 += vec2Classify[i] * p0Vec[i]

    p1 += math.log(pClass1)
    p0 += math.log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


p0V, p1V, pSpam = trainNB(train_data, train_label)
for i in range(test_size):
    print(classifyNB(test_data[i], p0V, p1V, pSpam))
