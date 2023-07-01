
from Gestion_de_productos import gestion_productos
from Gestion_de_clientes import gestion_clientes
from Gestion_de_ventas import gestion_de_venta
from Gestion_de_pagos import gestion_de_pagos
from Gestion_de_envios import gestion_de_envios
from Producto import Producto
from Validacion import options_menu , confirmation
from inicio import load_product
from Lectura_Datos import reinicio_datos, cargando_txt


print("\nINICIANDO PROGRAMA...")
def store():
    #Lector del archivo url
    def convert_to_object(url):
        db = []
        information = load_product(url)
        for producto in information:
            new_product = Producto(producto["name"],producto["description"],producto["price"],producto["category"],producto["quantity"] )
            db.append(new_product)
        return db

    db = convert_to_object("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/products.json")

    

    #LISTAS PARA EL PROGRAMA
    
    products_list = []
    customer_list = []
    sale_list = []
    pay_list = []
    shipping_list = []
    purchase_of_products = []

    #--Para cargar los datos originales e iniciar desde cero--  

    def reinicio():
        #borra los datos en el archivo txt
        with open('inventario.txt','w') as file:
            file.write("")
        #Apendea los nuevos datos de los productos del url con el show, uno debajo del otro en el txt  
        with open('inventario.txt','a') as file:
            for p in db:
                file.write(f"{p.showprod()}|\n")
        #Lee los datos (nuevos) agregados del txt para agregarlos a una lista y usarlos
        with open('inventario.txt','r') as file:
            for line in file:
                #line.split("|")[0] para apendiarlos sin el "\n", el "|" es parte del formarto del show
                products_list.append(line.split("|")[0])


    #--Para abrir datos cargados y reusarlos--
    def cargado_datos():
        #Lee los datos (guardados anteriormente) del txt para agregarlos a una lista y usarlos
        with open('inventario.txt','r') as file:
            for line in file:
                products_list.append(line.split("|")[0])

    #CARGADO DE DATOS
    print("\nAntes de iniciar el programa que datos le gustaria cargar al programa?")

    selection = False
    while selection == False:
        print("")
        data = ["Cargar datos guardados (carga los datos guardos)", "Reiniciar solo datos de productos (Borra solo los datos de productos y carga el resto)" ]
        for n in range(len(data)):
            print(f"{n+1}.{data[n]}")

        charge = options_menu(data)
        while charge == "Error! por favor intente de nuevo":
            print(charge)
            charge = options_menu(data)

        #--Cargar datos guardados (carga los datos guardos)--
        if charge == 1:
            print("Esta seguro de que quiere usar los datos guardados?")
            conf = input("s/n ---> ")
            option = confirmation(conf)
            while option == "Confirmacion invalida, introduzca un valor valido":
                print(option)
                conf = input("s/n ---> ")
                option = confirmation(conf)
            if option == "n":
                selection = False
            if option == "s":
                cargado_datos()
                #falatarian los demas datos de los otros modulos
                cargando_txt('clientes.txt',customer_list)
                cargando_txt('pagos.txt',pay_list)
                cargando_txt('ventas.txt',sale_list)
                cargando_txt('envios.txt',shipping_list)
                selection = True

        #--Reiniciar solo datos de productos (Borra solo los datos de productos y carga el resto)--
        if charge == 2:
            print("Esta seguro de quiere reiniciar los datos de productos y cargar el resto de datos?")
            conf = input("s/n ---> ")
            option = confirmation(conf)
            while option == "Confirmacion invalida, introduzca un valor valido":
                print(option)
                conf = input("s/n ---> ")
                option = confirmation(conf)
            if option == "n":
                selection = False
            if option == "s":
                reinicio()
                #falatarian los demas datos de los otros modulos
                cargando_txt('clientes.txt',customer_list)
                cargando_txt('pagos.txt',pay_list)
                cargando_txt('ventas.txt',sale_list)
                cargando_txt('envios.txt',shipping_list)
                selection = True
        
    #print (products_list)
    #MENU DE LA TIENDA
    tienda = ["Gestion de productos", "Gestion de ventas", "Gestion de clientes", "Gestion de pagos", "Gestion de envios","Indicadores de gestiton (estadisticas, no creado)","Finalizar programa"]

    print("""
    -----Tienda de Productos en linea-----

    Bienvenido :D

    Elija lo que desea hacer a continuacion:

    MENU
    """)


    #Mostrar menu
    for n in range(len(tienda)):
        print(f"{n+1}.{tienda[n]}")

    chose = options_menu(tienda)

    #print(customer_list)
    #Modulos del programa
    if chose == 1:
        repeat = gestion_productos(products_list)
        if repeat == "menu":
            return store()
    if chose == 2:
        repeat = gestion_de_venta(customer_list, products_list, sale_list, pay_list, shipping_list, purchase_of_products)
        if repeat == "menu":
            return store()
    if chose == 3:
        repeat = gestion_clientes(customer_list)
        if repeat == "menu":
            return store()
    if chose == 4:
        repeat = gestion_de_pagos(pay_list)
        if repeat == "menu":
            return store()
    if chose == 5:
        repeat = gestion_de_envios(shipping_list)
        if repeat == "menu":
            return store()
    if chose == 6:
        print("Fuera de servicio :c\n Por favor elija otro modulo")
        return store()
    if chose == 7:
        print("""
    --- Fin del programa :D ---
       Gracias por su visita
    """)



store()
