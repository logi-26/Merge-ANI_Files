'''
merge_ani.py by Logi26 - 2017
Basic Python script to merge all of the .ani animation files in the current directory.
'''
import os

# Lists to store all of the original animation files, combined animation data and all of the output data
animationFileList = []
combinedAnimationList = []
outputDataList = []
combinedAnimationLength = 0

# Get all of the .ANI files from the current directory
for root, dirs, files in os.walk("./"):
    for file in files:
        if file.endswith('.ANI'):
            animationFileList.append(file)

# Create the header for the new ANI file
with open(animationFileList[0]) as f:
	firstData = f.readlines()
firstData = [x.strip() for x in firstData] 

for x in range(0, 31):
	outputDataList.append(firstData[x])	
			
# Loop through all of the original animation data
for animationFile in animationFileList:
	
	# Read the current ANI file	from the list
	with open(animationFile) as f:
		animationData = f.readlines()
	animationData = [x.strip() for x in animationData] 
	
	# Tally up the total animation length for each animation file
	combinedAnimationLength += int(animationData[31])
	
	# Append the animation data to the list
	for x in range(32, len(animationData)):
		combinedAnimationList.append(animationData[x])
	
# Append the combined total animation length to the output data list
outputDataList.append(combinedAnimationLength)

# Loop through all of the combined animation data and append that to the output data list
for data in combinedAnimationList:
	outputDataList.append(data)
	
# Generate the merged ANI file using the data in the output data list
mergedfile = open('merged.ANI', 'w')
for item in outputDataList:
  mergedfile.write("%s\n" % item)
  
mergedfile.close()
