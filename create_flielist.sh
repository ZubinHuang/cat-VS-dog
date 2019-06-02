# /home/hzb/PycharmProjects/cat_dog/caffes-and-dogs-master sh
DATA=input/train/
WORK=input
echo "create train.txt..."
rm -rf $DATA/train.txt
find $DATA -name cat.*.jpg | cut -d '/' -f3 | sed "s/$/ 0/">>$DATA/train.txt
find $DATA -name dog.*.jpg | cut -d '/' -f3 | sed "s/$/ 1/">>$DATA/tmp.txt
cat $DATA/tmp.txt>>$DATA/train.txt
rm -rf $DATA/tmp.txt
mv $DATA/train.txt $WORK/
echo "Done..."
