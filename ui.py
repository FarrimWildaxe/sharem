import sys
import re

def showOptions():
	options = "\nOptions:\n"
	options +="h: Display options.\n"
	options +="i: Show PE file info.\n"
	options +="p: Print menu.\n"
	options +="q: Quick find all.\n"
	options +="s: Find shellcode instructions.\n"
	options +="k: Find strings.\n"
	options +="j: Find shellcode strings.\n"
	options +="m: Find InMemoryOrderModuleList.\n"
	options +="e: Find imports\n"
	options +="o: Output bins and ASCII text.\n"
	options +="b: Change bits.\n"
	options +="x: Exit\n"
	print(options)

def printBitMenu():
	bitMenu = "\nChange bits:\n"
	bitMenu +="Enter 32 or 64: "
	print(bitMenu)

def displayCurrentInstructions(bPushRet, bCallPop, bFstenv, bEgg, bHeaven, bPEB, bAll): #Display current shellcode instruction selections
	info = ''
	info = "Shellcode instructions:\n"
	info += "\tpr - Push ret\t\t\t[" 
	info += "x" if bPushRet else " "
	info += "]\n"
	info += "\tcp - Call pop / GetPC\t\t[" 
	info += "x" if bCallPop else " "
	info += "]\n"
	info += "\tfe - Fstenv / GetPC\t\t[" 
	info += "x" if bFstenv else  " "
	info += "]\n"
	info += "\tsy - Windows syscall\t\t[" 
	info += "x" if bEgg else " "
	info += "]\n"
	info += "\thg - Heaven's gate\t\t[" 
	info += "x" if bHeaven else " "
	info += "]\n"
	info += "\tpb - Walking the PEB\t\t[" 
	info += "x" if bPEB else " "
	info += "]\n"
	info += "\tall - All selections\t\t["
	info += "x" if bAll else " "
	info += "]\n\t\t*Default\n\n"
	# info += "Toggle choices by entering input.\n"
	print(info)

def displayCurrentSelections(bpPushRet, bpCallPop, bpFstenv, bpSyscall, bpHeaven, bpPEB, bpStrings, bpEvilImports, bpModules, bpPushStrings, bpAll): #Displays current print selections
	iMenu = "Selections to print:\n"
	iMenu += "\tpr - Push ret\t\t\t[" 
	iMenu += "x" if bpPushRet else " "
	iMenu += "]\n"
	iMenu += "\tcp - Call pop / GetPC\t\t[" 
	iMenu += "x" if bpCallPop else " "
	iMenu += "]\n"
	iMenu += "\tfe - Fstenv / GetPC\t\t[" 
	iMenu += "x" if bpFstenv else  " "
	iMenu += "]\n"
	iMenu += "\tsy - Windows syscall\t\t[" 
	iMenu += "x" if bpSyscall else " "
	iMenu += "]\n"
	iMenu += "\thg - Heaven's gate\t\t[" 
	iMenu += "x" if bpHeaven else " "
	iMenu += "]\n"
	iMenu += "\tpb - Walking the PEB\t\t[" 
	iMenu += "x" if bpPEB else " "
	iMenu += "]\n"
	iMenu += "\tim - Imports\t\t\t[" 
	iMenu += "x" if bpEvilImports else " "
	iMenu += "]\n"
	iMenu += "\tlm - Loaded modules\t\t[" 
	iMenu += "x" if bpModules else " "
	iMenu += "]\n"
	iMenu += "\tst - Strings \t\t\t["
	iMenu += "x" if bpStrings else " "
	iMenu += "]\n"
	iMenu += "\tps - Push Stack Strings \t["
	iMenu += "x" if bpPushStrings else " "
	iMenu += "]\n"
	iMenu += "\tall - All selections\t\t["
	iMenu += "x" if bpAll else " "
	iMenu += "]\n\t\t*Default\n\n"
	print(iMenu)

