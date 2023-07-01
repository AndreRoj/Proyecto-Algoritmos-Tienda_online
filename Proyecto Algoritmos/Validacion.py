#validaciones

def options_menu(m):
  option = input("\n Elija una opcion(el numero del la opcion que desea)---> ")
  if option.isnumeric() == True:
    if int(option) <= len(m) and int(option) > 0:
      return int(option)
    else:
      print("Error! por favor intente de nuevo")
      return options_menu(m)
  if option.isnumeric() == False:
    print("Error! por favor intente de nuevo")
    return options_menu(m)

  
def confirmation(n):
  option = n
  if option == "n" or option == "s":
    return option
  else:
    return f"Confirmacion invalida, introduzca un valor valido"
  
def espacio_vacio(n):
  option = n
  if option.isspace() == True or option == "":
    return f"Por favor introduzca un valor"
  if option.isspace() == False:
    return option
  
def alphabetic(n):
  option = n
  if option.isalpha() == True:
    return option
  if option.isalpha() == False:
    return f"Error! por favor intente de nuevo"
  
def numeric(n):
  option = n
  if option.isnumeric() == True:
    return option
  if option.isnumeric() == False:
    return f"Error! por favor intente de nuevo"
  
def cedula(list):
  filter_cedula = []
  inventario = []

  for info in list:
    inventario.append(info.split('/'))
  for index in range(len(inventario)):
    c = inventario[index][-1]
    categ = c.split(":")
    #Para cedula
    if "C" in categ[1]:
      if categ[1] not in filter_cedula:
        filter_cedula.append(categ[1])

  repeat = True
  while repeat == True:
    option = input("\n\nIntroduzca su cedula de identidad sin puntos\nEjemplo de cedula: C45677894\n\nCedula---> C")
    c = len(option)
    cedula = f"C{option}"
    if len(option) == 8 and option.isnumeric() == True:
      if cedula not in filter_cedula:
        print(f"\nCedula: C{option}")
        conf = input("\nEstos son los datos de su cedula? s/n ---> ")
        answer = confirmation(conf)
        while answer == "Confirmacion invalida, introduzca un valor valido":
          print(answer)
          conf = input("\nEstos son los datos de su cedula? s/n ---> ")
          answer = confirmation(conf)
        if answer == "s":
          return f"C{option}"
        if answer == "n":
          repeat = True
      if cedula in filter_cedula:
        print("Cedula invalida, por favor introduzca un valor nuevamente")
        repeat = True
    else:
      print("Error!, por favor introduzca un valor valido, solo numeros!")
      repeat = True
  
def num_rif(list):
  filter_rif = []
  inventario = []

  for info in list:
    inventario.append(info.split('/'))
  for index in range(len(inventario)):
    c = inventario[index][-1]
    categ = c.split(":")
    #Para rif
    if "J" in categ[1]:
      if categ[1] not in filter_rif:
        filter_rif.append(categ[1])

  repeat = True
  while repeat == True:
    option = input("\n\nIntroduzca rif\nEjemplo de rif: J345664312\n\nRif ---> J")
    c = len(option)
    rif = f"J{option}"
    if len(option) == 9 and option.isnumeric() == True:
      if rif not in filter_rif:
        print(f"\nRif:J{option}")
        conf = input("\nEstos son los datos de su rif? s/n ---> ")
        answer = confirmation(conf)
        while answer == "Confirmacion invalida, introduzca un valor valido":
          print(answer)
          conf = input("\nEstos son los datos de su rif? s/n ---> ")
          answer = confirmation(conf)
        if answer == "s":
          return f"J{option}"
        if answer == "n":
          repeat = True
      if rif in filter_rif:
        print("Rif invalido, por favor introduzca un valor nuevamente")
        repeat = True
    else:
      print("Error!, por favor introduzca un valor valido!\n")
      repeat = True

def correo_electronico(list):
  filter_email = []
  inventario = []
  for info in list:
    inventario.append(info.split('/'))
  for index in range(len(inventario)):
    c = inventario[index][0]
    categ = c.split(":")
    #Para cedula
    if categ[1] == "Natural":
        value = inventario[index][3]
        email = value.split(":")
        if email[1] not in filter_email:
            filter_email.append(f"{email[1]}")
    if categ[1] == "Juridico":
        value = inventario[index][2]
        email = value.split(":")
        if email[1] not in filter_email:
            filter_email.append(f"{email[1]}")

  repeat = True
  while repeat == True:
    option = input("\n\nIntroduzca email ---> ")
    if "@" in option:
      if ".com" in option:
        if option not in filter_email:
          print(f"\nEmail:{option}")
          conf = input("\nEstos son los datos de su email? s/n ---> ")
          answer = confirmation(conf)
          while answer == "Confirmacion invalida, introduzca un valor valido":
            print(answer)
            conf = input("\nEstos son los datos de su email? s/n ---> ")
            answer = confirmation(conf)
          if answer == "s":
            return f"{option}"
          if answer == "n":
            repeat = True
        if option in filter_email:
          print("correo electronico valido, por favor introduzca un valor nuevamente")
          repeat = True

        
      if ".ve" in option:
        if option not in filter_email:
          print(f"\nEmail:{option}")
          conf = input("\nEstos son los datos de su email? s/n ---> ")
          answer = confirmation(conf)
          while answer == "Confirmacion invalida, introduzca un valor valido":
            print(answer)
            conf = input("\nEstos son los datos de su email? s/n ---> ")
            answer = confirmation(conf)
          if answer == "s":
            return f"{option}"
          if answer == "n":
            repeat = True
        if option in filter_email:
          print("correo electronico valido, por favor introduzca un valor nuevamente")
          repeat = True
      else:
        print("Error!, por favor introduzca un email valido")
        repeat = True
    else:
      print("Error!, por favor introduzca un email valido")
      repeat = True
    
