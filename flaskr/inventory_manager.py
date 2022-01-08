from flaskr.item import Item

class Manager:

    PAGE_SIZE = 5

    def __init__(self,database):
        self.db = database
        self.next_id = 0
    
    def get_page(self,page):
        return list(
                self.db['inventory'].find()
                .skip(page * Manager.PAGE_SIZE)
                .limit(Manager.PAGE_SIZE)
            )
    
    def delete_item(self,id):
        self.db['inventory'].delete_one({'id_':id})
    
    def create_item(self):
        item = Item(self.next_id)
        self.next_id += 1
        self.db['inventory'].insert_one(
                item.to_dict()
            )
        return self.next_id - 1

    def edit_item(self, id,item):
        self.db['inventory'].update_one(
            {'id_':id},
            {'$set':item.to_dict()}
        )
    
    def get_item(self,id):
        return self.db['inventory'].find_one({'id_':id})
    
    def to_csv(self):
        csv_list = [['name','id','description','quantity','unit value','total value']]
        items = self.db['inventory'].find()
        for item in items:
            csv_list.append(Item.from_dict(item).to_list())
        return csv_list
