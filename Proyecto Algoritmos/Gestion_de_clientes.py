from Cliente import *
from Validacion import *
from Lectura_Datos import subir_datos



def register_customer(customer_list):

    print("\n---REGISTRAR CLIENTE--- \n")

    print("Que tipo de cliente es?\n")
    customer_type = ["Juridico","Natural"]
    for n in range(len(customer_type)):
        print(f"{n+1}.{customer_type[n]}")

    answer = options_menu(customer_type)

    #Cliente Juridico
    if answer == 1:
        print("\nUsted seleccionó 'Juridico'\n\nRellenemos el resto de datos:")
        
        type = "Juridico"

        name = input("\nNombre de empresa:")
        #validacion de name
        validation = espacio_vacio(name)
        while validation == "Por favor introduzca un valor":
            print(validation)
            name = input("\nNombre de empresa:")
            validation = espacio_vacio(name)
        name = name.capitalize()

        #validacion y input del email
        print("\nEmail:")
        email = correo_electronico(customer_list)

        #validacion y input de la direccion de envio
        print("\nDireccion:")
        address = direccion()

        #validacion y input del numero telefonico
        print("\nTelefono:")
        phone = telefono()

        #validacion y input del numero de rif
        print("\nRif:")
        rif = num_rif(customer_list)

        #registro del nuevo cliente
        new_customer = Juridico(type, name, email, address, phone, rif)
        print(f"""
        Estos seran los datos del nuevo cliente:

        --DATOS DEL NUEVO CLIENTE--
        {new_customer.show_atr_jur()}
        """)
        conf = input("\nEstos son los datos que desea para el cliente? s/n --->")
        confirmation_customer = confirmation(conf)
        while confirmation_customer == "Confirmacion invalida, introduzca un valor valido":
            print(confirmation_customer)
            conf = input("Estos son los datos que desea para el cliente? s/n --->")
            confirmation_customer = confirmation(conf)

        #Registrar cliente
        if confirmation_customer == "s":
            customer_list.append(new_customer.showjurid())
            #funcion en Lectura_Datos.py
            subir_datos('clientes.txt',customer_list)
            #verificar si se desea registrar otro cliente
            print("\nEl cliente a sido registrado con exito :D!\nLos Datos han sido guardados\n")
            return "creado"

        #reiniciar la creacion de los datos del nuevo producto y el programa de 'AGREGAR NUEVOS PRODUCTOS'
        if confirmation_customer == "n":
            return register_customer(customer_list)

    #Cliente Natural
    if answer == 2:
        print("\nUsted seleccionó 'Natural'\n\nRellenemos el resto de datos:")
        
        type = "Natural"

        name = input("\nNombre (solo nombre no apellido):")
        #validacion de name
        validation = espacio_vacio(name)
        while validation == "Por favor introduzca un valor":
            print(validation)
            name = input("\nNombre (solo nombre no apellido):")
            validation = espacio_vacio(name)
        name = name.capitalize()

        last_name = input("\nApellido:")
        #validacion de last_name
        validation = espacio_vacio(last_name)
        while validation == "Por favor introduzca un valor":
            print(validation)
            last_name = input("\nApellido:")
            validation = espacio_vacio(last_name)
        last_name = last_name.capitalize()

        #validacion y input del email
        print("\nEmail:")
        email = correo_electronico(customer_list)

        #validacion y input de la direccion de envio
        print("\nDireccion:")
        address = direccion()

        #validacion y input del numero telefonico
        print("\nTelefono:")
        phone = telefono()

        #validacion y input del numero de rif
        print("\nCedula de identidad:")
        id = cedula(customer_list)

        #registro del nuevo cliente
        new_customer = Natural(type, name, last_name, email, address, phone, id)
        print(f"""
        Estos seran los datos del nuevo cliente:

        --DATOS DEL NUEVO CLIENTE--
        {new_customer.show_atr_natur()}
        """)
        conf = input("\nEstos son los datos que desea para el cliente? s/n --->")
        confirmation_customer = confirmation(conf)
        while confirmation_customer == "Confirmacion invalida, introduzca un valor valido":
            print(confirmation_customer)
            conf = input("Estos son los datos que desea para el cliente? s/n --->")
            confirmation_customer = confirmation(conf)

        #Registrar cliente
        if confirmation_customer == "s":
            customer_list.append(new_customer.shownatur())
            #funcion en Lectura_Datos.py
            subir_datos('clientes.txt',customer_list)
            #verificar si se desea registrar otro cliente
            print("\nEl cliente a sido registrado con exito :D!\nLos Datos han sido guardados\n")
            return "creado"

         #reiniciar la creacion de los datos del nuevo producto y el programa de 'AGREGAR NUEVOS PRODUCTOS'
        if confirmation_customer == "n":
            return register_customer(customer_list)