#ui Discover Menu text
def instructionsMenu(bPushRet, bCallPop, bFstenv, bEgg, bHeaven, bPEB, bAll):
	iMenu = "\n"
	iMenu += "Selections to find:\n"
	iMenu += "\tpr - Push ret\t\t\t[" 
	iMenu += "x" if bPushRet else " "
	iMenu += "]\n"
	iMenu += "\tcp - Call pop / GetPC\t\t[" 
	iMenu += "x" if bCallPop else " "
	iMenu += "]\n"
	iMenu += "\tfe - Fstenv / GetPC\t\t[" 
	iMenu += "x" if bFstenv else  " "
	iMenu += "]\n"
	iMenu += "\tsy - Windows syscall\t\t[" 
	iMenu += "x" if bEgg else " "
	iMenu += "]\n"
	iMenu += "\thg - Heaven's gate\t\t[" 
	iMenu += "x" if bHeaven else " "
	iMenu += "]\n"
	iMenu += "\tpb - Walking the PEB\t\t[" 
	iMenu += "x" if bPEB else " "
	iMenu += "]\n"
	iMenu += "\tall - All selections\t\t["
	iMenu += "x" if bAll else " "
	iMenu += "]\n\t\t*Default\n\n"
	iMenu += "\nh - Show options.\n"
	iMenu += "g - Toggle selections.\n"
	iMenu += "c - Clear all selections.\n"
	iMenu += "s - Change technical setttings for finding shellcode instructions.\n"
	iMenu += "z - Find instructions.\n"
	iMenu += "r - Reset found instructions.\n"
	iMenu += "x - Exit.\n"
	print(iMenu)

def instructionSelectMenu():
	iSMenu = "\n\n...................\n"
	iSMenu += "Toggle Instructions"
	iSMenu += "\n...................\n"
	iSMenu += "Enter each instruction set code to toggle, delimitied by a space.\n"
	iSMenu +="\te.g. cp, fe, peb, all, none\n\n"
	iSMenu +="x to exit.\n\n"
	print(iSMenu)

def techSettingsMenu(bytesForward, bytesBack, linesForward, linesBack):
	tMenu =  "\n"
	tMenu += "*  Setting applies only for PE files\n"
	tMenu += "** Setting applies only for shellcode\n\n"
	tMenu += "Global settings:\n"
	tMenu += " *  Max bytes to dissassemble forward: "
	tMenu += str(bytesForward)
	tMenu += "\n"
	tMenu += " ** Max instructions to check forward: "
	tMenu += str(linesForward)
	tMenu += "\n"
	tMenu += " *  Max bytes to dissassemble backward: "
	tMenu += str(bytesBack)
	tMenu += "\n"
	tMenu += " ** Max instructions to check backward: "
	tMenu += str(linesBack)
	tMenu += "\n\n"
	tMenu += "  h - Display options.\n"
	tMenu += "  g - Global settings.\n"
	tMenu += "  c - Call pop.\n"
	tMenu += "  p - Walking the PEB.\n"
	tMenu += "  k - Change minimum length of strings.\n"
	tMenu += "  \t*Used for Syscall\n"
	tMenu += "  x - Exit.\n"
	print(tMenu)

def globalTechMenu(bytesForward, bytesBack, linesForward, linesBack):
	gtMenu = " h - Display options.\n"
	gtMenu += " fb - Max bytes to dissassemble forward: "
	gtMenu += str(bytesForward)
	gtMenu += "\n"
	gtMenu += " bb - Max bytes to dissassemble backward: "
	gtMenu += str(bytesBack)
	gtMenu += "\n\n"

	gtMenu += "Global settings for shellcode:\n"
	gtMenu += " fi - Max instructions to check forward: "
	gtMenu += str(linesForward)
	gtMenu += "\n"
	gtMenu += " bi - Max instructions to check backward: "
	gtMenu += str(linesBack)
	gtMenu += "\n\n"
	gtMenu += " x - Exit.\n"
	print(gtMenu)

def cpTechMenu(maxDistance):
	cpTMenu = "\nMax call distance: "
	cpTMenu += str(maxDistance)
	cpTMenu += "\n"
	cpTMenu += " *How far forward you can go for GetPC.\n\n"
	cpTMenu += "Enter max call distance: "
	print(cpTMenu)

