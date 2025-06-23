import os
import random


trainval_percent = 0.9
train_percent = 0.9
xmlfilepath = r'E:\anaconda3\yolov5-master\dataset\Annotations'
txtsavepath = r'E:\anaconda3\yolov5-master\dataset\images'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open(r'E:\anaconda3\yolov5-master\dataset\ImageSets\trainval.txt', 'w')
ftest = open(r'E:\anaconda3\yolov5-master\dataset\ImageSets\test.txt', 'w')
ftrain = open(r'E:\anaconda3\yolov5-master\dataset\ImageSets\train.txt', 'w')
fval = open(r'E:\anaconda3\yolov5-master\dataset\ImageSets\val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