#Para realizar todas las funciones del modulo de Gestion de productos
def gestion_clientes(customer_list):

    print("\n ---GESTION DE CLIENTE---")
    #Opciones de menu
    menu = ["Registrar Cliente","Buscar cliente","Modificar informacion de cliente","Eliminar cliente","Volver al menu principal"]
    for n in range(len(menu)):
        print(f"{n+1}.{menu[n]}")

    #Validacion de la opcion de menu
    choice = options_menu(menu)

    #Registrar cliente
    if choice == 1:
        repeat = True
        while repeat == True:
            create =  register_customer(customer_list)
            if create == "creado":
                conf = input("Desea registrar otro cliente? s/n --->")
                create_customer = confirmation(conf)
                while create_customer == "Confirmacion invalida, introduzca un valor valido":
                    print(create_customer)
                    conf = input("Desea registrar otro cliente? s/n --->")
                    create_customer = confirmation(conf)
                if create_customer == "s":
                #reinicia el programa de 'REGISTRAR CLIENTE'
                    repeat = True
                if create_customer == "n":
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
                    repeat = False

    #Buscar cliente
    if choice == 2:
        print("\n---BUSCAR CLIENTE--- \n")
        inventario = []
        for info in customer_list:
            inventario.append(info.split('/'))
        # print(inventario)
        confir = False

        while confir == False:
            print("--Filtros de busqueda--\n")
            category = ["Cedula o Rif", "Correo Electronico"]
            for n in range(len(category)):
                print(f"{n+1}.{category[n]}")

            print("\nPor cual filtro desea realizar su busqueda?")
            choice = options_menu(category)
            
            #Por "Cedula o Rif"
            if choice == 1:
                filter_cedula = []
                filter_rif = []
                #Creacion de la lista de filtros de Category
                for index in range(len(inventario)):
                    c = inventario[index][-1]
                    categ = c.split(":")
                    #Para cedula
                    if "C" in categ[1]:
                        if categ[1] not in filter_cedula:
                            filter_cedula.append(f"{index}.{categ[1]}")
                    if "J" in categ[1]:
                        if categ[1] not in filter_rif:
                            filter_rif.append(f"{index}.{categ[1]}")
                
                # print(filter_rif)
                # print(filter_cedula)
                print("\n--Eleccion--\n")
                filter_b = ["Cedula", "Rif"]
                for n in range(len(filter_b)):
                    print(f"{n+1}.{filter_b[n]}")

                print("\nEn cual filtro desea utilizar?")
                selection = options_menu(filter_b)

                #Busqueda por Cedula
                if selection == 1:
                    print("\n--Lista Cedulas--\n")
                    #Mostrar los filtros de cedula
                    for n in range(len(filter_cedula)):
                        v = filter_cedula[n]
                        div = v.split(".")
                        value = div[1]
                        print(f"{n+1}.{value}")

                    #Eleccion del filtro de cedula
                    print("\nEn cual filtro desea mostrar al cliente?")
                    select = options_menu(filter_cedula)
                    
                    num = select - 1
                    v = filter_cedula[num]
                    valor = v.split(".")
                    r_valor = valor[1]
                    print(r_valor)

                    #mostrar valores
                    print("")
                    for index in range(len(inventario)):
                        c = inventario[index][-1]
                        categ = c.split(":")
                        if categ[1] == r_valor:
                            filt = customer_list[index]
                            print(f"-{filt}\n")
                    
            
                    #Verificar si se desea hacer otra busqueda
                    conf = input("\nDesea realizar otra busqueda s/n --->")
                    confirmation_customer = confirmation(conf)
                    while confirmation_customer == "Confirmacion invalida, introduzca un valor valido":
                        print(confirmation_customer)
                        conf = input("\nDesea realizar otra busqueda s/n --->")
                        confirmation_customer = confirmation(conf)

                    if confirmation_customer == "s":
                    #reinicio a la muestra de los filtros
                        confir = False
                    if confirmation_customer == "n":
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
                
                #Busqueda por Rif
                if selection == 2:
                    print("\n--Lista Rif--\n")
                    #Mostrar los filtros de rif
                    for n in range(len(filter_rif)):
                        v = filter_rif[n]
                        div = v.split(".")
                        value = div[1]
                        print(f"{n+1}.{value}")

                    #Eleccion del filtro de rif
                    print("\nEn cual filtro desea mostrar al cliente?")
                    select = options_menu(filter_rif)
                    
                    num = select - 1
                    v = filter_rif[num]
                    valor = v.split(".")
                    r_valor = valor[1]
                    print(r_valor)

                    #mostrar valores
                    print("")
                    for index in range(len(inventario)):
                        c = inventario[index][-1]
                        categ = c.split(":")
                        if categ[1] == r_valor:
                            filt = customer_list[index]
                            print(f"-{filt}\n")
            
                    #Verificar si se desea hacer otra busqueda
                    conf = input("\nDesea realizar otra busqueda s/n --->")
                    confirmation_customer = confirmation(conf)
                    while confirmation_customer == "Confirmacion invalida, introduzca un valor valido":
                        print(confirmation_customer)
                        conf = input("\nDesea realizar otra busqueda s/n --->")
                        confirmation_customer = confirmation(conf)

                    if confirmation_customer == "s":
                    #reinicio a la muestra de los filtros
                        confir = False
                    if confirmation_customer == "n":
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

            #Por "Correo Electronico"
            if choice == 2:
                print("\n--correos electronicos--\n")
                filter = []
                
                #Creacion de la lista de filtros de Correo electronico
                for index in range(len(inventario)):
                    c = inventario[index][0]
                    categ = c.split(":")
                    #Para cedula
                    if categ[1] == "Natural":
                        value = inventario[index][3]
                        email = value.split(":")
                        if email[1] not in filter:
                            filter.append(f"{email[1]}")
                    if categ[1] == "Juridico":
                        value = inventario[index][2]
                        email = value.split(":")
                        if email[1] not in filter:
                            filter.append(f"{email[1]}")
                        
                #print(filter)

                #Mostrar los filtros
                for n in range(len(filter)):
                    print(f"{n+1}.{filter[n]}")

                #Eleccion del filtro de cliente
                print("\nEn cual filtro desea mostrar a los clientes?")
                choice = options_menu(filter)

                    
                num = choice - 1
                val = filter[num]
                #print(val)
                #mostrar valores
                print("")
                for index in range(len(inventario)):
                    c = inventario[index][0]
                    categ = c.split(":")
                    #print(categ)
                    if categ[1] == "Natural":
                        value = inventario[index][3]
                        #print(value)
                        email = value.split(":")
                        #print(email[1])
                        if email[1] == val:
                            filt = customer_list[index]
                            print(f"-{filt}\n")
                    if categ[1] == "Juridico":
                        value = inventario[index][2]
                        #print(value)
                        email = value.split(":")
                        #print(email[1])
                        if email[1] == val:
                            filt = customer_list[index]
                            print(f"-{filt}\n")

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

    #Modificar cliente     
    if choice == 3:
        print("\n---MODIFICAR CLIENTE--- \n")

        confir = False
        while confir == False:
            print("\nLista de clientes:\n")
            #Opciones de clientes a modificar
            for n in range(len(customer_list)):
                print(f"{n+1}.{customer_list[n]}")

            print("\nCual cliente desea modificar?")
            #Validacion de la opcion clientes a modificar
            choice = options_menu(customer_list)

            #Seleccion del objeto a modificar
            eliminate = choice - 1
            print(f"\n{customer_list[eliminate]}")
            customer = customer_list[eliminate]

            conf = input("\nEstos son los datos que desea modificar? s/n ---> ")
            confirmation_customer = confirmation(conf)
            while confirmation_customer == "Confirmacion invalida, introduzca un valor valido":
                print(confirmation_customer)
                conf = input("Estos son los datos que desea modificar? s/n ---> ")
                confirmation_customer = confirmation(conf)

            #Modificacion del cliente
            if confirmation_customer == "s":

                #Datos del objeto a modificar
                inventario = customer.split('/')

                #Creacion de la lista de filtros de Correo electronico

                c = inventario[0]
                categ = c.split(":")

                #Para modificar datos de un cliente natural
                if categ[1] == "Natural":

                    type = "Natural"

                    print("\n--Name--")
                    num = inventario[1]
                    answer = modificar(num)
                    name = answer
                    if name == "no":
                        name = input("\nNuevo nombre del cliente (solo el nombre sin el apellido):")
                    #validacion de name
                    validation = espacio_vacio(name)
                    while validation == "Por favor introduzca un valor":
                        print(validation)
                        name = input("Nuevo nombre del cliente (solo el nombre sin el apellido):")
                        validation = espacio_vacio(name)
                    name = name.capitalize()
                    #print(name)

                    print("\n--Last_name--")
                    num = inventario[2]
                    answer = modificar(num)
                    last_name = answer
                    if last_name == "no":
                        last_name = input("\nNuevo apellido del cliente:")
                    #validacion de last_name
                    validation = espacio_vacio(last_name)
                    while validation == "Por favor introduzca un valor":
                        print(validation)
                        last_name = input("\nNuevo apellido del cliente:")
                        validation = espacio_vacio(last_name)
                    last_name = last_name.capitalize()
                    #print(last_name)

                    print("\n--Email--")
                    num = inventario[3]
                    answer = modificar(num)
                    email = answer
                    if email == "no":
                        print("\nNuevo correo electronico del cliente:\n")
                         #validacion de email
                        email = correo_electronico(customer_list)
                    #print(email)


                    print("\n--Address--")
                    num = inventario[4]
                    answer = modificar(num)
                    address = answer
                    if address == "no":
                        print("\nNueva direccion de envio del cliente:")
                        #validacion de address
                        address = direccion()

                    print("\n--Phone--")
                    num = inventario[5]
                    answer = modificar(num)
                    phone = answer
                    if phone == "no":
                        print("\nNuevo numero de telefono del cliente:")
                        #validacion de phone
                        phone = telefono()

                    print("\n--ID--")
                    num = inventario[6]
                    answer = modificar(num)
                    id = answer
                    if id == "no":
                        print("\nNuevo numero de cedula de identidad  del cliente:")
                        #validacion de id
                        id = cedula(customer_list)          




                    #creacion del nuevo cliente
                    new_custumer = Natural(type,name,last_name,email,address,phone,id)
                    old_custumer = Natural(type,inventario[1],inventario[2],inventario[3],inventario[4],inventario[5],inventario[6])

                    print("Estos seran los datos del nuevo cliente:")
                    print(f"--VIEJOS DATOS DEL NUEVO CLIENTE--\n{old_custumer.show_atr_natur()}\n")
                    print(f"--NUEVOS DATOS DEL NUEVO CLIENTE--\n{new_custumer.show_atr_natur()}")

                    conf = input("\nEstos son los datos que desea del cliente? s/n --->")
                    confirmat = confirmation(conf)
                    while confirmat == "Confirmacion invalida, introduzca un valor valido":
                        print(confirmat)
                        conf = input("Estos son los datos que desea del cliente? s/n --->")
                        confirmat = confirmation(conf)

                    #Modificar cliente en la lista para el txt
                    if confirmat == "s":
                        customer_list[eliminate] = new_custumer.shownatur()
                    #funcion en Lectura_Datos.py
                    subir_datos('clientes.txt',customer_list)
                    #verificar si se desea crear mas clientes 
                    print("\nEl cliente a sido modificado con exito :D!\n")
                    conf = input("Desea modificar otro cliente? s/n --->")
                    create_customer = confirmation(conf)
                    while create_customer == "Confirmacion invalida, introduzca un valor valido":
                        print(create_customer)
                        conf = input("Desea modificar otro cliente? s/n --->")
                        create_customer = confirmation(conf)
                    if create_customer == "s":
                        #reinicia el programa de 'MODIFICAR CLIENTE'
                        confir = False
                    if create_customer == "n":
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

                    #reiniciar la creacion de los datos del nuevo cliente y el programa de 'AGREGAR NUEVOS PRODUCTOS'
                    if confirmat == "n":
                        confir = False
            
                if categ[1] == "Juridico":

                    type = "Juridico"

                    print("\n--Name--")
                    num = inventario[1]
                    answer = modificar(num)
                    name = answer
                    if name == "no":
                        name = input("\nNuevo nombre del cliente:")
                    #validacion de name
                    validation = espacio_vacio(name)
                    while validation == "Por favor introduzca un valor":
                        print(validation)
                        name = input("Nuevo nombre del cliente:")
                        validation = espacio_vacio(name)
                    #print(name)

                    print("\n--Email--")
                    num = inventario[2]
                    answer = modificar(num)
                    email = answer
                    if email == "no":
                        print("\nNuevo correo electronico del cliente:\n")
                         #validacion de email
                        email = correo_electronico(customer_list)
                    #print(email)


                    print("\n--Address--")
                    num = inventario[3]
                    answer = modificar(num)
                    address = answer
                    if address == "no":
                        print("\nNueva direccion de envio del cliente:")
                        #validacion de address
                        address = direccion()

                    print("\n--Phone--")
                    num = inventario[4]
                    answer = modificar(num)
                    phone = answer
                    if phone == "no":
                        print("\nNuevo numero de telefono del cliente:")
                        #validacion de phone
                        phone = telefono()

                    print("\n--RIF--")
                    num = inventario[5]
                    answer = modificar(num)
                    rif = answer
                    if rif == "no":
                        print("\nNuevo numero de cedula de identidad  del cliente:")
                        #validacion de rif
                        rif = num_rif(customer_list)          




                    #creacion del nuevo cliente
                    new_custumer = Juridico(type, name, email, address, phone, rif)
                    old_custumer = Juridico(type,inventario[1],inventario[2],inventario[3],inventario[4],inventario[5])

                    print("Estos seran los datos del nuevo cliente:")
                    print(f"--VIEJOS DATOS DEL NUEVO CLIENTE--\n{old_custumer.show_atr_jur()}\n")
                    print(f"--NUEVOS DATOS DEL NUEVO CLIENTE--\n{new_custumer.show_atr_jur()}")

                    conf = input("\nEstos son los datos que desea del cliente? s/n --->")
                    confirmat = confirmation(conf)
                    while confirmat == "Confirmacion invalida, introduzca un valor valido":
                        print(confirmat)
                        conf = input("Estos son los datos que desea del cliente? s/n --->")
                        confirmat = confirmation(conf)

                    #Modificar cliente en la lista para el txt
                    if confirmat == "s":
                        customer_list[eliminate] = new_custumer.showjurid()
                    #funcion en Lectura_Datos.py
                    subir_datos('clientes.txt',customer_list)
                    #verificar si se desea crear mas clientes 
                    print("\nEl cliente a sido modificado con exito :D!\n")
                    conf = input("Desea modificar otro cliente? s/n --->")
                    create_customer = confirmation(conf)
                    while create_customer == "Confirmacion invalida, introduzca un valor valido":
                        print(create_customer)
                        conf = input("Desea modificar otro cliente? s/n --->")
                        create_customer = confirmation(conf)
                    if create_customer == "s":
                        #reinicia el programa de 'MODIFICAR CLIENTE'
                        confir = False
                    if create_customer == "n":
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

                    #reiniciar la creacion de los datos del nuevo cliente y el programa de 'AGREGAR NUEVOS PRODUCTOS'
                    if confirmat == "n":
                        confir = False

    #Eliminar cliente       
    if choice == 4:

        print("\n---ELIMINAR CLIENTE--- \n")

        confir = False
        while confir == False:
          print("\nLista de clientes:\n")
          #Opciones de clientes a modificar
          for n in range(len(customer_list)):
                print(f"{n+1}.{customer_list[n]}")

          print("\nCual cliente desea eliminar?")
          #Validacion de la opcion clientes a modificar
          choice = options_menu(customer_list)

          #Seleccion del cliente a eliminar
          eliminate = choice - 1
          print(f"\n{customer_list[eliminate]}")
          product = customer_list[eliminate]

          conf = input("\nEstos son los datos que desea eliminar? s/n ---> ")
          confirmation_custumer = confirmation(conf)
          while confirmation_custumer == "Confirmacion invalida, introduzca un valor valido":
                print(confirmation_custumer)
                conf = input("Estos son los datos que desea eliminar? s/n ---> ")
                confirmation_custumer = confirmation(conf)

          #Eliminar cliente en la lista para el txt
          if confirmation_custumer == "s":
                  customer_list.pop(eliminate)
                  #funcion en Lectura_Datos.py
                  subir_datos('clientes.txt',customer_list)
                  print("\nEl cliente a sido eliminado con exito :D!\n")
                  #verificar si se desea crear mas productos 
                  conf = input("Desea eliminar otro cliente? s/n --->")
                  eliminate_customer = confirmation(conf)
                  while eliminate_customer == "Confirmacion invalida, introduzca un valor valido":
                        print(eliminate_customer)
                        conf = input("Desea eliminar otro cliente? s/n --->")
                        eliminate_customer = confirmation(conf)

                  if eliminate_customer == "s":
                        #reinicia el programa de 'ELIMINAR PRODUCTO'
                        confir = False
                  if eliminate_customer == "n":
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
