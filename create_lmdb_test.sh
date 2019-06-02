# /home/hzb/PycharmProjects/cat_dog sh
DATA=data_cat_dog
WORK=data_cat_dog
TOOLS=/home/hzb/caffe/build/tools

RESIZE=true
if $RESIZE; then
  RESIZE_HEIGHT=32
  RESIZE_WIDTH=32
else
  RESIZE_HEIGHT=0
  RESIZE_WIDTH=0
fi

#echo "Creating train lmdb..."
#rm -rf $DATA/catdog_train_lmdb
#GLOG_logtostderr=1 $TOOLS/convert_imageset \
#   --resize_height=$RESIZE_HEIGHT \
#    --resize_width=$RESIZE_WIDTH \
#    --shuffle \
#    /home/hzb/PycharmProjects/cat_dog/data_cat_dog/train/ \
#    $WORK/train.txt \
#    $DATA/img_train_lmdb

echo "Creating val lmdb..."

#rm -rf $DATA/catdog_test_lmdb
GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    /home/hzb/PycharmProjects/cat_dog/data_cat_dog/valset/ \
    $WORK/test.txt \
    $DATA/img_test_lmdb

echo "Done."
