
import sys
import os
path = sys.argv[1]

ignore = []
for line in open("ignore.txt", "r"):
	ignore.append(line)
print(ignore)

print("checking the folder " + path)

def check(fileName):
	global ignore
	for d in ignore:
		if d.rstrip() in fileName:return False
	return True

def countLines(file):
	n = 0

	for line in open(file, "r"):
		n += 1
	return n


def countLinesInFolder(p):
	global ingore
	files = os.listdir(p)
	total = 0
	print("filing :  " + p)
	print("--------------")
	for file in files:
		print(file)
		# if file == ".DS_Store" or file == "p5.js" or file == "brief.js" or file == "brief_compressed.js" or ".wav" in file or ".mp3" in file or ".jpg" in file or ".png" in file : 
		if not check(file):
			print("skipping file : " + file + " at : " + str(total))
			continue

		if "." in file:total += countLines(p + "/"+ file)
		else : total += countLinesInFolder(p + "/" +file)
	return total


print("----------------------------------------"+ "\ntotal number of lines : " + str(countLinesInFolder(path)))