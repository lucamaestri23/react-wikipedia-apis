from src.Model.pilot_model import PilotModel
from src.Repository.consultantQuery import query_db
import mysql.connector

class PilotRepository:
    def __init__(self, connection) -> None:
        self.mycursor = connection['mycursor']
        self.mydb = connection['mydb']

    def get_all(self):
        query = """
        SELECT id,name,team,gpwin,gpmade,points,podiums,pole,fastestlap
        FROM pilots;
        """
        result = query_db(self.mycursor, query)
        result = list(map(lambda value: PilotModel(**value), result))
        return result