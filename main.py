from Producto import product
from Boleta import boleta

listaproductos=[]
listaboleta=[]
numboleta=100
idboleta=10
def mostrarboleta():
    print("")
    print("******** PYTHON STORE | FERRETERÍA *********")
    print("--------------------")
    print("{:<5}".format("Boleta NRO*"))
    print("{:<5}".format(numboleta))
    print("--------------------")
    
    total = 0
    print("{:<10} | {:<38} | {:<10} | {:<10} |".format("Cantidad", "Descripción", "Precio", "Sub Total"))
    print("--------------------------------------------------------------------------------")
    for i in listaboleta:
        print("{:<10} | {:<38} | {:<10} | {:<10} |".format(i.amnt, i.product, i.productPrice, round(i.productPrice*i.amnt)))
        total+=i.productPrice
    print("----------------------")
    print("{:<5}".format("Total"))
    print("{:<5}".format(str(total)))
    print("----------------------")
def buscarid(id):
    for i in listaproductos:
        if id == i.id:
            return i
    return None

def buscaridPrecio(idPrecio):
    for i in listaproductos:
        if idPrecio == i.idPrecio:
            return i
    return None


producto = product(1, "Mazilla", 50, "Mazilla Mágica", "Herramientas", 1, 1500, 0.8)
listaproductos.append(producto)
producto = product(2,"Alicate",80,"Thor","Herramientas", 2, 2000, 0.6)
listaproductos.append(producto)
producto = product(3,"Clavos",100,"Clavo de acero","Herramientas", 3, 2000, 0.5)
listaproductos.append(producto)
producto = product(4,"Cemento",76,"PolPaico","Herramientas", 4, 2500, 0.5)
listaproductos.append(producto)
producto = product(5,"Brocha pelo de ardilla",50,"Peludita","Utilidades", 5, 2000, 0.4)
listaproductos.append(producto)
producto = product(6,"Carretilla",10,"Aigo","Herramientas", 6, 15000, 50)
listaproductos.append(producto)
producto = product(7,"Pegamento",100,"UwU","Utilidades", 7, 3000, 50)
listaproductos.append(producto)
producto = product(8,"Destornillador",60,"ToiLok","Materiales", 8, 2000, 50)
listaproductos.append(producto)
producto = product(9,"Arena",40,"CartagenaINC","Materiales", 9, 11000, 50)
listaproductos.append(producto)
producto = product(10,"Tambor",30,"Waiko","Utilidades", 10, 3000, 40)
listaproductos.append(producto)





while True:
    print("1. --Crear un producto--")
    print("2. --Editar un producto--")
    print("3. --Eliminar un producto--")
    print("4. --Iniciar Carrito de compras--")
    print("5. --Terminar la compra--")
    print("6. --Buscar un producto--")
    print("7. --Salir--")
    opc = int(input("--Ingrese una opción Valida:     --"))
    if(opc < 1) or (opc > 10):
        print("--La opcion que ingreso no es valida--")

    else:
        if opc == 1:
            id= int(input("Ingrese la id : "))
            actProd = buscarid(id)
            if actProd is None:
                nombre = input("--Ingrese el nombre del producto :")
                stock = int(input("--Ingrese Numero de stock : --"))
                proveedor = input("--¿Cual es su proveedor? : --")
                categoria = input("--Ingrese la categoría : -- ")
                idPrecio = int(input("--Ingrese la Id del precio : --"))
                precioLista = int(input("--Ingrese cual es el precio de la lista : --"))
                porGan = int(input("--Ingrese cual es el porcentaje de ganancia : --"))
                print("--Producto agregado existosamente--")
                nuevoproducto = product(id,nombre,stock,proveedor,categoria,idPrecio,precioLista,porGan)
                listaproductos.append(nuevoproducto)
            else:
                print("--Este producto ya existe--")

        elif opc == 2: #Editar un producto
            idbuscar = int(input("--Ingrese id del producto :--"))
            actProd = buscaridPrecio(idbuscar)
            if actProd is None:
                print("--No existe este producto--")
            else:
                nuevoproducto = input("--Ingrese el nuevo nombre del producto :")
                nuevostock = int(input("--Ingrese el Stock :"))
                nuevoproveedor = input("--Ingrese en nuevo nombre del Proveedor :")
                nuevacategoria = input("--Ingrese la nueva categoria :")
                nvoprecioLista = int(input("--Ingrese el nuevo precio de lista"))
                nvoporGan = int(input("--Ingrese  el porcentaje de ganancia"))
                actProd.actualizarProducto(nuevoproducto, nuevostock, nuevoproveedor, nuevacategoria, nvoprecioLista, nvoporGan)
                print("--Producto actualizado con éxito--")
                actProd.mostrarproducto()
        elif opc == 3:
            idbuscar = int(input("--Ingrese id del producto:"))
            actProd = buscarid(idbuscar)
            if actProd is None:
                print("--No existe este producto")
            else:
                listaproductos.remove(actProd)
                print("--Producto eliminado exitosamente...")

        elif opc == 4: #Generar carrito
            numboleta += 1
            idboleta *= 5
            while True:
                # product.mostrarproducto()
                print("{:<3} | {:<20} | {:<10} | {:<20} | {:<10}".format("ID", "NOMBRE", "STOCK", "PROVEEDOR", "CATEGORÍA"))
                for i in listaproductos:
                    (i.mostrarproducto())
                id = int(input("--Seleccione id :"))
                actproducto = buscarid(id)
                if actproducto is None:
                    print("--No se encuentra el producto")
                else:
                    if actproducto.stock != 0:
                        while True:
                            cantidadprod = int(input("--Ingrese cantidad a comprar : "))
                            if cantidadprod > 0:
                                if cantidadprod <= actproducto.stock:
                                    total = cantidadprod * (actproducto.precioLista * actproducto.porGan + actproducto.precioLista)
                                    Nuevaboleta = boleta(idboleta, numboleta, "NOMBRE", cantidadprod, total, total)
                                    listaboleta.append(Nuevaboleta)
                                    break
                                else:
                                    print("--Supera el stock--")
                                    print("--Stock no disponible--",actproducto.stock)
                            else:
                                print("--Cantidad Invalida--")
                    else: #No stock
                        print("--No hay Stock disponible--")
                print("--Desea continuar agregando al carrito?--")
                print("1.SI")
                print("2.NO")
                q = int(input("Respuesta: "))
                if q == 2:
                    break

        elif opc == 5:
            mostrarboleta()

        elif opc == 6:
            idbuscar = int(input("--Ingrese id del producto : --"))
            actProd = buscarid(idbuscar)
            if actProd is None:
                print("--No existe este producto--")
            else:
                actProd.mostrarproducto()

        elif opc == 7:
            print("--Gracias Por comprar en PYTHON STORE--")
            print("--Vuelva Pronto--")
            break