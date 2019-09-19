import csv

csv_file = "data/GDELT_2.0_Events_Column_Labels_Header_Row_Sep2016.csv"
with open(csv_file, 'rb') as f:
    with open("mappings.txt", 'w') as w:
        csvreader = csv.reader(f, delimiter=',')
        count = 0
        for row in csvreader:
            if row[1] == 'STRING':
                item_type = 'str'
            if row[1] == "INTEGER":
                item_type = "int"
            if row[1] == "FLOAT":
                item_type = "float"
            w.write("try: self.{name} = {item_typ}(self.__source_text[{item}]) \n".format(name=row[0], item=str(count), item_typ=item_type))
            w.write("except: pass \n")
            count +=1
        w.close()