import csv
import json
import sys


jsonfeeder = {}

with open('tables.csv') as csv_file:
	csv = csv.reader(csv_file, delimiter=',')
	step = 0
	steprow = 0
	stepdict = {}
	stepweight = []
	stepresult = []
	refmode = 0
	for row in csv:
		if 'REFERENCE' in row[1]:
			jsonfeeder[step]["weight"] = stepdict
			step = row[1]
			refmode = 1
		elif 'STEP' in row[1]:
			if step != 0:
				jsonfeeder[step] = stepdict
			step = row[1]
			# print("new step:", step)
			jsonfeeder[step] = {}
			refmode = 0
			steprow = 0
			stepdict = {}
			stepweight = []
			stepresult = []
		elif refmode == 1:
			stepdict[row[0]] = {"min":row[1],"max":row[2],"Real World Analogue":row[3]}
		else:
			# print(steprow,":",row[0],"=",row[2])
			stepweight.append(row[0])
			stepresult.append(row[2])
			stepdict = {"weight" : stepweight*1, "result" : stepresult}
			steprow += 1
	jsonfeeder[step] = stepdict

out = json.dumps(jsonfeeder)
print(out)