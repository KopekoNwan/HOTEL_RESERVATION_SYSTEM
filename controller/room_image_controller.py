from model.Host import pb
from model.room_images import room_images

def get_room_images() -> list[room_images]:
    records = pb.collection('room_images').get_full_list()

    list_of_imgRoom = map(
        lambda x:
            room_images(
                data=x.__dict__['collection_id']
            ), records
    )

    return list(list_of_imgRoom)