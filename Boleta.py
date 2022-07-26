class boleta:
    def __init__(self, idBoleta, numeroBoleta, producto, cantidad, precioProducto, subTotal):
        self.idBoleta = idBoleta
        self.numBol = numeroBoleta
        self.product = producto
        self.amnt = cantidad 
        self.productPrice = precioProducto
        self.subTotal = subTotal

    def mostrarBoleta(self):
        print("id de Boleta : " + self.idBoleta)
        print("Número de boleta : " + self.numBol)
        print("Producto a adquirir  : " + self.product.mostrarproducto())
        print("Cantidad :" + self.amnt)
        print("Precio del articulo : " + self.productPrice)
        print("Subtotal : " + self.subTotal)