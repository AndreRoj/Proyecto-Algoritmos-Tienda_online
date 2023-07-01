import random

class Factura:
  def __init__(self, pay_number, name_cliente, id , buy_products, pay_type, payment_coin, shipping_method, subtotal, discount, iva, igtf, total, sale_date, pay_date, shipping_date):
    self.pay_number = pay_number
    self.name_cliente = name_cliente
    self.id = id
    self.buy_products =  buy_products
    self.pay_type = pay_type
    self.payment_coin = payment_coin
    self.shipping_method = shipping_method
    self.subtotal = subtotal
    self.discount = discount
    self.iva = iva
    self.igtf = igtf
    self.total = total
    self.sale_date = sale_date
    self.pay_date = pay_date
    self.shipping_date = shipping_date

  def show_venta(self):
    return f"numero de compra:{self.pay_number}/name:{self.name_cliente}/Rif o C.I:{self.id}/product list:{self.buy_products}/payment type:{self.pay_type}/payment coin:{self.payment_coin}/Shipping method:{self.shipping_method}/Subtotal:{self.subtotal}/discount(1.5%):{self.discount}/IVA(16%):{self.iva}/IGTF(3%):{self.igtf}/Total:{self.total}/sale date:{self.sale_date}/Payment date:{self.pay_date}"

  def show_pago(self):
    return f"name:{self.name_cliente}/payment amount:{self.total}/payment coin:{self.payment_coin}/payment type:{self.pay_type}/payment date:{self.pay_date}"
  
  def show_envio(self):
    if self.shipping_method == "Delivery":
      service_cost = "$5"
      motos = ["Carlos Ramirez, numero de matricula:JU1W23A","Juan Rodriguez, numero de matricula:SA1R23A","Maria Marquez, numero de matricula:KP1T23A"]
      motorizado = random.choice(motos)
      return f"numero de compra:{self.pay_number}/name:{self.name_cliente}/shipping method:{self.shipping_method}/datos del motorizado:{motorizado}/service cost:{service_cost}/shipping date:{self.shipping_date}"
    if self.shipping_method != "Delivery":
      service_cost = "$8"
      return f"numero de compra:{self.pay_number}/name:{self.name_cliente}/shipping method:{self.shipping_method}/service cost:{service_cost}/shipping date:{self.shipping_date}"

  def show_factura(self):
    print(f"""
                                        RIF J-00502005
                                Tienda de Productos en Linea
    -----------------------------------------------------------------------------------------
    Rif o C.I:{self.id}
    Nombre o Razon Social:{self.name_cliente}
    nº:{self.pay_number}
                                          FACTURA
    FECHA:{self.sale_date}                                      
    FECHA TOPE PARA REALIZAR EL PAGO:{self.pay_date}                       
    -----------------------------------------------------------------------------------------""")
    #separacion de los productos comprados
    compra = self.buy_products
    compra = compra.split(",")
    for index in range(len(compra)):
      print(f"""
    {compra[index]}""")
    print(f"""
    -----------------------------------------------------------------------------------------
    SUBTOTAL                                                          ${self.subtotal}
    -----------------------------------------------------------------------------------------
    Moneda de pago:{self.payment_coin}
    Forma de envio:{self.shipping_method}
    -----------------------------------------------------------------------------------------
    Descuento(1.5%): {self.discount}
    IVA(16%): {self.iva}
    IGTF(3%): {self.igtf}
    -----------------------------------------------------------------------------------------
    Metodo de pago:{self.pay_type}
    -----------------------------------------------------------------------------------------
    TOTAL                                                             {self.payment_coin}{self.total}
    """)
                  
