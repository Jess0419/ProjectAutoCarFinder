#Vehicle Finder
allowedVehicleList = ["Ford F-150", "Chevorlet Silverado", "Telsa Cybertruck", "Toyota Tundra", "Nissan Titan"]

#Menu
print("===============================")
print("AutoCountry Vehicle Finder v0.1")
print("===============================")
print("Please enter the following number below from the following menu: ")
print("1. PRINT all Authorized Vehicles")
print("2. SEARCH for Authorized Vehicle")
print("3. Exit")

##############
menu = int(input(""))


#Menu Selection
if menu == 1:
  print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
  print(allowedVehicleList)

if menu == 2:
  car = input("Please Enter the full Vehicle Name: ")
  if car in allowedVehicleList:
    print(str(car)+ " is an authorized vehicle")
  else:
    print(str(car)+ " is not an authorized vehicle")
  
if menu == 3:
  print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
  

