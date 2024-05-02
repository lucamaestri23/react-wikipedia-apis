from src.Configuration.database import db_connection
from src.Model.pilot_model import PilotModel
from src.Repository.pilot_repository import PilotRepository


class PilotService:
    def __init__(self) -> None:
        mydb, mycursor = db_connection()
        self.connection = {'mydb': mydb, 'mycursor': mycursor}
        self.ticket_repository = PilotRepository(self.connection)

    def get_pilots(self):
            payload = self.ticket_repository.get_all()
            self.connection['mydb'].close()
            return payload