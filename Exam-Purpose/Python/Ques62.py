'''62. Read a text file which contents monthly electricity bills of different customer.
print he electricity consumption for july and November month'''

# solution
with open("electricity_bills.txt") as f:
  data = f.readlines()
consumption = {"July":0,"November":0}
for line in data:
  fields = line.split(",")  # split the line into fields
  if fields[1] =="July":
    consumption["July"] += int(fields[2])
  elif fields[1]=="November":
    consumption["November"] += int(fields[2])
print("July consumption: ", consumption["July"])
print("November consumption: ", consumption["November"])