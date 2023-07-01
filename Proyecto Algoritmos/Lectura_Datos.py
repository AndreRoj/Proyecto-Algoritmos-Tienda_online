#Funciones para la carga de datos
#--Para borrar ciertos datos--  
def reinicio_datos(txt):
    #borra los datos en el archivo txt
    with open(txt,'w') as file:
        file.write("")

#--Para abrir datos cargados y reusarlos--
def cargando_txt(txt,list):
    #Lee los datos (guardados anteriormente) del txt para agregarlos a una lista y usarlos
    with open(txt,'r') as file:
        for line in file:
            list.append(line.split("|")[0])

#-COMO SE APENDEARIA LA LISTA CON LOS NUEVOS DATOS A EL TXT PARA SER USADOS DE NUEVO
def subir_datos(txt,list):
    with open(txt,'w') as file:
            file.write("")
    with open(txt,'a') as file:
            for p in list:
                file.write(f"{p}|\n")

