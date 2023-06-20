from model.Host import pb
from model.rooms import rooms

def get_room() -> list[rooms]:
    records = pb.collection('rooms').get_full_list()
    list_of_rooms = map(
        lambda x:
            rooms(
                data=x.__dict__['collection_id']
            ), records
    )

    return list(list_of_rooms)