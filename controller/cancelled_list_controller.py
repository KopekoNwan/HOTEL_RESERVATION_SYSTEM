from model.Host import pb
from model.cancelled_list import cancelled

def get_cancelled_list() -> list[cancelled]:
    records = pb.collection('cancelled_reservation').get_full_list()
    list_of_cancelled = map(
        lambda x:
            cancelled(
                data=x.__dict__['collection_id']
            ), records
    )

    return list(list_of_cancelled)