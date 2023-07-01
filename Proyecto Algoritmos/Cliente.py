class Cliente:
  def __init__(self, type, name, email, address, phone):
    self.type = type
    self.name = name
    self.email = email
    self.address = address
    self.phone = phone

  
class Juridico(Cliente):
  def __init__(self, type, name, email, address, phone, rif):
    super().__init__(type, name, email, address, phone)
    self.type = self.type
    self.rif = rif

  def showjurid(self):
    return f"customer type:{self.type}/name:{self.name}/email:{self.email}/shipping adress:{self.address}/phone:{self.phone}/rif:{self.rif}"
  
  def show_atr_jur(self):
    return f"""
    custumer type:{self.type},
    name:{self.name},
    email:{self.email},
    shipping adress:{self.address},
    phone:{self.phone},
    rif:{self.rif}"""

class Natural(Cliente):
  def __init__(self, type, name, last_name, email, address, phone, id):
    super().__init__(type, name, email, address, phone)
    self.type = self.type
    self.last_name = last_name
    self.id = id

  def shownatur(self):
    return f"customer type:{self.type}/name:{self.name}/last_name:{self.last_name}/email:{self.email}/shipping adress:{self.address}/phone:{self.phone}/id:{self.id}"
  
  def show_atr_natur(self):
    return f"""
    custumer type:{self.type},
    name:{self.name},
    last_name:{self.last_name},
    email:{self.email},
    shipping adress:{self.address},
    phone:{self.phone},
    id:{self.id}"""  
