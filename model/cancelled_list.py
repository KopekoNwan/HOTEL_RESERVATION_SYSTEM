from pocketbase.models.utils import BaseModel

class cancelled(BaseModel):

    user: str
    cancelled_date: str
    customer: str
    reservation_id: str
    email:str
    contact:str

    def load(self, data: dict):
        super().load(data)
        self.user = data.get('user', '')
        self.cancelled_date = data.get('cancelled_date', '')
        self.customer = data.get('customer', '')
        self.reservation_id = data.get('reservation_id', '')
        self.email = data.get('email', '')
        self.contact = data.get('contact', '')

        return self