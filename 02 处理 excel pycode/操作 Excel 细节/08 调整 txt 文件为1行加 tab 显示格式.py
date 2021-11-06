import re



# originalFile = r"C:\Users\Lenovo\Desktop\源.txt"
# alteredFile = r"C:\Users\Lenovo\Desktop\源1111.txt"

# original=open(originalFile,'r+')
# text=original.read()
# original.close()

# pattern=r"(\d+\.\s*\w+/?\w*).*\n+"
# newtext=re.sub(pattern,r'\1\t',text)

# altered=open(alteredFile,'w')
# altered.write(newtext)
# altered.close()


def stripFile(oldFName, newFName):
  '''''remove the space or Tab or enter in a file,and output to a new file in the same folder'''
  fp = open(oldFName, "r+")
  newFp = open(newFName, "w")
  for eachline in fp.readlines():
    pattern=r"(\d+\.\s*\w+/?\w*).*\n+"
    newStr = re.sub(pattern, r'\1\t', eachline)
    # newStr = eachline.replace(" ", "").replace("\1\t", "").strip()
    #print "Write:",newStr
    newFp.write(newStr)
  fp.close()
  newFp.close()


if __name__ == "__main__":
  oldName = input("input file name:")
  nameList = oldName.split(".")
  newName = "%s%s%s" % (nameList[0], "_new.", nameList[1])
  stripFile(oldName, newName)
  print("finish output to new file:", newName)


