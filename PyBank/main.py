import os
import csv
import statistics

budget_csv = os.path.join("budget_data.csv")
file_output = os.path.join("budget_output.txt")

fecha_list = []
dates_list = []
meses_list = []
amount_list = []
suma = 0
diferencia_list = []
anterior = 0
dato_print = ''

with open(budget_csv,newline='') as csvFile:
    csvreader = csv.reader(csvFile,delimiter=',')
    next(csvreader,None)

    for row in csvreader:
        fecha_list.append(row[0].split('-'))
        dates_list.append(row[0])
        amount_list.append(int(row[1]))
    
for meses in fecha_list:
    meses_list.append(meses[0])

for cuenta in amount_list:
    suma = suma + int(cuenta)
    diferencia_list.append(cuenta - anterior)
    anterior = cuenta

del(diferencia_list[0])
del(dates_list[0])

increase = zip(dates_list,diferencia_list)
maximo = max(diferencia_list)
minimo = min(diferencia_list)

print('Financial Analysis')
print('---------------------')
print(f"Total Months: {len(meses_list)}")
print(f"Total: {str(suma)}")
print(f"Average Change: {statistics.mean(diferencia_list)}")

for dato in increase:
    if(dato[1]==maximo):
        print(f"Greatest Increase in Profits: ${dato}")
        dato_print=("Greatest Increase in Profits: $" + str(dato))
    if(dato[1]==minimo):
        print(f"Greatest Decrease in Profits: ${dato}")
        dato_print+=("\nGreatest Decrease in Profits: $" +str(dato))

csvFile.close()

with open(file_output,'w') as datafile:
    datafile.write('Financial Analysis')
    datafile.write('\n---------------------')
    datafile.write("\n"+ f"Total Months: {str(len(meses_list))}")
    datafile.write("\n"+ f"Total: {str(suma)}")
    datafile.write('\n'+ f"Average Change: {str(statistics.mean(diferencia_list))}")
    datafile.write('\n'+ dato_print)