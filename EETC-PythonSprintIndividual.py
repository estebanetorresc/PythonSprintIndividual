# Proyecto individual -- Sprint Individual
# Autor: Esteban Torres
import os
import random
import string

# Variables
usuariosList =['Esteban','Carlos','Pedro','Luis','Mario','Juan','Patricio','Alberto','Domingo','Adolfo']
cuentasUsuarios ={}

#Funciones 
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

#Funcion para generar las contraseñas
def get_random_password():
    random_source = string.ascii_letters + string.digits + string.punctuation
    # select 1 lowercase
    password = random.choice(string.ascii_lowercase)
    # select 1 uppercase
    password += random.choice(string.ascii_uppercase)
    # select 1 digit
    password += random.choice(string.digits)
    # select 1 special symbol
    password += random.choice(string.punctuation)

    # generate other characters
    for i in range(6):
        password += random.choice(random_source)

    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password


#Funcion que se encarga de mostrar todos los usuarios que se encuentran pendientes de ser creados con cuentas
def mostrarUsuarios(usuariosList:list):

   indice = 0
   print('----------------------------')
   print('LISTADO USUARIOS SIN CUENTAS')
   print('----------------------------')
   print(' ') 

   #Ciclo que se encarga de leer uno a uno los usuarios de la lista para uluego imprimirlos       
   for usuario in usuariosList:
       indice +=1
       print (f'  {indice} - {usuario}')
  
   print(' ')        
   print(' ')           
   return usuariosList

#Funcion que se encarga generar las cuentas de usuarios pendientes
def crearCuentas(usuariosList):
   cuentasDic ={}
   opcion ='S'

   while opcion == 'S':
        clearConsole()
        print('----------------------------')
        print('GENERAR CUENTAS DE USUARIOS')
        print('----------------------------')
        print(' ') 
        #Llamamos a la funcion que muestra los usuarios pendientes de cuentas por crear
        usuariosList = mostrarUsuarios(usuariosList)

        opcion = int(input('Indique el numero del usuario a crear: '))
        
        print('----------------------------')
        print(f'INFORMACION: Se creara la cuenta del ususario {usuariosList[opcion-1]}')
        
        #Validamos el ingreso de los digitos de telefono sean mayor a 8
        while True:
            print(' ')
            telefono= input('  Ingrese el telefono (Ingrese 8 digitos): ')
        
            if len(telefono)>=8:
                break
            else:
                print ('')
                print('  ALERTA: El telefono debe ser mayor a 8 digitos') 
                print('')

        #creamos la contraseña
        contrasena = get_random_password()
        
        cuentasDic[usuariosList[opcion-1]] = {'telefono':telefono,'contrasena':contrasena}
        print('')
        print(' INFORMACION: Usuario creado Satisfactoriamente..........')
        
        #Borramos el usuario de la lista de los pendientes
        usuariosList.remove(usuariosList[opcion-1])
        
        print ('')
        print ('')
        opcion = input('    ¿Desea generar otra cuenta? (S/N) ').upper()

   return cuentasDic

#Funcion que se encarga de mostrar las cuentas de usuarios creados
def mostrarCuentas(cuentasUsuarios):
   indice=0
   print('------------------------------')
   print('LISTADO DE CUENTAS EXISTENTES')
   print('------------------------------')
   print('')         
   #Recorremos la lista de usuarios
   for datos in cuentasUsuarios.items():
       indice += 1
       print(f'{indice}.- {datos}')
       
   print('')
   print('')      
   continuar = input('Presiona ENTER para continuar.....')

#-----------Inicio del Programa--------------#
print('---------------------------------')
print('BIENVENIDO A REGISTRO DE USUARIOS')
print('---------------------------------')
while True: 
    clearConsole()
    print('-------------------------------------------')
    print('------------------ MENU -------------------')
    print('-------------------------------------------')
    print('1. Mostrar lista usuarios sin cuentas')
    print('2. Generar cuenta automaticamente')
    print('3. Mostrar lista de usuarios con cuentas')
    print('4. Salir del programa')
    print('')
    print('--------SELECCIONE UNA OPCION-------------')
    print ('')
    opcion = input('Seleccione una opcion---> ')
    print('------------------------------------------')   
    clearConsole()

    if opcion == '1':
       clearConsole() 
       usuariosList = mostrarUsuarios(usuariosList) 
       enter = input('Presiona ENTER para continuar..........') 
    elif opcion == '2':
       clearConsole()
       cuentasUsuarios.update(crearCuentas(usuariosList))
       
    elif opcion == '3':
       clearConsole()
       mostrarCuentas(cuentasUsuarios)

    elif opcion == '4':
       break

    print (' ') 
    print (' ') 
    print ('Muchas Gracias')
    print (' ') 
#-----------Fin del Programa -----------------#
