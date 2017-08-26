#exec(open('C:/Users/Sophomore/Dropbox/APythonCode/del_file.py').read())

import glob, os
fold=['Sophomore','aislam']
lstIndx=['*.exe', '*.o', '*.txt'] 		# multiple file format
total=0
for x in fold:
	for evryLoc in lstIndx:
		locname="C:/Users/" + x + "/Dropbox/ACM/" + evryLoc
		filelist = glob.glob(locname)
		total=total+len(filelist)
		#print(total)
		for f in filelist:
			os.remove(f)
print("Total file deleted: ", total)
