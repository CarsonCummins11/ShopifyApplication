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
    query - we obviously don't have that as we don't have a search query.
    Pagination will help decrease load times for our site, making it much more user friendly
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
    essentially replaces the old item with the new one in our database using the mongodb update command.
    Doing this instead of delete, insert allows us to speed up db access by using only one DB op rather than 2
    '''
    def edit_item(self, id,item):
        self.db['inventory'].update_one(
            {'id_':id},
            {'$set':item.to_dict()}
        )

    '''
    just a wrapper for a standard mongodb command
    '''
    def get_item(self,id):
        return self.db['inventory'].find_one({'id_':id})
    

    '''
    lists each item in our database and adds it to a python list object
    keeping everything in memory allows us to stay speedy, but this could be converted to multiple hard disk ops
    if the # of items becomes large enough
    '''
    def to_csv(self):
        csv_list = [['name','id','description','quantity','unit value','total value']]
        items = self.db['inventory'].find()
        for item in items:
            csv_list.append(Item.from_dict(item).to_list())
        return csv_list
