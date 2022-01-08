class Item():
    def __init__(self, id_ ,name='New Item', description='No Description',quantity=1,unit_value=0):
        self.id_ = id_
        self.name = name
        self.description = description
        self.quantity = quantity
        self.unit_value = unit_value
        self.total_value = unit_value * quantity

    def to_dict(self):
        return {
            'id_':self.id_,
            'name':self.name,
            'description': self.description,
            'quantity':self.quantity,
            'total_value': self.total_value,
            'unit_value': self.unit_value
        }

    @staticmethod
    def from_dict(data):
        return Item(data['id_'],data['name'],data['description'],data['quantity'],data['unit_value'])

    def to_list(self):
        return [
                self.name,
                self.id_,
                self.description,
                self.quantity,
                self.unit_value,
                self.total_value
            ]

    def set_unit_value(self, value):
        self.unit_value = value
        self.total_value = self.quantity * self.unit_value

    def set_quantity(self, quantity):
        self.quantity = quantity
        self.total_value = self.quantity * self.unit_value
    