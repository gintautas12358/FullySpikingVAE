#!/bin/bash

file_name="data_info.txt"

 > data_info.txt
echo "$file_name content erased"

counter=0
for n in $(ls cropped_event_imgs/); do 
	for nn in $(ls cropped_event_imgs/${n}); do 

		echo "$n/$nn $counter" >> data_info.txt; 
		counter=$(($counter+1));
	done
done

echo "$file_name is reinitialized"

