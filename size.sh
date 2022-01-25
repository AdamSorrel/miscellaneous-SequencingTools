#!bin/bash

totalSize=0

for i in ~/MiSeq/Programs/*; do
	fileSize=$(ls -l $i | cut -d " " -f5)
  totalSize=$(totalSize + fileSize)
done