def pebTechMenu(pointsLimit):
	pebTMenu = "Minimum number of likely features: "
	pebTMenu += str(pointsLimit)
	pebTMenu += "\n"	
	pebTMenu += " *These are unique features to identify PEB wakling.\n"
	pebTMenu += "\nEnter number of features: "
	print (pebTMenu)

def setRegValMenu():
	print("")
	print("proto")

def printMenu(bpPushRet, bpCallPop, bpFstenv, bpEgg, bpHeaven, bpPEB, bExportAll, bpStrings, bpEvilImports, bpModules, bpPushStrings, bpAll):
	iMenu = "Selections to print:\n"
	iMenu += "\tpr - Push ret\t\t\t[" 
	iMenu += "x" if bpPushRet else " "
	iMenu += "]\n"
	iMenu += "\tcp - Call pop / GetPC\t\t[" 
	iMenu += "x" if bpCallPop else " "
	iMenu += "]\n"
	iMenu += "\tfe - Fstenv / GetPC\t\t[" 
	iMenu += "x" if bpFstenv else  " "
	iMenu += "]\n"
	iMenu += "\tsy - Windows syscall\t\t[" 
	iMenu += "x" if bpEgg else " "
	iMenu += "]\n"
	iMenu += "\thg - Heaven's gate\t\t[" 
	iMenu += "x" if bpHeaven else " "
	iMenu += "]\n"
	iMenu += "\tpb - Walking the PEB\t\t[" 
	iMenu += "x" if bpPEB else " "
	iMenu += "]\n"
	iMenu += "\tim - Imports\t\t\t[" 
	iMenu += "x" if bpEvilImports else " "
	iMenu += "]\n"
	iMenu += "\tlm - Loaded modules\t\t[" 
	iMenu += "x" if bpModules else " "
	iMenu += "]\n"
	iMenu += "\tst - Strings \t\t\t["
	iMenu += "x" if bpStrings else " "
	iMenu += "]\n"
	iMenu += "\tps - Push Stack Strings \t["
	iMenu += "x" if bpPushStrings else " "
	iMenu += "]\n"
	iMenu += "\tall - All selections\t\t["
	iMenu += "x" if bpAll else " "
	iMenu += "]\n\t\t*Default\n\n"
	iMenu += "j - Export all to JSON. \t["
	iMenu += "x" if bExportAll else " "
	iMenu += "]\n"
	iMenu += "h - Show options.\n"
	iMenu += "c - Clear all print selections.\n"
	iMenu += "s - Windows syscall submenu.\n"
	iMenu += "g - Toggle selections.\n"
	iMenu += "z - Print selections.\n"
	iMenu += "x - Exit.\n"
	print(iMenu)

def osFindSelectionPrint(osVersion):
	if(type(osVersion) == "<class '__main__.OSVersion'>"):
		return osVersion.toggle

	else:
		print("false")

def osFindSelection(osVersion):	
	#Returns [ ] if false else [x] 
	menuString = ""
	g = ""
	if(osVersion.toggle):
		menuString += "[x]"
		g = "[x]"
	else:
		menuString += "[ ]"
		g = "[ ]"
	return g

