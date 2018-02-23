# Algorithm for downloading images from iDigBio
###  (all images are verified by experts)

All Diptera occurences from iDigBio are obtained and cleaned to preserve only those that have associated image of the frontal view (head) of the specimens.

### NOTE: to download the same images as in our study use this csv file 

    D1_list_of_filtered_images.csv
    
### Here is the walk trough how we acquired and filtered the images

**Input**: multimedia.csv - a list of records from iDigBio obtained with query keywords ("hasImage":"true" and "order":"diptera")

**Outputs**: images of frontal habitus sorted by family names

Procedure: 

	Step 1.
		collect:
			- images with keywords
				- 'dorsal'
				- 'habitus_dor', 'Habitus_dor'
				- '_D.', "_had"
			- images from institutions that provide mainly dorsal view 
				- 'Denver Museum of Nature & Science'
	            - 'University of Tennessee at Chattanooga (UTC-UTCI)'
	            - 'United States National Museum, Entomology Collections (USNM-USNMENT)'
		skip: 
			- images with keywords: 
				- "lateral", "frontal", "ventral", 'anterior'
				- "head", 'antenna', "labels", 
				- 'mesosoma', "genitalia"
				- "_L", "_F", "_V", 
				- 'web', 'habitus_lat', 'Habitus_lat' 
				- "hed", "hef", "hal", "hed" (head images) 
            - images from institutions that provided fossil images
		check:
			- from records that are not skipped or collected depict images from poorly represented families 
	Step 2.
    	- download images from families with N+ records
		- manually check all the images (to avoid drawings, images of labels, images where head is destroyed, etc.)
        

We ended up with 11 families and 884 images.