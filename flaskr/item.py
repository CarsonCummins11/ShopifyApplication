'''
simple data class to represent an item in the inventory system
'''

class Item():

    '''
    constructor with some defaults built in to keep everything clean
    '''
    def __init__(self, id_ ,name='New Item', description='No Description',quantity=1,unit_value=0):
        self.id_ = id_
        self.name = name
        self.description = description
        self.quantity = quantity
        self.unit_value = unit_value
        self.total_value = unit_value * quantity #keep this value calculated, should never differ from quantity * unit_value (obviously)

    '''
    just dumps our object data into a python dictionary so this object can interface with mongodb easily
    '''
    def to_dict(self):
        return {
            'id_':self.id_,
            'name':self.name,
            'description': self.description,
            'quantity':self.quantity,
            'total_value': self.total_value,
            'unit_value': self.unit_value
        }


    '''
    allows us to get the object back from data stored in mongodb
    by simply calling the constructor with the provided dictionary's values
    '''
    @staticmethod
    def from_dict(data):
        return Item(data['id_'],data['name'],data['description'],data['quantity'],data['unit_value'])


    '''
    converts all of this objects fields to a list so we can output to a CSV
    order is defined in the inventory_manager.py file
    '''
    def to_list(self):
        return [
                self.name,
                self.id_,
                self.description,
                self.quantity,
                self.unit_value,
                self.total_value
            ]

    '''
    setters for the unit value and quantity that should be used
    in order to ensure total_value stays correct
    '''

    def set_unit_value(self, value):
        self.unit_value = value
        self.total_value = self.quantity * self.unit_value

    def set_quantity(self, quantity):
        self.quantity = quantity
        self.total_value = self.quantity * self.unit_value
    