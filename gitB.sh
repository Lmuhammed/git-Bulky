#!/bin/bash
  
FILENAME="repos.txt"

LINES=$(cat $FILENAME)

for LINE in $LINES
do
    git clone $LINE
    sleep 1
done
echo "تم نسخ جميع المستودعات ، أظهر للعالم إبداعاتك"
echo "ALl repos SUCCESSFULLY , Make something Geat !"