def telefono():
  option = input("Introduzca numero de telefono\nEjemplo: 0414-3464253\n\nTelefono ---> ")
  if "-" in option:
    div = option.split("-")
    if div[0].isnumeric() and div[1].isnumeric():
      if len(div[0]) == 4 and len(div[1]) == 7:
        print(f"Telefono:{option}")
        conf = input("\nEstos son los datos de su numero de telefono? s/n ---> ")
        answer = confirmation(conf)
        while answer == "Confirmacion invalida, introduzca un valor valido":
          print(answer)
          conf = input("\nEstos son los datos de su numero de telefono? s/n ---> ")
          answer = confirmation(conf)
        if answer == "s":
          return f"{option}"
        if answer == "n":
          return telefono()
      else:
        print("Error!, por favor introduzca un numero valido")
      return telefono()
    else:
      print("Error!, por favor introduzca un numero valido")
      return telefono()
  else:
    print("Error!, por favor introduzca un numero valido")
    return telefono()

def direccion():
  option = input("Introduzca direccion de envio\n\nDireccion ---> ")
  validation = espacio_vacio(option)
  while validation == "Por favor introduzca un valor":
    print(validation)
    option = input("\nDireccion ---> ")
    validation = espacio_vacio(option)
  
  print(f"\nDireccion de envio:{option}")
  conf = input("\nEstos son los datos de direccion de envio? s/n ---> ")
  answer = confirmation(conf)
  while answer == "Confirmacion invalida, introduzca un valor valido":
    print(answer)

    conf = input("\nEstos son los datos de direccion de envio? s/n ---> ")
    answer = confirmation(conf)
  if answer == "s":
    return f"{option}"
  if answer == "n":
    return direccion()
  
#Funcion para ver si se reusan ciertos datos del producto
def modificar(num):
#Para tomar los datos del "inventarion[valor]" 
  d = num
  info= d.split(":")
  data = info[1]

  print(f"\nDatos seleccionados:\n{num}\n")
  conf = input("Desea conservar estos datos? s/n ---> ")
  confirmation_customer = confirmation(conf)
  while confirmation_customer == "Confirmacion invalida, introduzca un valor valido":
      print(confirmation_customer)
      conf = input("Desea conservar estos datos? s/n ---> ")
      confirmation_customer = confirmation(conf)

  if confirmation_customer == "s":
      return data
  if confirmation_customer == "n":
      return "no"

def verif_rif_ced(list):
  filter = []
  inventario = []

  for info in list:
    inventario.append(info.split('/'))
  for index in range(len(inventario)):
    c = inventario[index][-1]
    categ = c.split(":")
    #Para cedula
    if "C" in categ[1]:
      if categ[1] not in filter:
        filter.append(f"{categ[1]}")
    if "J" in categ[1]:
      if categ[1] not in filter:
        filter.append(f"{categ[1]}")
  #print(filter)

  repeat = True
  try_search = 3
  while repeat == True and try_search != 0:

    option = input("\n\nIntroduzca su cedula de identidad si es un Cliente Natural (Ejemplo de cedula: C45677894) o su numero de rif si es un Cliente Juridico (Ejemplo de rif: J345664312)\n\n---> ")
    print(f"Rif/C.I:{option}")
    conf = input("\nEstos son sus datos?  s/n ---> ")
    answer = confirmation(conf)
    while answer == "Confirmacion invalida, introduzca un valor valido":
      print(answer)
      conf = input("\nEstos son sus datos?  s/n ---> ")
      answer = confirmation(conf)

    if answer == "s":
      if "C" in option:
        num = option.split("C")
        div = num[1]
        if len(option) == 9 and div.isnumeric() == True:
          if option in filter:
            for index in range(len(inventario)):
              c = inventario[index][-1]
              categ = c.split(":")
              if categ[1] == option:
                customer = inventario[index]
            print("\nYa lo hemos encontrado en el sistema por favor disfrute de su compra")
            #print(customer)
            return customer

          if option not in filter:
            print("\nNo lo hemos encontrado en el sistema por favor introduzca un valor nuevamente\n")
            repeat = True
        else:
          print("\nCedula invalida, por favor introduzca un valor nuevamente\n")
          repeat = True

      if "J" in option:
        num = option.split("J")
        div = num[1]
        if len(option) == 10 and div.isnumeric() == True:
          if option in filter:
            for index in range(len(inventario)):
              c = inventario[index][-1]
              categ = c.split(":")
              if categ[1] == option:
                customer = inventario[index]
            print("Ya lo hemos encontrado en el sistema por favor disfrute de su compra")
            #print(customer)
            return customer
          if option not in filter:
            print("No lo hemos encontrado en el sistema por favor introduzca un valor nuevamente")
            repeat = True
        else:
          print("Rif invalido, por favor introduzca un valor nuevamente")
          repeat = True

      else:
          print("ERROR! por favor introduzca un valor valido")
          try_search -= 1
          print(f"\n======LE QUEDA {try_search} INTENTOS====")
          repeat = True

    if answer == "n":
      repeat = True
  print("Vamos a llevarlo a al modulo de registro para registrarlo")
  return "registrar"



# verif_rif_ced(cara)