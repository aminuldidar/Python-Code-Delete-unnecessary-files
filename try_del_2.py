import glob, os
fold=['Sophomore','aislam']  # multiple user account
for x in fold:
	locname=["C:/Users/" + x + "/Dropbox/ACM/*.exe", "C:/Users/" + x + "/Dropbox/ACM/*.o"];
	for evryLoc in locname:
		filelist = glob.glob(evryLoc)
		for f in filelist:
			os.remove(f)
