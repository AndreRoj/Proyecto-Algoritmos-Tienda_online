from Validacion import *


def gestion_de_envios(shipping_list):
    print("\n ---GESTION DE ENVIOS---")
    #Opciones de menu
    menu = ["Buscar envio","Volver al menu principal"]
    for n in range(len(menu)):
        print(f"{n+1}.{menu[n]}")

    #Validacion de la opcion de menu
    choice = options_menu(menu)
    while choice == "Error! por favor intente de nuevo":
        print(choice)
        choice = options_menu(menu)

    #registrar buscar
    if choice == 1:
        print("\n---BUSCAR ENVIO--- \n")
        inventario = []
        
        for info in shipping_list:
          inventario.append(info.split('/'))
        # print(inventario)


        confir = False

        while confir == False:
            print("--Filtros de busqueda--\n")
            category = ["Name", "Shipping date"]
            for n in range(len(category)):
                print(f"{n+1}.{category[n]}")

            print("\nPor cual filtro desea realizar su busqueda?")
            choice = options_menu(category)

            #por "Name"
            if choice == 1:
                filter = []
                #Creacion de la lista de filtros de Name
                for index in range(len(inventario)):
                    c = inventario[index][1]
                    categ = c.split(":")
                    cate = categ[1]
                    name = cate
                    if name not in filter:
                      filter.append(name)
                print(filter)
                #Mostrar los filtros
                print("\n--Lista de Name--\n")
                
                for n in range(len(filter)):
                  print(f"{n+1}.{filter[n]}")
                #Eleccion del filtro de Name
                print("\nPor cual nombre le gustaria buscar?")
                choice = options_menu(filter)

                num = choice - 1
                val = filter[num]
                #mostrar valores
                print("")
                for index in range(len(inventario)):
                  c = inventario[index][1]
                  categ = c.split(":")
                  if val in categ[1]:
                    filt = shipping_list[index]
                    print(f"-{filt}\n")
      
                #Verificar si se desea hacer otra busqueda
                conf = input("\nDesea realizar otra busqueda s/n --->")
                confirmation_product = confirmation(conf)
                while confirmation_product == "Confirmacion invalida, introduzca un valor valido":
                  print(confirmation_product)
                  conf = input("\nDesea realizar otra busqueda s/n --->")
                  confirmation_product = confirmation(conf)

                if confirmation_product == "s":
                #reinicio a la muestra de los filtros
                  confir = False
                if confirmation_product == "n":
                  print("\nDesea volver al menu principal o finalizar el programa?")
                  menu = ["Volver al menu principal","Finalizar programa"]
                  for n in range(len(menu)):
                      print(f"{n+1}.{menu[n]}")

                  chose = options_menu(menu)

                  if chose == 1:
                      return "menu"
                  if chose == 2:
                    print("""
                  --- Fin del programa :D ---
                  inicie el programa de nuevo
                  """)
                    break
                  
            #por "Shippig date"
            if choice == 2:
                filter = []
                #Creacion de la lista de filtros de pay_date
                for index in range(len(inventario)):
                    c = inventario[index][-1]
                    categ = c.split(":")
                    cate = categ[1]
                    date = cate
                    if date not in filter:
                      filter.append(date)
                #Mostrar los filtros
                print("\n--Lista de dates--\n")
                
                for n in range(len(filter)):
                  print(f"{n+1}.Date:{filter[n]}")
                #Eleccion del filtro de Name
                print("\nPor cual fecha le gustaria buscar?")
                choice = options_menu(filter)

                num = choice - 1
                val = filter[num]
                #mostrar valores
                print("")
                for index in range(len(inventario)):
                  c = inventario[index][-1]
                  categ = c.split(":")
                  if val in categ[1]:
                    filt = shipping_list[index]
                    print(f"-{filt}\n")
      
                #Verificar si se desea hacer otra busqueda
                conf = input("\nDesea realizar otra busqueda s/n --->")
                confirmation_product = confirmation(conf)
                while confirmation_product == "Confirmacion invalida, introduzca un valor valido":
                  print(confirmation_product)
                  conf = input("\nDesea realizar otra busqueda s/n --->")
                  confirmation_product = confirmation(conf)

                if confirmation_product == "s":
                #reinicio a la muestra de los filtros
                  confir = False
                if confirmation_product == "n":
                  print("\nDesea volver al menu principal o finalizar el programa?")
                  menu = ["Volver al menu principal","Finalizar programa"]
                  for n in range(len(menu)):
                      print(f"{n+1}.{menu[n]}")

                  chose = options_menu(menu)

                  if chose == 1:
                      return "menu"
                  if chose == 2:
                    print("""
                  --- Fin del programa :D ---
                  inicie el programa de nuevo
                  """)
                    break    

    if choice == 2:
        return "menu"