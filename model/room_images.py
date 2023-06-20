from pocketbase.models.utils import BaseModel

class room_images(BaseModel):
    id:str
    classification:str
    room_image:str

    def load(self, data: dict):
        super().load(data)
        self.classification = data.get('classification', '')
        self.room_image = data.get('room_image', '')

        return self