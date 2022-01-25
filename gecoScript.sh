#!bin/bash

oldTotalSize=0
newTotalSize=0
for i in ~/MiSeq/Arielle/Arielle2016/I_with_primers/*; do
	~/./Programs/geco/src/GeCo $i
	oldFileSize=$(ls -l $i | cut -d " " -f5)
	oldTotalSize=$(($oldTotalSize+$oldFileSize))
	rm $i
	j=$(echo $i".co")
	newFileSize=$(ls -l $j | cut -d " " -f5)
	newTotalSize=$(($newTotalSize+$newFileSize))
done

filesList="filtered_DNA.fa filtered_DNA.fq filtered_RNA.fa filtered_RNA.fq merged_DNA.fq merged_RNA.fq otus_aligned_DNA.fasta otus_aligned_RNA.fasta otus_DNA.fa otus_RNA.fa SILVA_123.1_SSURef_Nr99_tax_silva.fasta SILVA_123_SSURef_Nr99_tax_silva.fasta uniques_DNA.fa uniques_RNA.fa"
cd /home/stovicek_lab/MiSeq/Arielle

for i in $filesList; do
	echo $i
	~/./Programs/geco/src/GeCo $i
	oldFileSize=$(ls -l $i | cut -d " " -f5)
  oldTotalSize=$(($oldTotalSize+$oldFileSize))
	rm $i
	j=$(echo $i".co")
	newFileSize=$(ls -l $j | cut -d " " -f5)
  newTotalSize=$(($newTotalSize+$newFileSize))
done

#~/./Programs/geco/src/GeCo ~/MiSeq/Arielle/Arielle2015/uniques.fa
#rm ~/MiSeq/Arielle/Arielle2015/uniques.fa

oldTotalSizeMB=$(echo "scale = 2; $oldTotalSize/1048576" | bc)
newTotalSizeMB=$(echo "scale = 2; $newTotalSize/1048576" | bc)

echo "Old file size: " $oldTotalSizeMB " MB"
echo "New file size: " $newTotalSizeMB " MB"
diffSize=$(($oldTotalSize-$newTotalSize))
diffSizeMB=$(echo "scale = 2; $diffSize/1048576" | bc)
#echo 'scale = 2; $diffSize / 1048576' | bc
#diffSizeMB=$((bc <<< "scale = 2; ($diffSize/1048576)"))
echo "Space saved: " $diffSizeMB " MB"
sizeFraction=$(echo "scale = 2; $oldTotalSize/$newTotalSize" | bc)
echo "Compression ratio: " $sizeFraction
