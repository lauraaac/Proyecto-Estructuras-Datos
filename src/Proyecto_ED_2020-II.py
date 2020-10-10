import django
print("hola mundo")
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class lista_enlazada:
    def mostrar_lista(self,head):ED
        current = head
        while current:
            print (current.data)
            current = current.next
    def insertar(self,head,data):
        if(head== None):
            return Node(data)
        head.next= self.insertar(head.next,data)
        return head 
inventario=lista_enlazada()
head=None
usuarios={"pepito123":("123456", "inventario"),"juanita123":("654321","produccion")}
#se toma cada linea del archivo y hace casting a los datos que lo requieren
for line in open("prueba_de_veras_.txt", "r").readlines():
    data=line.strip().split(",")
    #codigo producto
    data[2]=int(data[2])
    #Unidades producto
    data[6]=int(data[6])
    #Vida útil producto
    data[7]=int(data[7])
    #Costo unitario
    data[8]=float(data[8])
    #Costo total
    data[9]=float(data[9])
    #Se crea la tupla con los datos y se agrega a la lista enlazada
    datos=[data[0], data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9]]
    head=inventario.insertar(head,datos)
inventario.mostrar_lista(head)
bandera_ingreso=False
while(bandera_ingreso==False):
    print("_________________________________")
    print("Bienvenido a Alpina")
    print("Ingrese Usuario y Contraseña:")
    usuario=input("Usuario:")
    contraseña=input("Contraseña:")
    print("_________________________________")
    clave_usuario=usuarios[usuario]
    #Se pide el usuario y la contraseña para poder ingresar a la plataforma
    if(usuario in usuarios and clave_usuario[0]==contraseña):
            bandera_ingreso=True
            actual=head
            while (actual):
                producto= actual.data
                print("__________________________________")
                print("Producto:",producto[4])
                print("Descripción", producto[3])
                print("Cantidad:",producto[6])
                print("Fecha vencimiento:", producto[5])
                print("__________________________________")
                actual=actual.next
            seleccion=0
            volver=0
            #Se pide que el usuario seleccione la opción que desee
            #Tendrá la opcíon de devolverse 
            while(volver==0):
                print("Seleccione:")
                print("1.Actualizar Inventario:")
                print("2.Donaciones:")
                print("3.Buscar:")
                seleccion=int(input())
                #se piden los datos, a pesar de que solo los que tienen asterisco son obligarios los otros deben tener un 0 (cero)
                if(seleccion==1):
                    print("______________________________")
                    print("* -> campo obligatorio")
                    codigo=int(input("Código producto*:"))
                    print(codigo)
                    cantidad=int(input("Cantidad*:"))
                    print(cantidad)
                    ciudad=input("Ciudad:")
                    print(ciudad)
                    lote=input("Fecha lote(DD/MM/AAAA)*:")
                    print(lote)
                    producto=input("Producto:")
                    descripcion=input("Descripción:")
                    vida_util=input("Vida Útil:")
                    caducidad=input("Fecha caducidad(DD/MM/AAAA)*:")
                    print(caducidad)
                    costo_unitario=float(input("Costo Unitario:"))
                    print(costo_unitario)
                    #Una vez se ingresan los datos, este podrá ser agregado o actualizado
                    print("Procesando....¿Desea agregar o actualizar?")
                    print("1. Agregar")
                    print("2. Actualizar")
                    print("3.Salir")
                    agregar_actualizar=int(input())
                    #Agregar: ingresará a la lista encadenada
                    if(agregar_actualizar==1):
                        try:
                            datos=[lote, ciudad, codigo,descripcion,producto,caducidad,cantidad,vida_util,costo_unitario ]
                            head= inventario.insertar(head,datos)
                            print("Actualización Exitosa")
                            volver=int(input("Presione 0 para volver otro para salir..."))
                        except:
                            print("Error en la actualización")
                    #Actualizar: tomará en cuenta el codigo del producto (unico) y la fecha de lote , estas actualizaciones serán de la cantidad de productos
                    elif(agregar_actualizar==2):
                        actual=head
                        while(actual):
                            producto=actual.data
                            try:
                                if(codigo in producto and producto[0]==lote):
                                    producto[6]= cantidad
                                    print("Actualización exitosa")
                            except:
                                print("Error en la actualización")
                            actual=actual.next
                        print("Presione 0 para volver otro para salir...")
                        volver=int(input())
                    print("______________________________")  
                #Donaciones: Queda pendiente para hacer                
                elif(seleccion==2):
                    #Importante hacer este!!!
                    print("se ingresan los datos del producto y pasa a la cola de donaciones")
                #Se busca el producto teniendo en cuenta su codigo, puede arrojar más de 1 resultado ya que hay diferentes lotes.
                elif(seleccion==3):
                    busqueda=int(input("Código producto: "))
                    actual=head
                    while(actual):
                        producto=actual.data
                        if(busqueda in producto):
                            try:
                                print("__________________________________")
                                print("Producto:",producto[4])
                                print("Descripción", producto[3])
                                print("Cantidad:",producto[6])
                                print("Fecha vencimiento:", producto[5])
                                print("__________________________________")
                            except:
                                print("Not Found")
                        actual=actual.next
                    volver=int(input("Presione 0 para volver otro para salir..."))
                else:
                    print("Ingrese una opción válida")
                
    else:
        print("usuario o clave incorrecta")
        print("Hola mundo")

        

