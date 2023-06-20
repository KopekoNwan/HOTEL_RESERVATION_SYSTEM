from model.Host import pb
from model.customers_list import customer

def get_customers() -> list[customer]:
    records = pb.collection('customers').get_full_list()
    list_of_customers = map(
        lambda x:
            customer(
                data=x.__dict__['collection_id']
            ), records
    )

    return list(list_of_customers)