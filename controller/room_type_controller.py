from model.Host import pb
from model.room_types import room_types

def get_room_types() -> list[room_types]:
    records = pb.collection('types_of_room').get_full_list()

    list_of_types = map(
        lambda x:
            room_types(
                data=x.__dict__['collection_id']
            ), records
    )

    return list(list_of_types)