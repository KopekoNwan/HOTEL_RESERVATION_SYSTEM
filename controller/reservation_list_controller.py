from model.Host import pb
from model.reservation_list import reservation_list

def get_reservations() -> list[reservation_list]:
    records = pb.collection('reservation_list').get_full_list()
    list_of_reservations = map(
        lambda x:
            reservation_list(
                data=x.__dict__['collection_id']
            ), records
    )

    return list(list_of_reservations)