def syscallPrintSubMenu(syscallSelection, showDisassembly, syscallPrintBit, showOptions):
	vMenu = ""
	if(showOptions):
		vMenu += "Selections:\n"
	nada = ""
	column1 = 0 		#The col1 position in syscallSelection
	column2 = 0
	col1Newline = False
	col2Newline = False
	col1Category = ''
	col2Category = ''
	t = 0
	while not ((column1 == -1) and (column2 == -1)):

	#Prints two columns recursively from our list
	#-1 indicates column is done
		if  not (column1 == -1): 

			#check for newline
			if not (syscallSelection[column1].category == col1Category):
				col1Newline = True
				col1Category = syscallSelection[column1].category


			#check if we've reached the last in a category	
			if(re.search("server", syscallSelection[column1].category, re.IGNORECASE)):
				#Look for next col1 category
				for i in range(len(syscallSelection[column1 + 1:])):
					if not (re.search("server", syscallSelection[i + column1].category, re.IGNORECASE)):
						column1 = i + column1
						col1Category = syscallSelection[column1].category
						break

					#bounds checking
					if i == len(syscallSelection[column1 + 1:])-1:
						column1 = -1

		if  not (column2 == -1):

			if not (syscallSelection[column2].category == col2Category):
				col2Newline = True
				col2Category = syscallSelection[column2].category
			#check if we've reached the last in a category
			if not (re.search("server", syscallSelection[column2].category, re.IGNORECASE)):

				#Look for next col2 category
				for i in range(len(syscallSelection[column2 + 1:])):
					if (re.search("server", syscallSelection[i + column2].category, re.IGNORECASE)):
						column2 = i + column2
						col2Category = syscallSelection[column2].category
						break

			#bounds checking
			#After it finds the end of the list, it sets the position (column2) to -1 to know it is at the end
			if column2 >= (len(syscallSelection)):
						print("Col2 end")
						column2 = -1

		#Add col1 item
		if not (column1 == -1):
			if(col1Newline):
				vMenu += ('{:<32}'.format(nada))
			else:

				#Format non categories
				if not (syscallSelection[column1].name == syscallSelection[column1].category):
					vMenu += ('{:<5s} {:<4s} {:<12s} {:<8}'.format(nada, syscallSelection[column1].code, syscallSelection[column1].name, osFindSelection(syscallSelection[column1]))) 

				#Format Categories
				else:
					vMenu += ('{:<4s} {:<17s}  {:<8}'.format(syscallSelection[column1].code, syscallSelection[column1].name, osFindSelection(syscallSelection[column1]))) 
				column1 += 1
				if column1 >= (len(syscallSelection)):
							column1 = -1
		if not (column2 == -1):
			if not col2Newline: 

				#Format non categories
				if not (syscallSelection[column2].name == syscallSelection[column2].category) and not (syscallSelection[column2].category == "server Column multiselect variables"):
					vMenu += ('{:<6s} {:<5s} {:<27s} {:<5}'.format(nada, syscallSelection[column2].code, syscallSelection[column2].name, osFindSelection(syscallSelection[column2])))

				#Format categories
				else:
					vMenu += ('{:<4s} {:<35s} {:<5}'.format(syscallSelection[column2].code, syscallSelection[column2].name, osFindSelection(syscallSelection[column2])))  
				column2 += 1
				if column2 >= (len(syscallSelection)):
							column2 = -1
		vMenu += "\n"
		col1Newline = False
		col2Newline = False
	vMenu += "\n"

	if showOptions:
		vMenu += "\nFunctional Commands:\n"
		vMenu += "h - Options.\n"
		vMenu += "c - Clear syscall selections.\n"
		vMenu += "g - Enter syscall selections.\n"
		vMenu += "b - Change bits.\t\t["
		vMenu += str(syscallPrintBit)
		vMenu += "]\n"
		vMenu += "d - Display disassembly.\t["
		vMenu += "x" if showDisassembly else " "
		vMenu += "]\n"
		vMenu += "z - Print syscalls.\n"
		# vMenu += "b - Change bits 64]\n"
		vMenu += "x - Exit.\n"

	print(vMenu)

def printModulesMenu(modulesMode):
	iMenu = 'Select one of the following options:\n'
	iMenu += "\t1 - Find only DLLs in IAT"
	if(modulesMode == 1):
		iMenu += "\t\t[x]\n"
	else:
		iMenu += "\t\t[ ]\n"
	iMenu += "\t2 - Find DLLs in IAT and beyond"
	if(modulesMode == 2):
		iMenu += "\t\t[x]\n"
	else:
		iMenu += "\t\t[ ]\n"
	iMenu += "\t3 - Find DLLs in IAT, beyond, and more"
	if(modulesMode == 3):
		iMenu += "\t[x]\n"
	else:
		iMenu += "\t[ ]\n"
	iMenu += "\t\t*Default\n"
	iMenu += "\t\t**This must be selected to find InMemoryOrderModuleList.\n"
	iMenu += "\th - Show options.\n"
	iMenu += "\tp - Print.\n"
	iMenu += "\tz - Execute.\n"
	iMenu += "\tr - Reset InMemoryOrderModuleList.\n"
	iMenu += "\tx - Exit.\n"
	print(iMenu)

