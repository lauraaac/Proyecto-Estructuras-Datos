import django
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class lista_enlazada:
    def mostrar_lista(self,head):
        current = head
        while current:
            print (current.data)
            current = current.next
    def lista_actualizada(self,head,archivo):
        current = head
        while current:
            lista=current.data
            lista[0]=lista[0].lstrip("'")
            lista[0]=lista[0].rstrip("'")
            lista[1]=lista[1].lstrip("'")
            lista[1]=lista[1].rstrip("'")
            lista[3]=lista[3].lstrip("'")
            lista[3]=lista[3].rstrip("'")
            lista[4]=lista[4].lstrip("'")
            lista[4]=lista[4].rstrip("'")
            lista[5]=lista[5].lstrip("'")
            lista[5]=lista[5].rstrip("'")
            dato=str(lista)
            dato=dato.lstrip("[")
            dato=dato.rstrip("]")
            archivo.write(lista[0]+","+lista[1]+","+str(lista[2])+","+lista[3]+","+lista[4]+","+lista[5]+","+str(lista[6])+","+
            str(lista[7])+","+str(lista[8])+","+str(lista[9])+"\n")
            current = current.next
    def insertar(self,head,data):
        new_node=Node(data)
        new_node.next=head
        head=new_node
        return head

inventario=lista_enlazada()
head=None
usuarios={"pepito123":("123456", "inventario"),"juanita123":("654321","produccion")}
#se toma cada linea del archivo y hace casting a los datos que lo requieren
for line in open("prueba_de_veras_.txt","r+").readlines():
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
bandera_ingreso=False
archivo_nuevo=open("prueba_de_veras_.txt","w")
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
                print("1.Agregar Inventario:")
                print("2.Actualizar Inventario:")
                print("3.Donaciones:")
                print("4.Buscar:")
                seleccion=int(input())
                #se piden los datos, a pesar de que solo los que tienen asterisco son obligarios los otros deben tener un 0 (cero)
                if(seleccion==1):
                    print("______________________________")
                    print("* -> campo obligatorio")
                    codigo=int(input("Código producto*:"))
                    cantidad=int(input("Cantidad*:"))
                    ciudad=input("Ciudad:")
                    lote=input("Fecha lote(DD/MM/AAAA)*:")
                    producto=input("Producto:")
                    descripcion=input("Descripción:")
                    vida_util=int(input("Vida Útil:"))
                    caducidad=input("Fecha caducidad(DD/MM/AAAA)*:")
                    costo_unitario=float(input("Costo Unitario:"))
                    costo_total=float(input("Costo total:"))
                    #Una vez se ingresan los datos, este podrá ser agregado o actualizado:
                    try:
                            existe=False
                            datos=[lote, ciudad, codigo,descripcion,producto,caducidad,cantidad,vida_util,costo_unitario,costo_total]
                            actual=head
                            while(actual):
                                producto=actual.data
                                if(producto[2]==codigo and producto[0]==lote):
                                    print("El producto ya existe. Para modificar vaya a la sección de actualización")
                                    existe=True
                                    break
                                actual=actual.next
                            if(not existe):
                                head= inventario.insertar(head,datos)
                                print("Actualización Exitosa")
                            print("__________________________________________")
                            volver=int(input("Presione 0 para volver otro para salir..."))
                    except:
                            print("Error en la agregación, revise que los datos sean acordes.")
                    #Actualizar: tomará en cuenta el codigo del producto (unico) y la fecha de lote , estas actualizaciones serán de la cantidad de productos
                if(seleccion==2):
                    print("______________________________")
                    print("* -> campo obligatorio")
                    codigo=int(input("Código producto*:"))
                    cantidad=int(input("Cantidad*:"))
                    lote=input("Fecha lote(DD/MM/AAAA)*:")
                    actualizado=False
                    actual=head
                    while(actual):
                        producto=actual.data
                        if(codigo in producto and producto[0]==lote):
                                producto[6]= cantidad
                                print("Actualización exitosa")
                        actual=actual.next
                    print("__________________________________________")
                    print("Presione 0 para volver otro para salir...")
                    volver=int(input())
                    print("______________________________")  
                #Donaciones: Queda pendiente para hacer                
                elif(seleccion==3):
                    #Importante hacer este!!!
                    print("se ingresan los datos del producto y pasa a la cola de donaciones")
                #Se busca el producto teniendo en cuenta su codigo, puede arrojar más de 1 resultado ya que hay diferentes lotes.
                elif(seleccion==4):
                    busqueda=int(input("Código producto: "))
                    actual=head
                    encontrado=False
                    while(actual):
                        producto=actual.data
                        if(busqueda in producto):
                            print("__________________________________")
                            print("Producto:",producto[4])
                            print("Descripción", producto[3])
                            print("Cantidad:",producto[6])
                            print("Fecha vencimiento:", producto[5])
                            print("__________________________________")
                            encontrado=True
                            break
                        actual=actual.next
                    if(not encontrado):    
                        print("Not Found")
                            
                    print("__________________________________________")
                    volver=int(input("Presione 0 para volver otro para salir..."))
                else:
                    print("Ingrese una opción válida")
            inventario.lista_actualizada(head,archivo_nuevo)
            print("¡Hasta pronto!")      
    else:
        print("usuario o clave incorrecta")

        

