# -*- coding: UTF-8 -*-
import numpy as np
import caffe
import os
f = open('/home/hzb/PycharmProjects/cat_dog/test.txt', 'wr')
caffe.set_mode_gpu()
net = caffe.Net('/home/hzb/PycharmProjects/cat_dog/train_test.prototxt',
                '/home/hzb/PycharmProjects/cat_dog/model/solver_iter_100000.caffemodel', caffe.TEST)

path =  '/home/hzb/PycharmProjects/cat_dog/data_cat_dog/mean_file/'
my_path = '/home/hzb/PycharmProjects/cat_dog/data_cat_dog/'
blob = caffe.proto.caffe_pb2.BlobProto()
data = open(path + 'mean.binaryproto' , 'rb' ).read()
blob.ParseFromString(data)
arr = np.array( caffe.io.blobproto_to_array(blob) )
out = arr[0]
np.save(path + 'mean.npy' , out )

mu = np.load(path + 'mean.npy')
mu = mu.mean(1).mean(1)

transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})  # shape要与net中data的shape一致
transformer.set_transpose('data', (2, 0, 1))  # caffe.io.load_image读取jpg图片时，第三维是channel，需要把channel换到第一维
transformer.set_mean('data', mu)  # 减去均值
transformer.set_raw_scale('data', 255)  # python中将图片存储为[0, 1]，而caffe中将图片存储为[0, 255]，所以需要一个转换
transformer.set_channel_swap('data', (2, 1, 0))  # python的图片是RGB格式，而caffe中的是BGR格式，需要进行转置

caffe.set_mode_cpu() #如果只使用CPU，需要这一行，如果使用GPU，则设为GPU
model_def = '/home/hzb/PycharmProjects/cat_dog/deploy.prototxt'   #模型配置文件
model_weights = '/home/hzb/PycharmProjects/cat_dog/model/solver_iter_100000.caffemodel'# #训练好的参数
net = caffe.Net(model_def, model_weights, caffe.TEST)

# img = caffe.io.load_image('/home/hzb/PycharmProjects/cat_dog/data_cat_dog/valset/dog.10533.jpg')  # 加载图片，进行预处理
img = caffe.io.load_image('/home/hzb/PycharmProjects/cat_dog/data_cat_dog/test/11.jpg')  # 加载图片，进行预处理

transformed_img = transformer.preprocess('data', img)

net.blobs['data'].reshape(1, 3, 32, 32)  # 修改net的data的格式，使之与输入匹配（可以修改第一个参数，进行批处理）
net.blobs['data'].data[...] = transformed_img  # 输入
output = net.forward()  # 分类

output_prob = output['prob'][0]  # 读取分类结果
if output_prob.argmax():
   print 'predicted class is dog'
else:
    print 'predicted class is cat'