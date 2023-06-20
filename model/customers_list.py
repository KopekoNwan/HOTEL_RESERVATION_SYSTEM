from pocketbase.models.utils import BaseModel

class customer(BaseModel):

    last_name:str
    first_name:str
    email:str
    contact:str
    reservation_id:str
    room:str
    check_in:str
    check_out:str

    def load(self, data: dict):
        super().load(data)
        self.last_name = data.get('last_name', '')
        self.first_name = data.get('first_name', '')
        self.email = data.get('email', '')
        self.contact = data.get('contact', '')
        self.room = data.get('room', '')
        self.check_in = data.get('check_in', '')
        self.check_out = data.get('check_out', '')

        return self