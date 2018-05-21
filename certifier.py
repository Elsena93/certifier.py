#This is an application to fill pdfs form field
#Yessir

import os
import csv
from fdfgen import forge_fdf

	
def main():
	NAMESLIST = input('Name list(.csv): ')
	PDFORI = input('Original pdf file (.pdf): ')


	names = []
	with open(NAMESLIST, "r") as f:
	        reader = csv.reader(f, delimiter=',')
	        for row in reader:
	                for x in row:
	                        names.append(x)

	numfile = 0

	for i in names:
		fields = [('Name', i)]
		z = i.replace(" ","")
		print('creating {0}.pdf...'.format(z))
		fdf = forge_fdf("",fields,[],[],[])
		fdf_file = open("tmp.fdf","wb")
		fdf_file.write(fdf)
		fdf_file.close()
		cmd = 'pdftk {0} fill_form tmp.fdf output {1}.pdf flatten'.format(PDFORI, z)
		os.system(cmd)
		numfile += 1
		print('{0}.pdf created'.format(z))

	print('END OF PROCESS: {0} FILES CREATED'.format(numfile))

if __name__ == '__main__':
	main()


