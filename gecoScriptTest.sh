#!bin/bash

oldTotalSize=0
newTotalSize=0

filesList="otus1.fa otus2.fa"
cd ~/MiSeq/TEST

for i in $filesList; do
	echo $i
	~/./Programs/geco/src/GeCo $i
	oldFileSize=$(ls -l $i | cut -d " " -f5)
  oldTotalSize=$(($oldTotalSize+$oldFileSize))
	#rm $i
	j=$(echo $i".co")
	newFileSize=$(ls -l $j | cut -d " " -f5)
  newTotalSize=$(($newTotalSize+$newFileSize))
done

oldTotalSizeMB=$(echo "scale = 2; $oldTotalSize/1048576" | bc)
newTotalSizeMB=$(echo "scale = 2; $newTotalSize/1048576" | bc)

echo "Old file size: " $oldTotalSizeMB " MB"
echo "New file size: " $newTotalSizeMB " MB"
diffSize=$(($oldTotalSize-$newTotalSize))
diffSizeMB=$(echo "scale = 2; $diffSize/1048576" | bc)
#diffSizeMB=$((bc <<< "scale = 2; ($diffSize/1048576)"))
echo "Space saved: " $diffSizeMB " MB"
sizeFraction=$(echo "scale = 2; $oldTotalSize/$newTotalSize" | bc)
echo "Compression ratio: " $sizeFraction
