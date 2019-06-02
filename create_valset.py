# -*- coding:utf-8 -*-
__author__ = 'Zubin'

import os
import shutil
import random

root_dir = '/home/hzb/PycharmProjects/cat_dog/data_cat_dog/train/'
output_dir = '/home/hzb/PycharmProjects/cat_dog/data_cat_dog/valset/'
ref = 1

for root, dirs, files in os.walk(root_dir):
    number_of_files = len(os.listdir(root))
    if number_of_files > ref:
        ref_copy = int(round(0.2 * number_of_files))  # 随机筛选20%的图片到新建的文件夹当中
        for i in xrange(ref_copy):
            chosen_one = random.choice(os.listdir(root))
            file_in_track = root
            file_to_copy = file_in_track + '/' + chosen_one
            if os.path.isfile(file_to_copy) == True:
                shutil.copy(file_to_copy, output_dir)
                print file_to_copy
    else:
        for i in xrange(len(files)):
            track_list = root
            file_in_track = files[i]
            file_to_copy = track_list + '/' + file_in_track
            if os.path.isfile(file_to_copy) == True:
                shutil.copy(file_to_copy, output_dir)
                print file_to_copy
print 'Finished !'