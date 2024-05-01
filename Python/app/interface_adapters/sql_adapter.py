from sqlalchemy.orm import Session
from .i_database import IDatabase

class SQLAdapter(IDatabase):
    def __init__(self, database_engine):
        self.database_engine = database_engine

    def write(self, model, data: dict):
        with Session(self.database_engine) as session:
            try:	
                save_data = model(**data) 
                session.add(save_data)
                session.commit()
                return save_data

            except Exception as e:
                session.rollback()
                raise e