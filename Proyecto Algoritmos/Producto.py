class Producto:
  def __init__(self, name, description, price, category, quantity):
    self.name = name
    self.description = description
    self.price = price
    self.category = category
    self.quantity = quantity

  def showprod(self):
    return f"name:{self.name}/description:{self.description}/price:{self.price}/category:{self.category}/quantity:{self.quantity}"
  
  def show_atr(self):
    return f"""
    name:{self.name},
    description:{self.description},
    price:{self.price},
    category:{self.category},
    quantity:{self.quantity}"""