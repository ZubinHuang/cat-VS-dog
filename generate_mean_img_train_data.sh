#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
TOOLS=/home/hzb/caffe/build/tools
DATA=/home/hzb/PycharmProjects/cat_dog
rm -rf $DATA/data_cat_dog/mean_file/mean.binaryproto
$TOOLS/compute_image_mean $DATA/data_cat_dog/img_train_lmdb \
  $DATA/data_cat_dog/mean_file/mean.binaryproto
echo "Done."

