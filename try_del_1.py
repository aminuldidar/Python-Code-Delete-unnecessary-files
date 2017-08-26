import glob, os
filelist = glob.glob("C:/Users/Sophomore/Dropbox/ACM/*.exe")
for f in filelist:
	os.remove(f)
filelist = glob.glob("C:/Users/Sophomore/Dropbox/ACM/*.o")
for f in filelist:
	os.remove(f)