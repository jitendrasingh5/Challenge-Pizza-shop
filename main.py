dict = {}

try:
  r = open("pizza.txt", "r")
  dict = eval(r.read())
  r.close()
except:
  print("ERROR! First save file")
  
            
def add():
  name = input("Name : ")
  toppings = input("Toppings : ")
  size = input("Size (s/m/l) : ")
  if size.lower() == "s":
    size_value = 20.5
  elif size.lower() == "m":
    size_value = 40
  elif size.lower() == "l":
    size_value = 77.87
  while True:
    try:
      quantity = int(input("Quantity : "))
      break
    except:
      print()
      print("Please! Enter a number")
      print()
  total = size_value*quantity
  
  dict[name] = {"Toppings" : toppings, "Size" : size, "Quantity" : quantity, "Total" : total}


def prettyPrint():
  print("Name\t Toppings\t Size  Quantity  Total")
  
  for key, value in dict.items():
    print(f"""{key}: {value["Toppings"]:<10} {value["Size"]:<10} {value["Quantity"]:<2} {value["Total"]:<2}""")
    
      
      
while True:
  print("Romino's pizza")
  print()
  
  menu = input("1.Add Pizza\n2.View Pizzas\n\n : ")

  if menu == "1":
    print()
    add()
  elif menu == "2":
    prettyPrint()


  f = open("pizza.txt", "w")
  f.write(str(dict))
  f.close()
  import time,os
  time.sleep(5)
  os.system("clear")
  
    

  
  