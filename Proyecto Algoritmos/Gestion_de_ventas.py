from Lectura_Datos import subir_datos
from Gestion_de_clientes import register_customer
from Producto import Producto
from Factura import *
from Validacion import *
from time import localtime,asctime
import datetime

def gestion_de_venta(customer_list, product_list, sale_list, pay_list, shipping_list, purchase_of_products):

    print("\n ---GESTION DE VENTA---")
    #Opciones de menu
    menu = ["Registrar venta","Buscar venta","Volver al menu principal"]
    for n in range(len(menu)):
        print(f"{n+1}.{menu[n]}")

    #Validacion de la opcion de menu
    choice = options_menu(menu)
    while choice == "Error! por favor intente de nuevo":
        print(choice)
        choice = options_menu(menu)

    #registrar venta
    if choice == 1:
        def compra():
            sale = False
            while sale == False:
                verif_customer = verif_rif_ced(customer_list)
                if verif_customer == "registrar":
                    create =  register_customer(customer_list)
                    if create == "creado":
                        sale = False
                if verif_customer != "registrar":
                    sale = True
        
            c = verif_customer[0]
            categ = c.split(":")

            inventario = []
            for info in product_list:
                inventario.append(info.split('/'))

            if categ[1] == "Natural":
                #Creacion del name_cliente
                c = verif_customer[1]
                name = c.split(":")
                name = name[1]
                c = verif_customer[2]
                last_name = c.split(":")
                last_name = last_name[1]
                name_cliente = f"{name} {last_name}"
                #para la compra mas adelante
                type = "Natural"
                d = verif_customer[-1]
                id = d.split(":")
                #id del cliente
                id = id[1]

            if categ[1] == "Juridico":
                #Creacion del name_cliente
                c = verif_customer[1]
                name = c.split(":")
                name_cliente = name[1]
                #para la compra mas adelante
                type = "Juridico"
                d = verif_customer[-1]
                id = d.split(":")
                #id del cliente
                id = id[1]

            num_ventas = len(sale_list)
            num_ventas = int(num_ventas)
            pay_number = num_ventas + 1

            # print(type)
            # print(name_cliente)
            # print(id)
            # print(pay_number)

            carrito = []
            change_products = []
            total = 0

            compra =  True
            while compra == True:
                print("======LISTA DE PRODUCTOS======\n")
                for index in range(len(inventario)):
                    print(f"{index + 1}.{inventario[index][0]}\n {inventario[index][1]}\n {inventario[index][2]}\n {inventario[index][3]}\n {inventario[index][4]}\n")


                print("\nCual producto desea agregar al carrito?\nRevise la lista con cuidado y seleccione el producto que desee")
                #Validacion de la opcion productos a modificar
                choice = options_menu(product_list)
                selection = choice - 1
                product = inventario[selection][4]
                quantity = product.split(":")
                quantity = int(quantity[1])
                    
                while quantity == 0:
                    print("Verifique las existencias de producto")
                    choice = options_menu(product_list)
                    selection = choice - 1
                    product = inventario[selection][4]
                    quantity = product.split(":")
                    quantity = int(quantity[1])

                selection = choice - 1
                product = inventario[selection][4]
                quantity = product.split(":")
                quantity = int(quantity[1])
                    

                #Seleccion del objeto a modificar
                selection = choice - 1

                name_product = inventario[selection][0]
                name_product = name_product.split(":")
                name_product = name_product[1]
                print(f"\nproducto:{name_product}")
                #sacando valor del producto
                price_product = inventario[selection][2]
                price_product = price_product.split(":")
                price_product = price_product[1]
                price_product = int(price_product)

                repeat = True
                while repeat == True:
                    print(f"precio del producto:{price_product}\n")
                    cant = input("cantidad del producto: ")
                    validation = numeric(cant)
                    while validation == "Error! por favor intente de nuevo":
                        print(validation)
                        cant = input("cantidad del producto:")
                        validation = numeric(cant)
                    cant = int(cant)

                    print(f"\nCantidad:{cant}")
                    conf = input("\nEsta es la cantidad que desea? s/n ---> ")
                    answer = confirmation(conf)
                    while answer == "Confirmacion invalida, introduzca un valor valido":
                        print(answer)
                        conf = input("\nEsta es la cantidad que desea? s/n ---> ")
                        answer = confirmation(conf)

                    if answer == "s":
                        if cant <= quantity:
                            print("no hay productos suficientes!, intente de nuevo")
                            repeat = False
                        if cant > quantity:
                            print("no hay productos suficientes!, intente de nuevo")
                            repeat = True
                    if answer == "n":
                        repeat = True


                #calculando subtotal del producto
                subtotal_prod = price_product*cant
                total += subtotal_prod

                new_quantity = quantity - cant

                data_producto = inventario[selection]
                data_change = []
                for index in range(len(data_producto)):
                    value = data_producto[index]
                    data = value.split(":")
                    c = data[1]
                    data_change.append(c)

                new_product = Producto(data_change[0],data_change[1],data_change[2],data_change[3],new_quantity)
                
                carrito.append(f"{name_product} x{cant} ----- ${subtotal_prod}")
                change_products.append(f"{selection}.{new_product.showprod()}")
                print("\n         SU CARRITO DE COMPRA\n------------------------------------")
                for producto in range(len(carrito)):
                    print(carrito[producto])
                print("------------------------------------")
                print(f"SUBTOTAL ACTUAL: {total}")
                #print(change_products)

                #preguntar si desea agregar otro producto
                
                conf = input("\nDesea registrar otro producto? s/n --->")
                append_carrito = confirmation(conf)
                while append_carrito == "Confirmacion invalida, introduzca un valor valido":
                    print(append_carrito)
                    conf = input("\nDesea registrar otro producto? s/n --->")
                    append_carrito = confirmation(conf)
                if append_carrito == "s":
                #reinicia el programa de 'REGISTRAR CLIENTE'
                    compra = True
                if append_carrito == "n":
                    compra = False
            
            #print(carrito)
            #creacion de la lista de productos de compra como str
            buy_products = ""
            for index in range(len(carrito)):
                prod = carrito[index]
                buy_products += f"{prod}, "
            #Subtotal sera el valor en dolares del total, el total se usara para las converciones de moneda
            subtotal = total
            
            print("\n---FORMALICEMOS LA COMPRA---\n")
            print("--Metodos de pago--\n")
            print("Por favor elija el metodo de pago que desea utilizar")
            print("\n--Metodos--\n")
            pays = ["PdV","PM","Zelle","Cast"]

            for n in range(len(pays)):
                print(f"{n+1}.{pays[n]}")

            choice = options_menu(pays)

            if choice == 1:
                pay_type = "PdV"
            if choice == 2:
                pay_type = "PM"
            if choice == 3:
                pay_type = "Zelle"
            if choice == 4:
                pay_type = "Cast"

            print("\n--Moneda de pago--\n")
            print("Por favor elija la moneda de pago que desea utilizar")
            print("\n--Monedas--\n")
            coins = ["Bs.","$","Euro"]

            for n in range(len(coins)):
                print(f"{n+1}.{coins[n]}")

            choice = options_menu(coins)

            if choice == 1:
                payment_coin = "Bs."
            if choice == 2:
                payment_coin = "$"
            if choice == 3:
                payment_coin = "Euro"

            print("\n--Metodo de envio--\n")
            print("Por favor elija el metodo de envio que desea utilizar")
            print("\n--Tipos de envio--\n")
            shipping = ["MRW","Zoom","Delivery"]

            for n in range(len(shipping)):
                print(f"{n+1}.{shipping[n]}")

            choice = options_menu(shipping)

            if choice == 1:
                shipping_method = "MRW"
            if choice == 2:
                shipping_method = "Zoom"
            if choice == 3:
                shipping_method = "Delivery"

            #Calculo descuento:
            if type == "Natural":
                discount = "None"
            if type == "Juridico":
                discount = (1.5 * total) / 100
                total -= discount

            #Calculo del iva:
            iva = (16 * total) / 100
            total += iva

            #Calculo de igtf
            if payment_coin == "Bs.":
                igtf = "None"
            if payment_coin == "$" or payment_coin == "Euro":
                igtf = (3 * total) / 100
                total += igtf

            #Calculo del total
            if payment_coin == "Bs.":
                total *= 27.8
            if payment_coin == "Euro":
                total *= 1.09
            #Dia de pago
            ahora = datetime.datetime.utcnow()
            ahora = str(ahora)
            ahora = ahora.split(" ")
            sale_date = ahora[0]

            #fecha maxima para realizar el pago
            if type == "Juridico":
                ahora = datetime.datetime.utcnow()
                tomorrow = ahora + datetime.timedelta(days=25)
                tomorrow = str(tomorrow)
                tomorrow = tomorrow.split(" ")
                pay_date = tomorrow[0]
            if type == "Natural":
                pay_date = sale_date

            #fecha maxima para recibir eel envio
            ahora = datetime.datetime.utcnow()
            tomorrow = ahora + datetime.timedelta(days=32)
            tomorrow = str(tomorrow)
            tomorrow = tomorrow.split(" ")
            shipping_date = tomorrow[0]

            new_factura = Factura(pay_number, name_cliente, id, buy_products, pay_type, payment_coin, shipping_method, subtotal, discount, iva, igtf, total, sale_date, pay_date, shipping_date)

            print(new_factura.show_factura())

            conf = input("\nDesea registrar la compra? s/n --->")
            validacion = confirmation(conf)
            while validacion == "Confirmacion invalida, introduzca un valor valido":
                print(validacion)
                conf = input("\nDesea registrar la comprar? s/n --->")
                validacion = confirmation(conf)

            if validacion == "s":
                sale_list.append(new_factura.show_venta())
                pay_list.append(new_factura.show_pago())
                shipping_list.append(new_factura.show_envio())
                #funcion en Lectura_Datos.py
                subir_datos('ventas.txt',sale_list)
                subir_datos('pagos.txt',pay_list)
                subir_datos('envios.txt',shipping_list)
                #para cambiar el stock
                for index in range(len(change_products)):
                    values = []
                    product = change_products[index]
                    product = product.split(".")
                    #product_list[change_num], para elegir el producto a modificar
                    change_num = product[0]
                    change_num = int(change_num)

                    c = product[1]
                    invent = c.split('/')
                    for v in range(len(invent)):
                        d = invent[v]
                        info= d.split(":")
                        dat = info[1]
                        values.append(dat)

                    change_product = Producto(values[0],values[1],values[2],values[3],values[4])
                    product_list[change_num] = change_product.showprod()

                subir_datos('inventario.txt',product_list)

                #verificar si se desea registrar otro cliente
                return "no"

            if validacion == "n":
                return "no"

        

        repeat = True
        while repeat == True:
            create =  compra()
            if create == "no":
                conf = input("Desea crear otro pago s/n --->")
                create_compra = confirmation(conf)
                while create_compra == "Confirmacion invalida, introduzca un valor valido":
                    print(create_compra)
                    conf = input("Desea crear otro pago s/n --->")
                    create_compra = confirmation(conf)
                if create_compra == "s":
                #reinicia el programa de 'REGISTRAR VENTA'
                    repeat = True
                if create_compra == "n":
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



    #buscar venta
    if choice == 2:
        print("\n---BUSCAR VENTA--- \n")
        inventario = []
        for info in sale_list:
          inventario.append(info.split('/'))
        

        confir = False

        while confir == False:
            print("--Filtros de busqueda--\n")
            category = ["Name", "Sale date", "Amount in total"]
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
 
            #por "Sale date"
            if choice == 2:
                filter = []
                #Creacion de la lista de filtros de Name
                for index in range(len(inventario)):
                    c = inventario[index][-2]
                    categ = c.split(":")
                    cate = categ[1]
                    name = cate
                    if name not in filter:
                      filter.append(name)
                print(filter)
                #Mostrar los filtros
                print("\n--Lista de dates--\n")

                for n in range(len(filter)):
                  print(f"{n+1}.Fecha:{filter[n]}")
                #Eleccion del filtro de Name
                print("\nPor cual fecha le gustaria buscar?")
                choice = options_menu(filter)

                num = choice - 1
                val = filter[num]
                #mostrar valores
                print("")
                for index in range(len(inventario)):
                  c = inventario[index][-2]
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

            #por "Amount in total"
            if choice == 3:
                filter = []
                #Creacion de la lista de filtros de Name
                for index in range(len(inventario)):
                    c = inventario[index][-3]
                    categ = c.split(":")
                    cate = categ[1]
                    name = cate
                    if name not in filter:
                      filter.append(name)
                print(filter)
                #Mostrar los filtros
                print("\n--Lista de amount--\n")

                for n in range(len(filter)):
                  print(f"{n+1}.Fecha:{filter[n]}")
                #Eleccion del filtro de Name
                print("\nPor cual monto total le gustaria buscar?")
                choice = options_menu(filter)

                num = choice - 1
                val = filter[num]
                #mostrar valores
                print("")
                for index in range(len(inventario)):
                  c = inventario[index][-3]
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
  

    if choice == 3:
        return "menu"