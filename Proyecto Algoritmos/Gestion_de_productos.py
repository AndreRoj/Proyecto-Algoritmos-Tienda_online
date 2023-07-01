from Producto import Producto
from Validacion import *
from Lectura_Datos import subir_datos


#Para realizar todas las funciones del modulo de Gestion de productos
def gestion_productos(product_list):

  print("\n ---GESTION DE PRODUCTOS---")
  #Opciones de menu
  menu = ["Agregar nuevo producto","Buscar productos","Modificar productos","Eliminar producto","Volver al menu principal"]
  for n in range(len(menu)):
    print(f"{n+1}.{menu[n]}")

  #Validacion de la opcion de menu
  choice = options_menu(menu)

  #Agregar producto
  if choice == 1:
    print("\n---AGREGAR PRODUCTO--- \n")

    confir = False
    while confir == False:
      name = input("Nombre del producto:")
      #validacion de name
      validation = espacio_vacio(name)
      while validation == "Por favor introduzca un valor":
        print(validation)
        name = input("Nombre del producto:")
        validation = espacio_vacio(name)

      description = input("Descripcion del producto:")
      #validacion de description
      validation = espacio_vacio(description)
      while validation == "Por favor introduzca un valor":
        print(validation)
        description = input("Descripcion del producto:")
        validation = espacio_vacio(description)

      price = input("Precio del producto:")
      #validacion de price
      validation = numeric(price)
      while validation == "Error! por favor intente de nuevo":
        print(validation)
        price = input("Precio del producto:")
        validation = numeric(price)
      
      category = input("categoria del producto:")
      category = category.capitalize()
      #validacion de category
      validation = espacio_vacio(category)
      while validation == "Por favor introduzca un valor":
        print(validation)
        category = input("categoria del producto:")
        validation = espacio_vacio(category)

      quantity = input("exitencias del producto:")
      #validacion de quantity
      validation = numeric(quantity)
      while validation == "Error! por favor intente de nuevo":
        print(validation)
        quantity = input("exitencias del producto:") 
        validation = numeric(quantity)
        
      #creacion del nuevo producto
      new_product = Producto(name,description,price,category,quantity)
      
      print(f"""
      Estos seran los datos del nuevo producto:

      --DATOS DEL NUEVO PRODUCTO--
      {new_product.show_atr()}
      """)
      

      conf = input("\nEstos son los datos que desea para producto? s/n --->")
      confirmation_product = confirmation(conf)
      while confirmation_product == "Confirmacion invalida, introduzca un valor valido":
        print(confirmation_product)
        conf = input("Estos son los datos que desea para producto? s/n --->")
        confirmation_product = confirmation(conf)

      
      #Agregar producto
      if confirmation_product == "s":
        product_list.append(new_product.showprod())
        #funcion en Lectura_Datos.py
        subir_datos('inventario.txt',product_list)
        #verificar si se desea crear mas productos 
        print("\nAgregado con exito al inventario :D\n")
        conf = input("Desea agregar otro producto? s/n --->")
        create_product = confirmation(conf)
        while create_product == "Confirmacion invalida, introduzca un valor valido":
          print(create_product)
          conf = input("Desea agregar otro producto? s/n --->")
          create_product = confirmation(conf)
        if create_product == "s":
          #reinicia el programa de 'AGREGAR NUEVOS PRODUCTOS'
          confir = False
        if create_product == "n":
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

      #reiniciar la creacion de los datos del nuevo producto y el programa de 'AGREGAR NUEVOS PRODUCTOS'
      if confirmation_product == "n":
        confir = False

  #Buscar producto      
  if choice == 2:
    print("\n---BUSCAR PRODUCTO--- \n")
    inventario = []
    for info in product_list:
      inventario.append(info.split('/'))
    

    confir = False

    while confir == False:
      print("--Filtros de busqueda--\n")
      category = ["Category", "Price", "Name", "Quantity"]
      for n in range(len(category)):
        print(f"{n+1}.{category[n]}")

      print("\nPor cual filtro desea realizar su busqueda?")
      choice = options_menu(category)
      
      #Por "Category"
      if choice == 1:
        filter = []
        #Creacion de la lista de filtros de Category
        for index in range(len(inventario)):
          c = inventario[index][3]
          categ = c.split(":")
          if categ[1] not in filter:
            filter.append(categ[1])
        #Mostrar los filtros
        print("\n--Lista de Category--\n")
        for n in range(len(filter)):
          print(f"{n+1}.{filter[n]}")

        #Eleccion del filtro de category
        print("\nEn cual filtro desea mostrar los productos?")
        choice = options_menu(filter)
        
        num = choice - 1
        val = filter[num]
        #mostrar valores
        print("")
        for index in range(len(inventario)):
          c = inventario[index][3]
          categ = c.split(":")
          if categ[1] == val:
            filt = product_list[index]
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

      #Por "Price"
      if choice == 2:
        filter = []
        #Creacion de la lista de filtros de Price
        for index in range(len(inventario)):
          c = inventario[index][2]
          categ = c.split(":")
          if categ[1] not in filter:
            filter.append(categ[1])
        #Mostrar los filtros
        print("\n--Lista de Price--\n")
        for n in range(len(filter)):
          print(f"{n+1}.Price:{filter[n]}")
        #Eleccion del filtro de category
        print("\nPor cual precio desea mostrar los productos?")
        choice = options_menu(filter)

        
        num = choice - 1
        val = filter[num]
        #mostrar valores
        print("")
        for index in range(len(inventario)):
          c = inventario[index][2]
          categ = c.split(":")
          if categ[1] == val:
            filt = product_list[index]
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

      #Por "Name"
      if choice == 3:
        filter = []
        #Creacion de la lista de filtros de Name
        for index in range(len(inventario)):
          c = inventario[index][0]
          categ = c.split(":")
          cate = categ[1]
          name = cate.split(" ")
          for v in name:
            if v not in filter:
              filter.append(v)
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
          c = inventario[index][0]
          categ = c.split(":")
          if val in categ[1]:
            filt = product_list[index]
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

      #Por "Quantity"
      if choice == 4:
        filter = []
        #Creacion de la lista de filtros de Quantity
        for index in range(len(inventario)):
          c = inventario[index][-1]
          categ = c.split(":")
          if categ[1] not in filter:
            filter.append(categ[1])
        #Mostrar los filtros
        print("\n--Lista de Quantity--\n")
        for n in range(len(filter)):
          print(f"{n+1}.Quantity:{filter[n]}")
        #Eleccion del filtro de quantity
        print("\nPor cual valor de existencias desea mostrar los productos?")
        choice = options_menu(filter)
        
        num = choice - 1
        val = filter[num]
        #mostrar valores
        print("")
        for index in range(len(inventario)):
          c = inventario[index][-1]
          categ = c.split(":")
          if categ[1] == val:
            filt = product_list[index]
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

  #Modificar producto     
  if choice == 3:
    print("\n---MODIFICAR PRODUCTO--- \n")

    confir = False
    while confir == False:
      print("\nLista de productos:\n")
      #Opciones de productos a modificar
      for n in range(len(product_list)):
        print(f"{n+1}.{product_list[n]}")

      print("\nCual producto desea modificar?")
      #Validacion de la opcion productos a modificar
      choice = options_menu(product_list)

      #Seleccion del objeto a modificar
      eliminate = choice - 1
      print(f"\n{product_list[eliminate]}")
      product = product_list[eliminate]

      conf = input("\nEstos son los datos que desea modificar? s/n ---> ")
      confirmation_product = confirmation(conf)
      while confirmation_product == "Confirmacion invalida, introduzca un valor valido":
        print(confirmation_product)
        conf = input("Estos son los datos que desea modificar? s/n ---> ")
        confirmation_product = confirmation(conf)

      #Modificacion del producto
      if confirmation_product == "s":
        #Datos del objeto a modificar
        inventario = product.split('/')
        #print(inventario)

        print("\n--Name--")
        num = inventario[0]
        answer = modificar(num)
        name = answer
        if name == "no":
          name = input("\nNuevo nombre del producto:")
          #validacion de name
          validation = espacio_vacio(name)
          while validation == "Por favor introduzca un valor":
            print(validation)
            name = input("Nuevo nombre del producto:")
            validation = espacio_vacio(name)
        

        print("\n--Description--")
        num = inventario[1]
        answer = modificar(num)
        description = answer
        if description == "no":
          description = input("\nNueva descripcion del producto:")
          #validacion de description
          validation = espacio_vacio(description)
          while validation == "Por favor introduzca un valor":
            print(validation)
            description = input("Nueva descripcion del producto:")
            validation = espacio_vacio(description)
        

        print("\n--Price--")
        num = inventario[2]
        answer = modificar(num)
        price = answer
        if price == "no":
          price = input("\nNuevo precio del producto:")
          #validacion de price
          validation = numeric(price)
          while validation == "Error! por favor intente de nuevo":
            print(validation)
            price = input("Nuevo precio del producto:")
            validation = numeric(price)
        
        print("\n--Category--")
        num = inventario[3]
        answer = modificar(num)
        category = answer
        if category == "no":
          category = input("\nNueva categoria del producto:")
          category = category.capitalize()
          #validacion de category
          validation = espacio_vacio(category)
          while validation == "Por favor introduzca un valor":
            print(validation)
            category = input("Nueva categoria del producto:")
            validation = espacio_vacio(category)

        print("\n--Quantity--")
        num = inventario[4]
        answer = modificar(num)
        quantity = answer
        if quantity == "no":
          quantity = input("\nNueva cantidad de exitencias del producto:")
          #validacion de quantity
          validation = numeric(quantity)
          while validation == "Error! por favor intente de nuevo":
            print(validation)
            quantity = input("exitencias del producto:") 
            validation = numeric(quantity)
          
        #creacion del nuevo producto
        new_product = Producto(name,description,price,category,quantity)
        old_product = Producto(inventario[0],inventario[1],inventario[2],inventario[3],inventario[4])
        
        print("Estos seran los datos del nuevo producto:")
        print(f"--VIEJOS DATOS DEL NUEVO PRODUCTO--\n{old_product.show_atr()}\n")
        print(f"--NUEVOS DATOS DEL NUEVO PRODUCTO--\n{new_product.show_atr()}")
          
        conf = input("\nEstos son los datos que desea del producto? s/n --->")
        confirmat = confirmation(conf)
        while confirmat == "Confirmacion invalida, introduzca un valor valido":
          print(confirmat)
          conf = input("Estos son los datos que desea del producto? s/n --->")
          confirmat = confirmation(conf)

        #Modificar producto en la lista para el txt
        if confirmat == "s":
          product_list[eliminate] = new_product.showprod()
          #funcion en Lectura_Datos.py
          subir_datos('inventario.txt',product_list)
          #verificar si se desea crear mas productos 
          print("\nEl objeto a sido modificado con exito :D!\n")
          conf = input("Desea modificar otro producto? s/n --->")
          create_product = confirmation(conf)
          while create_product == "Confirmacion invalida, introduzca un valor valido":
            print(create_product)
            conf = input("Desea modificar otro producto? s/n --->")
            create_product = confirmation(conf)
          if create_product == "s":
            #reinicia el programa de 'MODIFICAR PRODUCTOS'
            confir = False
          if create_product == "n":
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

        #reiniciar la creacion de los datos del nuevo producto y el programa de 'AGREGAR NUEVOS PRODUCTOS'
        if confirmat == "n":
          confir = False

      #reiniciar la seleccion del producto a modificar
      if confirmation_product == "n":
        confir = False

  #Eliminar producto
  if choice == 4:
    print("\n---ELIMINAR PRODUCTO--- \n")

    confir = False
    while confir == False:
      print("\nLista de productos:\n")
      #Opciones de productos a modificar
      for n in range(len(product_list)):
        print(f"{n+1}.{product_list[n]}")

      print("\nCual producto desea eliminar?")
      #Validacion de la opcion productos a modificar
      choice = options_menu(product_list)

      #Seleccion del objeto a eliminar
      eliminate = choice - 1
      print(f"\n{product_list[eliminate]}")
      product = product_list[eliminate]

      conf = input("\nEstos son los datos que desea eliminar? s/n ---> ")
      confirmation_product = confirmation(conf)
      while confirmation_product == "Confirmacion invalida, introduzca un valor valido":
        print(confirmation_product)
        conf = input("Estos son los datos que desea eliminar? s/n ---> ")
        confirmation_product = confirmation(conf)

      #Eliminar producto en la lista para el txt
      if confirmation_product == "s":
          product_list.pop(eliminate)
          #funcion en Lectura_Datos.py
          subir_datos('inventario.txt',product_list)
          print("\nEl objeto a sido eliminado con exito :D!\n")
          #verificar si se desea crear mas productos 
          conf = input("Desea eliminar otro producto? s/n --->")
          create_product = confirmation(conf)
          while create_product == "Confirmacion invalida, introduzca un valor valido":
            print(create_product)
            conf = input("Desea eliminar otro producto? s/n --->")
            create_product = confirmation(conf)

          if create_product == "s":
            #reinicia el programa de 'ELIMINAR PRODUCTO'
            confir = False
          if create_product == "n":
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

      #reiniciar la eleccion del producto a eliminar
      if confirmation_product == "n":
          confir = False

  if choice == 5:
    return "menu"