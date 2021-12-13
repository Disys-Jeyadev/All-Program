
'''db = {"customer": {"1000": {"ID": "1000", "name": "John Smith ", "DOB": "01/01/2000", "Gender": "F", "Age": "20","Zip code": "08122-2324", "Amount ": "1500.20"},"2000": {"ID": "2000", "name": "Jim McDonald ", "DOB": "02/02/2020", "Gender": "M", "Age": "25","Zip code": "08136-2324","Amount ": "1500.20"},"20": {"ID": "20", "name": "Jim McDonald", "DOB": "02/02/1999", "Gender": "M", "Age": "25","Zip code": "08124-6565","Amount ": "1500.20"}}}
for i in db.values():
     #print(i)
     for j in i.values():
          for k,l in j.items():
               if k == "Age" and int(l)>25:
                    print(j,l)
               else:
                    print("No Customer Found in the Database")
               break
'''
import json
with open('data.txt') as f:
     lines = f.readlines()

json.dumps(lines)




