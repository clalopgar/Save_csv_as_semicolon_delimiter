from easygui import fileopenbox 

sep=','

def SelectCSVPaths():
    return fileopenbox(title='Seleccionar archivos CSV',default='*.csv', filetypes=['*.csv'],multiple=True)


def GroupByTypes(paths):
    filesCsv = dict()
    isOk =True

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
	csvSep=CsvDelimiter(header)
	if csvSep !=None:
		new_csv=[path,csvSep]
		if header not in csv_paths:
			csv_paths[header]=[]
		csv_paths[header].append(new_csv)
	csv.close()


csv_paths = SelectCSVPaths()
print(csv_paths)
#Inicializa el diccionario

