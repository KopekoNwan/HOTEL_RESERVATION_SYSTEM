from pocketbase.models.utils import BaseModel

class room_types(BaseModel):
    type: str
    price: str

    def load(self, data: dict):
        super().load(data)
        self.type = data.get('type', '')
        self.price = data.get('price', '')
        return self