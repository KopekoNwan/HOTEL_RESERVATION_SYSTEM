from pocketbase.models.utils import BaseModel

class rooms(BaseModel):
    
    id: str
    room_number: str
    room_type: str
    price: str
    status: str

    def load(self, data: dict):
        super().load(data)
        self.room_number = data.get('room_number', '')
        self.room_type = data.get('room_type', '')
        self.price = data.get('price', '')
        self.status = data.get('status', '')

        return self