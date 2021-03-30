# -*- coding: utf-8 -*-
"""
Created on Oct. 1, 2017
@author: Masker_Li
感谢原神的帮助
"""

import os
import sys

#--------------------------------------------------------------------------------------------
## 运行此脚本前请认真阅读此部分内容。

##！ 需要调整的参数全部在此部分！！！！可调整参数为两道线之间的变量.特别注意文件命名尽量保持统一风格，尤其是最后部分。
## 此脚本只读取.log后缀文件运行并在运行结束后在当前目录下建立sp文件夹并在其中创建.com输入文件。在此之前需确认每个结构都已经计算正确。

# NewMethods 为目标方法和基组信息。需要自己调整。
NewMethodsa= "#p def2tzvpp m062x"
NewMethodsb= "#p 6-31g(d) m062x scrf=(smd,solvent=acetonitrile) stable=opt"
NewMethodsc= "#p 6-31g(d) m062x stable=opt"


# addinput 为定义赝势基组的时候需要用到的额外输入，一般不用改，当自己发现漏了什么元素的时候来调整BasisSet1和BasisSet12部分即可。注意赝势基组会重复一次。
BasisSet1 = [ ] #无赝式输入
BasisSet2 = [ ]
## BasisSet1 = ["-C -H -O -N -P -S -Cl -F -Si -Na -K -B -Li 0\n","6-311+g(d,p)\n","****\n"]
## BasisSet2 = ["-Cu -Pd -I -Cr -Br -Ag -Ni -Ru -Fe -Au 0\n","SDD\n","****\n","\n"]
addinput = BasisSet1 + BasisSet2 + BasisSet2

# nwords 为改文件名（加上后缀名和标点.）时需要删去的字符数,取负数，newexten 为新的文件名最后部分内容
# 比如需要将 abc-ts-1mod.gjf 改为 abc-ts-1o.com，则 nwords = -7，newexten = 'o.com'
nwords = -4
newexten = 'sp.com'

#----------------------------------------------------------------------------------------------

def MKfile(NewName,NewMethods,addinput,ChargeSpinCoordinates,nwords=None,newexten = '.com'):
	#path=os.getcwd();
	#os.chdir(path+"\sp")    #转换目录，进入sp文件夹
	nf = open( NewName, 'w' )  # 重新打开文件
	countent = ["%nprocshared=8\n","%mem=1GB\n",NewMethods,"\n","\n"]
	nf.writelines(countent)
	nf.write(NewName[:-4])
	nf.write("\n")
	nf.write("\n")
	nf.writelines(ChargeSpinCoordinates)

	nf.write("\n")
	nf.writelines(addinput)
	nf.close()
	#os.chdir(path)    #转换目录，返回sp上级文件夹
	return 0
	
def GetWords(fname):
	nCharge = 0
	Index0 = -2
	IndexMax = 0
	Indexend = 0
	IndexCoordinates = -5
	if fname[-5:-4] == 'O':
		nCharge = 2
	Charge = '0'
	Spin = '1'
	Elements = []
	Coordinates = []

	path=os.getcwd()
	fn = os.path.basename(fname)   #获取文件名
	ifile = open( fname, 'r' )
	textlines = ifile.readlines()
	ifile.close()
	for line in textlines :
		IndexMax = max(Index0,IndexMax)
		words = line.split()
		if len(words) > 4:
			if words[0] == 'Charge' and words[1] == '=' and words[3] == 'Multiplicity' and words[4] == '=':
				nCharge += 1
				if nCharge == 4:
					Charge = words[2]
					Spin = words[5]
		if len(words) > 2:
			if nCharge == 4 and words[0] == 'Recover' and words[1] == 'connectivity':
				Indexend += 1
		if nCharge == 4 and Indexend < 1:
			Index0 += 1
			if Index0 >0:
				words1 = line.split(',')
				Elements.append('%-3s'%words1[0])
			#print(Elements)

		if IndexCoordinates > -5 and IndexCoordinates <= IndexMax:
			IndexCoordinates += 1
		if len(words) > 1:
			if nCharge == 4 and Indexend == 1:
				if words[0] == 'Standard' and words[1] == 'orientation:':
					IndexCoordinates = -4
					#print(Index0,Indexend)
				if IndexCoordinates > 0 and Index0 > 0:
					Index0 -= 1
					Coordinates.append('%-13s %13.8f %13.8f %13.8f' %(' ',float(words[3]),float(words[4]),float(words[5])))

	#print(Index0,IndexCoordinates)
	ifile.close()

	ChargeSpinCoordinates = []
	ChargeSpinCoordinates.append(Charge+' '+Spin+'\n')
	for i in range(IndexMax):
		ChargeSpinCoordinates.append(Elements[i]+Coordinates[i]+'\n')
	#print(ChargeSpinCoordinates)
	return ChargeSpinCoordinates

def Check(fname,NewMethods,addinput,nwords,newexten,dirname):
	path=os.getcwd();
	if os.path.isdir(path+"\\"+dirname) == False:    #检查目录中是否有dirname文件夹，如果没有创建一个
		os.mkdir(dirname)
	OldName =os.path.basename(fname);
	if OldName[-4:] == '.log':
		NewName = OldName[:nwords] + newexten;#新的文件名
		#os.mknod(NewName)    #创建新的文件
		#os.rename(OldName,NewName);  #重命名

	if 	os.path.isfile("%s\%s\%s"%(path,dirname,NewName))==True :
		ifile = open( "%s\%s\%s"%(path,dirname,NewName), 'r' )
		textlines = ifile.readlines()
		ifile.close()
		if textlines[2] == NewMethods + "\n":
			print ("%2d  %-30s has already converted!!!" %(n,fname))
	else:
		ChargeSpinCoordinates = GetWords(fname)
		os.chdir(path+"\\"+dirname)    #转换目录，进入sp文件夹
		Result = MKfile(NewName,NewMethods,addinput,ChargeSpinCoordinates,nwords,newexten)
		os.chdir(path)
		if Result == 0:
			print("%2d  %-30s is OK and has converted successfully!" %(n,fname))
		else:
			print("%2d  %-30s is wrong" %(n,fname))
		#print('wowo')


from glob import glob
n=0
print("New NewMethods1 is: %s" %NewMethodsa)
print("New NewMethods2 is: %s" %NewMethodsb)
print("New NewMethods3 is: %s" %NewMethodsc)
print ('')

for eachfile in glob('*.log') :
	n+=1
	Check(eachfile,NewMethodsa,addinput,nwords,newexten,dirname="def2-sp")
	Check(eachfile,NewMethodsb,addinput,nwords,newexten,dirname="SMD-sp")
	Check(eachfile,NewMethodsc,addinput,nwords,newexten,dirname="gas-sp")
    
print ('')
os.system("pause")


