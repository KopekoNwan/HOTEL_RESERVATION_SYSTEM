from pocketbase.models.utils import BaseModel

class reservation_list(BaseModel):

    user: str
    last_name: str
    first_name: str
    contact_number: int
    email: str
    guest: str
    room: str
    check_in: str
    check_out: str
    room_id: str
    state:str

    def load(self, data: dict):
        super().load(data)
        self.user = data.get('user', '')
        self.last_name = data.get('last_name', '')
        self.first_name = data.get('first_name', '')
        self.contact_number = data.get('contact_number', '')
        self.email = data.get('email', '')
        self.guest = data.get('guest', '')
        self.room = data.get('room', '')
        self.check_in = data.get('check_in', '')
        self.check_out = data.get('check_out', '')
        self.room_id = data.get('room_id', '')
        self.state = data.get('state', '')

        return self