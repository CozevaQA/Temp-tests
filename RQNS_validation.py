from openpyxl import Workbook, load_workbook
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir("Assets") if isfile(join("Assets", f))]
print(onlyfiles)
manifestFileName=""

for x in onlyfiles:
    if "MANIFEST" in x:
        manifestFileName = x
        break

print(manifestFileName)

wb = load_workbook("Assets\\"+manifestFileName)

ws = wb.active

Listicle = list(ws.values)

onlyfiles = [f for f in listdir("Assets\\Extracted PDF Files") if isfile(join("Assets\Extracted PDF Files", f))]
print(onlyfiles)

total_count_arr = []
for i in range(0,len(Listicle)):
    total_count_arr.append(0)
iterator1 = 0
for x in Listicle:
    if x[1] == "Filename":
        continue
    for j in onlyfiles:
        if x[1]+"_" in j or x[1]+".txt" in j or "_"+x[1]+".txt" in j:
            total_count_arr[iterator1] += 1
    iterator1 += 1

iterator1 =0



for x in Listicle:
    if x[1] == "Filename":
        continue
    if int(x[2]) == total_count_arr[iterator1]:
        print(str(x[1])+" : "+str(int(x[2]))+" : "+str(total_count_arr[iterator1])+" : PASSED")
    else:
        print(str(x[1]) + " : " + str(int(x[2])) + " : " + str(total_count_arr[iterator1]) + " : FAILED")
    iterator1+=1



