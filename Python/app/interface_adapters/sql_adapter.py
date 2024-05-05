from sqlalchemy import select
from .i_database import IDatabase

class SQLAdapter(IDatabase):
    def __init__(self, database_engine):
        self.db = database_engine


    def get(self, model, id: int):
        return self.db.session.get(model, id)
    
    def get_all_city_rates(self, model, id):
        return self.db.session.query(model).filter(model.city_id == id).all()


    def write(self, model, data: dict):
        self.db.session.begin()
        try:	
            save_data = model(**data) 
            self.db.session.add(save_data)

        except Exception as e:
            self.db.rollback()
            raise e
        else:
            self.db.session.commit()
            return save_data