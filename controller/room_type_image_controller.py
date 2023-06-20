from model.Host import pb
from model.room_images import room_images

def get_Sroom_images() -> list[room_images]:
    records = pb.collection('room_images').get_full_list(
        query_params={
            'filter' : 'classification = "Standard"'
        }
    )

    list_of_imgRoom = map(
        lambda x:
            room_images(
                data=x.__dict__['collection_id']
            ), records
    )

    return list(list_of_imgRoom)

def get_Froom_images() -> list[room_images]:
    records = pb.collection('room_images').get_full_list(
        query_params={
            'filter' : 'classification = "Family"'
        }
    )

    list_of_imgRoom = map(
        lambda x:
            room_images(
                data=x.__dict__['collection_id']
            ), records
    )

    return list(list_of_imgRoom)

def get_Proom_images() -> list[room_images]:
    records = pb.collection('room_images').get_full_list(
        query_params={
            'filter' : 'classification = "Premium"'
        }
    )

    list_of_imgRoom = map(
        lambda x:
            room_images(
                data=x.__dict__['collection_id']
            ), records
    )

    return list(list_of_imgRoom)