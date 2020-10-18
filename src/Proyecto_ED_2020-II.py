import django
# Se importan las siguientes librerias para tiempo 
from datetime import datetime 
from datetime import date
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class node_dll (Node):
    def __init__(self, data):
        Node.__init__(self,data)
        self.before = None

    # Se agrega elemento, siempre poner el self es importante    
    def __str__ (self): 
        return str( self.data)


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
            if type(lista[5]) != str:
                lista[5] = lista[5].strftime('%d/%m/%Y')
            else:
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


class dll_queue:
    # Constructor de la clase 
    def __init__(self):
        self.head = None
        self.tail = None 
        self.size = 0 

    # Se pregunta si está vacía 
    def Empty (self):
        if self.head == None:
            return True
        else:
             return False 

    # Se añade el dato a la lista         
    def enqueue(self, value): 
        if self.tail is None: 
            self.head =node_dll(value) 
            self.tail =self.head 
        else: 
            self.tail.next = node_dll(value) 
            self.tail.next.before= self.tail
            self.tail = self.tail.next
        self.size += 1

    # Se borra el elemento 
    def dequeue (self):
        if self.head == None:
            return None    
        else: 
            current = self.head.data
            self.head = self.head.next
            self.head.before = None 
            self.size -= 1
            return current
 
    # Se imprime el primer dato 
    def top (self):
        return self.head.data 

    # Se imprime los elementos de la lista 
    def __str__ (self):
        if self.size == 0:
            return False
        else:
            string = "["
            current = self.head 
            while current != None:
                if current.next == None:
                    string += str(current.data)  
                else: 
                    string += str(current.data)
                    string += str(", \n")
                current = current.next
            string += "]"
        print(string)


inventario=lista_enlazada()
head=None
cola = dll_queue()

usuarios={"pepito123":("123456", "inventario"),"juanita123":("654321","produccion")}
#se toma cada linea del archivo y hace casting a los datos que lo requieren
for line in open("10K_Datos_.txt","r+", encoding="utf8").readlines():
    data=line.strip().split(",")
    #codigo producto
    data[2]=int(data[2])
    #fecha de vencimiento
    data[5] = datetime.strptime(data[5],'%d/%m/%Y')
    #Unidades producto
    data[6]=float(data[6])
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
archivo_nuevo=open("10K_Datos_.txt","w",encoding="utf8")
archivo_donaciones = open("Donaciones.txt","w",encoding="utf8")
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
            actual = head
            while (actual):
                producto= actual.data
                """print("__________________________________")
                print("Producto:",producto[4])
                print("Descripción", producto[3])
                print("Cantidad:",producto[6])
                print("Fecha vencimiento:", producto[5])
                print("__________________________________")"""
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
                print("5. Salir")
                seleccion=input()
                #se piden los datos, a pesar de que solo los que tienen asterisco son obligarios los otros deben tener un 0 (cero)
                if(seleccion == "1"):
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
                elif(seleccion=="2"):
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
                elif(seleccion=="3"):
                    #Importante hacer este!!!
                        print("Los porductos en cola de donación son:\n")
                        actual = head
                        while (actual):
                            try:
                                producto = actual.data
                                # Se toma la fehca actual 
                                fecha_actual =  datetime.now()
                                # Se hace la resta de días
                                diferencia = abs((fecha_actual - producto[5]).days)
                                # Teniendo una vez la diferencia entoces 
                                if producto[5] < fecha_actual and diferencia >= 15  and diferencia<= 300:
                                    producto[5] = producto[5].strftime('%d/%m/%Y') 
                                
                                    cola.enqueue(producto)
                                    archivo_donaciones.write(str(producto)+"\n")

                                    print("__________________________________")
                                    print("Producto:",producto[4])
                                    print("Descripción", producto[3])
                                    print("Cantidad:",producto[6])
                                    print("Fecha vencimiento:", producto[5])
                                    print("__________________________________\n")

                                elif producto[5] < fecha_actual  and diferencia > 300 :
                                    print("on time\n")
                                else:
                                    if producto[5] > fecha_actual  and diferencia < 15:
                                        print("Apunto de vencer\n")
                                    else:
                                        print("Vencido\n")
                                
                            except:
                                    print("Error en el formato de la fecha, verifique que el formato de la fecha éste bien ingresado")
                            
                            actual = actual.next
                        volver=0

                #Se busca el producto teniendo en cuenta su codigo, puede arrojar más de 1 resultado ya que hay diferentes lotes.
                elif(seleccion=="4"):
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
                    volver=int(input("Presione 0 para volver, otro para salir..."))

                elif(seleccion == "5"):
                    volver = 1

                else:
                    print("Ingrese una opción válida")

            inventario.lista_actualizada(head,archivo_nuevo)
            print("¡Hasta pronto!")      
    else:
        print("usuario o clave incorrecta")

        

