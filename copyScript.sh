#!bin/bash

for i in ~/MiSeq/Eucalyptus/Files/*; do
	cd $i
  for j in $i; do
    cd $j # opening sample folder
		cd Files # opening 'Data'
		cp * ~/MiSeq/Eucalyptus # Listing files in the folder
  done
done
