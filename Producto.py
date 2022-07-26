from Precio import precio
class product(precio):
    def __init__(self, id, nombre, stock, proveedor, categoria,idDePrecio, preciodeLista, porGan):
        super(product, self).__init__(idDePrecio, preciodeLista, porGan)
        self.id = id
        self.name = nombre
        self.stock = stock
        self.proveedor = proveedor
        self.categoria = categoria

    def mostrarproducto(self):
        print("{:<3} | {:<20} | {:<10} | {:<20} | {:<10}".format(str(self.id), self.name, str(self.stock), self.proveedor, self.categoria))
        
    def actualizarProducto(self, nuevoProducto, nuevoStock, nuevoProv, nuevaCat, nueviPrecioList, NuevoPorGan):
        self.name = nuevoProducto
        self.stock = nuevoStock
        self.proveedor = nuevoProv
        self.categoria = nuevaCat
        self.precioLista = nueviPrecioList
        self.porGan = NuevoPorGan
