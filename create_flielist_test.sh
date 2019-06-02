# /home/hzb/PycharmProjects/cat_dog/caffes-and-dogs-master sh
DATA=input/test
WORK=input
echo "create test.txt......."
rm -rf $DATA/test.txt
find $DATA -name cat.*.jpg | cut -d '/' -f3 | sed "s/$/ 0/">>$DATA/test.txt
find $DATA -name dog.*.jpg | cut -d '/' -f3 | sed "s/$/ 1/">>$DATA/tmp.txt
cat $DATA/tmp.txt>>$DATA/test.txt
rm -rf $DATA/tmp.txt
mv $DATA/test.txt $WORK/
echo "Done........"
