import formParser

from tableMaker import listToExcel

output = formParser.parser("data/inputExample.txt")
listToExcel(output, "data/newInput.xlsx")
