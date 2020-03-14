from easygui import fileopenbox 
import pandas as pd
import os

Semicolon=';'
filesCsv = dict()

def SelectCSVPaths():
    return fileopenbox(title='Seleccionar archivos CSV',default='*.csv', filetypes=['*.csv'],multiple=True)

def GroupByTypes(paths):
    global filesCsv
    isOk =True
    for path in paths:
        try:
            AddToCsvDicctionary(path)
        except Exception as error:
            print("Error: "+path)
            print("\t"+str(error))

def CsvDelimiter(line):
	csvSep=None
	if line.find(",") !=-1:
		return ","
	elif line.find(";") !=-1:
		return ";"
	return csvSep

def AddToCsvDicctionary(path):
    csv= open(path,'r')
    header= csv.readline()
    global filesCsv
    csvSep=CsvDelimiter(header)
    if csvSep !=None:
        new_csv=[path,csvSep]
        if header not in filesCsv:
            csv_paths[header]=[]
            filesCsv[header].append(new_csv)
    csv.close()

def NameOfFile(path):
    return os.path.split(path)[len(os.path.split(path))-1]

def LogError(error):
    print("#### ERROR #####")
    print("\t"+str(error))

def SaveCsv(csvList):
	listcsvs=csvList[:]
	csvInit=listcsvs[0]
	listcsvs.remove(csvInit)
	good=True
	try:
		[path0,sep0]=csvInit
		df1 = pd.read_csv(path0, sep=sep0,encoding='cp1252',dtype=str)
		name=NameOfFile(path0)
		print("Guardando: "+name)
		for path,sep in listcsvs:
			name=NameOfFile(path)
			print("          +"+name)
			df2 = pd.read_csv(path, sep=sep,encoding='cp1252',dtype=str)
			df1=df1.append(df2)
	except Exception as error:
		LogError(error)
		good=False

	if good:
		try:
			df1= df1.sort_values(by=['IMP_ID'])
			df1.to_csv(path0,encoding='cp1252',index=False,sep=Semicolon)
		except Exception as error:
			df1.to_csv(path0,encoding='cp1252',index=False,sep=Semicolon)
	
		for path,sep in listcsvs:
			os.remove(path)

def main():
    csv_paths = SelectCSVPaths()
    GroupByTypes(csv_paths)
    for csv,list_csv in csv_paths.items():
		SaveCsv(list_csv)
    input("Presiona tecla para finalizar")

main()

