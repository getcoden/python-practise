import os
files = os.listdir("./")

#print(files)
i = 0

for file in files:

    fileFormat = files[i][files[i].find("."):]
	
    #print(fileFormat)

    fileName = files[i][:files[i].find(".")]
	
    fileName.strip()

    #print(fileName)
    if (fileFormat.strip() == ".txt".strip()):
		
        os.rename(fileName + fileFormat, "2017-学生信息-" + str(i + 1) + fileFormat)
		
    i = i + 1
	
