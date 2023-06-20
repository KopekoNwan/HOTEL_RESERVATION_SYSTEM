import flet as ft
from controller.room_controller import get_room
from controller.room_type_controller import get_room_types
from view.components.available_room import room_numbers
from view.components.available_room import room_types
from view.components.standard_room_view import append_Sroom_to_row
from view.components.family_room_view import append_Froom_to_row
from view.components.premium_room_view import append_Proom_to_row


def updated_records():
    #this function will keep our data up to date and updated every second
    get_room()

    #new list for room type containers
    new_Sroom_list = get_room()
    new_Proom_list = get_room()
    new_Froom_list = get_room()
    append_Sroom_to_row(f=new_Sroom_list)
    append_Froom_to_row(q=new_Proom_list)
    append_Proom_to_row(l=new_Froom_list)

    #for dropdown options
    list_of_types = get_room_types()
    new_list = get_room()
    room_list = new_list
    room_numbers.options.clear()
    room_types.options.clear()
    for t in list_of_types:
        room_types.options.append(ft.dropdown.Option(f'{t.type}'))
    for e in room_list:
        if room_types.value == e.room_type and e.status == True:
            room_numbers.options.append(ft.dropdown.Option(f'{e.room_number}'))
    room_numbers.update()