import flet as ft
from controller.room_controller import get_room
from controller.room_type_controller import get_room_types

list_of_types = get_room_types()
list_of_rooms = get_room()

def update_room(_):
    global list_of_rooms
    room_numbers.options.clear()
    room_types.options.clear()
    new_list = get_room()
    list_of_rooms = new_list
    for t in list_of_types:
        room_types.options.append(ft.dropdown.Option(f'{t.type}'))
    for e in new_list:
        if room_types.value == 'Standard':
            if e.room_type == 'v54ixd0f7vlu3kq':
                room_numbers.options.append(ft.dropdown.Option(f'{e.room_number}'))
        if room_types.value == 'Family':
            if e.room_type == '4yjezbow65i8fy6':
                room_numbers.options.append(ft.dropdown.Option(f'{e.room_number}'))
        if room_types.value == 'Premium':
            if e.room_type == 'pfit5otmnsqxxoz':
                room_numbers.options.append(ft.dropdown.Option(f'{e.room_number}'))
    room_numbers.update()
    room_types.update()

room_types = ft.Dropdown(width=100, height=30, border_color='white', content_padding=2, text_size=12, color='white', on_change=update_room, value='Standard', alignment=ft.alignment.center)
room_numbers = ft.Dropdown(width=100, height=30, border_color='white', content_padding=2, text_size=12, color='white', alignment=ft.alignment.center)
guest = ft.TextField(width=50, height=30, bgcolor='white', color='black', text_size=12, max_lines=1, content_padding=2)


for i in list_of_types:
    room_types.options.append(ft.dropdown.Option(f'{i.type}'))
for r in list_of_rooms:
    if room_types.value == r.room_type:
        room_numbers.options.append(ft.dropdown.Option(f'{r.room_number}'))

class available_room(ft.UserControl):

    def build(self):
        return ft.Row(
            [
                ft.Column(
                    [
                        ft.Text(value='Room Type', size=12, color='white'),
                        room_types
                    ]
                ),
                ft.Column(
                    [
                        ft.Text(value='Room Number', size=12, color='white'),
                        room_numbers
                    ]
                ),
                ft.Column(
                    [
                        ft.Text(value='Number of Guest', size=12, color='white'),
                        guest
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND
        )