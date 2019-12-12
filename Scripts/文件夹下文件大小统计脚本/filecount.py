import os
import numpy as np
import xlsxwriter
workbook = xlsxwriter.Workbook('Data_Analysis.xlsx')    
worksheet = workbook.add_worksheet() 
worksheet.set_column('A:A', 20)
filename = os.listdir(r'./')
b = [0 for i in range(2632)]
# print b
max = 0
count=0
for file in filename:
	fsize = os.path.getsize(file)/1024
	# print fsize
	count=count+1
	b[fsize]=b[fsize]+1
	if fsize>max:
		max=fsize
	# print fsize/1024
print "Max data is",max/1024
print "Data count is ",count

print "Consequence is",b
# kb



flag=1
for i in b:
	column1="A"+str(flag)
	worksheet.write(column1, flag)
	
	column2="B"+str(flag)
	worksheet.write(column2, i)
	flag=flag+1

workbook.close()