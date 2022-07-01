#!/bin/bash

file_name="data_info.txt"

 > data_info.txt
echo "$file_name content erased"

path="grey_cropped_event_imgs"
# path="cropped_event_imgs"

counter=0
for n in $(ls ${path}/); do 
	for nn in $(ls ${path}/${n}); do 

		echo "$n/$nn $counter" >> data_info.txt; 
		counter=$(($counter+1));
	done
done

echo "$file_name is reinitialized"