def stringMenu(bAsciiStrings, bWideCharStrings, bPushStackStrings, bAllStrings, s):
	iMenu = ''
	iMenu += "Strings to find:\n"
	iMenu += "\tas - ASCII strings\t["
	iMenu += "x" if bAsciiStrings else " "
	iMenu += "]\n"
	iMenu += "\twc - Wide char strings\t["
	iMenu += "x" if bWideCharStrings else " "
	iMenu += "]\n"
	iMenu += "\tps - Push stack strings\t["
	iMenu += "x" if bPushStackStrings else " "
	iMenu += "]\n"
	iMenu += "\tall - All strings\t["
	iMenu += "x" if bAllStrings else " "
	iMenu += "]\n\n"
	# iMenu += "Sections:\n"
	# for sec in s:
	# 	iMenu += "\t" + sec.sectionName.decode() + "\n"
	# iMenu += "\n"
	iMenu += "h - Show options.\n"
	iMenu += "g - Toggle selections.\n"
	iMenu += "c - Clear selections.\n"
	iMenu += "p - Print found strings.\n"
	iMenu += "m - Set register values.\n"
	iMenu += "z - Find strings.\n"
	iMenu += "r - Reset found strings.\n"
	iMenu += "x - Exit.\n"
	print(iMenu)

def shellcodeStringMenu(bAsciiStrings, bWideCharStrings, bPushStackStrings, bAllStrings, s):
	iMenu = ''
	iMenu += "Strings to find:\n"
	iMenu += "\tas - ASCII strings\t["
	iMenu += "x" if bAsciiStrings else " "
	iMenu += "]\n"
	iMenu += "\twc - Wide char strings\t["
	iMenu += "x" if bWideCharStrings else " "
	iMenu += "]\n"
	iMenu += "\tps - Push stack strings\t["
	iMenu += "x" if bPushStackStrings else " "
	iMenu += "]\n"
	iMenu += "\tall - All strings\t["
	iMenu += "x" if bAllStrings else " "
	iMenu += "]\n\n"
	# iMenu += "Sections:\n"
	# for sec in s:
	# 	iMenu += "\t" + sec.sectionName.decode() + "\n"
	# iMenu += "\n"
	iMenu += "h - Show options.\n"
	iMenu += "g - Toggle selections.\n"
	iMenu += "c - Clear selections.\n"
	iMenu += "p - Print found strings.\n"
	iMenu += "m - Change minimum shellcode length.\n"
	iMenu += "z - Find strings.\n"
	iMenu += "r - Reset found strings.\n"
	iMenu += "x - Exit.\n"
	print(iMenu)

def showStringSelections(bAsciiStrings, bWideCharStrings, bPushStackStrings, bAllStrings, s):
	iMenu = "\nSelections changed.\n\n"
	iMenu += "Strings to find:\n"
	iMenu += "\tas - ASCII strings\t["
	iMenu += "x" if bAsciiStrings else " "
	iMenu += "]\n"
	iMenu += "\twc - Wide char strings\t["
	iMenu += "x" if bWideCharStrings else " "
	iMenu += "]\n"
	iMenu += "\tps - Push stack strings\t["
	iMenu += "x" if bPushStackStrings else " "
	iMenu += "]\n"
	iMenu += "\tall - All strings\t["
	iMenu += "x" if bAllStrings else " "
	iMenu += "]\n\n"
	print(iMenu)

def importsMenu():
	iMenu = ''
	iMenu +='h - Show options.\n'
	iMenu +='p - Print imports.\n'
	iMenu +='z - Execute.\n'
	iMenu +='r - Reset found imports.\n'
	iMenu +='x - Exit.\n'
	print(iMenu)