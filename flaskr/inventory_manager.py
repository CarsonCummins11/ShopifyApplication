from flaskr.item import Item

class Manager:

    PAGE_SIZE = 5 #the number of items to render on a given page - keeping it low so it's easy to check out this functionality

    '''
    constructor to allow this object persistent access to the database
    and to maintain track of what the next unique id will be (simply incrementing an int, assuming no more than 2^32 items will be created)
    '''
    def __init__(self,database):
        self.db = database
        self.next_id = 0
    

    '''
    makes use of a classic mongodb design pattern, although normally this will include a sort command for relevance to a search
    query - we obviously don't have that as we don't have a search query
    '''
    def get_page(self,page):
        return list(
                self.db['inventory'].find()
                .skip(page * Manager.PAGE_SIZE)
                .limit(Manager.PAGE_SIZE)
            )
    '''
    just uses the mongodb built in delete method, very simple
    '''
    def delete_item(self,id):
        self.db['inventory'].delete_one({'id_':id})
    

    '''
    creates an item using the item constructor to get the defaults in a clean pythonic way
    increments the next_id to the next unique id
    and puts the the new item in our database
    '''
    def create_item(self):
        item = Item(self.next_id)
        self.next_id += 1
        self.db['inventory'].insert_one(
                item.to_dict()
            )
        return self.next_id - 1
    '''
    
    '''
    def edit_item(self, id,item):
        self.db['inventory'].update_one(
            {'id_':id},
            {'$set':item.to_dict()}
        )
    '''
    
    '''
    def get_item(self,id):
        return self.db['inventory'].find_one({'id_':id})
    

    '''
    
    '''
    def to_csv(self):
        csv_list = [['name','id','description','quantity','unit value','total value']]
        items = self.db['inventory'].find()
        for item in items:
            csv_list.append(Item.from_dict(item).to_list())
        return csv_list
