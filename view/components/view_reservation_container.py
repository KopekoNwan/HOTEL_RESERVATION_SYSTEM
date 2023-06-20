import pocketbase
import flet as ft
import datetime
import time
from view.components.cal_container import cal_container
from view.components.date_picker_container import date_picker_container
from view.components.available_room import available_room
from model.Host import pb
from view.components.available_room import guest
from view.components.available_room import room_numbers
from view.components.available_room import room_types
from view.components.userID_Card import userIDField
from view.components.view_customers_container import customer_data
from view.components.view_cancelled_container import cancelled_data
from view.components.view_cancelled_container import counter
from view.components.view_customers_container import counter_customer
from controller.room_controller import get_room
from controller.room_type_controller import get_room_types
from view.components.standard_room_view import append_Sroom_to_row
from controller.customers_controller import get_customers

# from controller.cancelled_list_controller import get_cancelled_list
from view.components.family_room_view import append_Froom_to_row
from view.components.premium_room_view import append_Proom_to_row
from view.components.view_cancelled_container import append_cancelled_list
from view.components.view_customers_container import append_customer_list
from controller.reservation_list_controller import get_reservations
from view.components.cal_container import mark_day_reservations
from model.updated_records import updated_records
#above are all the imports...

#instance of the models(data):
room_list = get_room()
list_of_types = get_room_types()
hotel_rooms = get_room()
reservations = get_reservations()
customers = get_customers()
#-------------------------------#

#instance of the objects:
rooms_display = ft.Column([], scroll=ft.ScrollMode.ALWAYS, auto_scroll=True)
month_and_day = date_picker_container()
all_reservation_cont = cal_container()
room = available_room()
now = datetime.datetime.now()
room_row: list[ft.UserControl] = []
reservation_row: list[ft.UserControl] = []
table_lines: list[ft.UserControl] = []
list_of_list: list = []
current_color = ft.Text(value='')
#--------------------------------------------------------#

#variable containers:
room_count = {}
reserved_containers = {}
cancel_confirmations = {}
reserved_reservation_ids = {}
name_tags = {}
name_tag_buttons = {}
f_name = {}
l_name = {}
e_mail = {}
c_num = {}
#------------------------#

#all of my global variables:
s_num = 0
f_num = 0
p_num = 0
run_clock = True
check_in_value = ''
check_out_value = ''
#-------------------------#

#shows a row of room
def show_reservations():
    # global variables
    global hotel_rooms
    global reservations
    global s_num
    global f_num
    global p_num
    # local variable
    s_num=0
    f_num=0
    p_num=0

    # local variable controls re set value to zero(0)
    standard_num.value = f'{0}'
    family_num.value = f'{0}'
    premium_num.value = f'{0}'

    #function call
    mark_day_reservations()
    append_cancelled_list()
    append_customer_list()

    #getting the new record in collection if changes are made
    hotel_rooms = get_room()
    reservations = get_reservations()

    #clearing the controls
    f_name.clear()
    l_name.clear()
    e_mail.clear()
    c_num.clear()
    room_row.clear()
    reservation_row.clear()
    table_lines.clear()
    rooms_display.controls.clear()
    list_of_list.clear()
    room_count.clear()
    reserved_containers.clear()
    reserved_reservation_ids.clear()

    #updating the controls after clearing
    cancelled_data.update()
    customer_data.update()
    all_reservation_cont.update()
    standard_num.update()
    number_for_standard.update()
    family_num.update()
    number_for_family.update()
    premium_num.update()
    number_for_premium.update()
    counter.update()
    counter_customer.update()

    #loop to append empty Row control for every room available in the rooms collection(pocket_base)
    for z in hotel_rooms:
            room_row.append(ft.Row([], alignment=ft.CrossAxisAlignment.CENTER))
    for y in hotel_rooms:
            reservation_row.append(ft.Row([], width=920, alignment=ft.CrossAxisAlignment.CENTER, wrap=True))
    for t in hotel_rooms:
        table_lines.append(ft.Column([ft.Container(width=1130, border=ft.border.only(top=ft.BorderSide(1, color='#B7B7B7')))]))
    for l in hotel_rooms:
        list_of_list.append([])

    #appending the rooms to its corresponding room type Row container
    for hs_room in hotel_rooms:
        if hs_room.room_type == 'v54ixd0f7vlu3kq':
            room_row[int(hs_room.room_number) - 1].controls.append(
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Container(
                                    content=ft.Text(value='S', color='white', font_family='Arial', size=10, weight=ft.FontWeight.BOLD),
                                    shape=ft.BoxShape.CIRCLE,
                                    width=20,
                                    height=20,
                                    border=ft.border.all(2, color='white'),
                                    alignment=ft.alignment.center
                                ),
                                ft.Text(value=f'Room {hs_room.room_number}', size=12, color='white'),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND
                        ),
                        width=120,
                        height=25,
                        bgcolor='#323232',
                        alignment=ft.alignment.center,
                    )
            )
            room_row[int(hs_room.room_number) - 1].controls.append(reservation_row[int(hs_room.room_number) - 1])
            table_lines[int(hs_room.room_number) - 1].controls.append(room_row[int(hs_room.room_number) - 1])
    for hs_room in hotel_rooms:
        if hs_room.room_type == '4yjezbow65i8fy6':
            room_row[int(hs_room.room_number) - 1].controls.append(
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Container(
                                content=ft.Text(value='F', color='white', font_family='Arial', size=10, weight=ft.FontWeight.BOLD),
                                shape=ft.BoxShape.CIRCLE,
                                width=20,
                                height=20,
                                border=ft.border.all(2, color='white'),
                                alignment=ft.alignment.center
                            ),
                            ft.Text(value=f'Room {hs_room.room_number}', size=12, color='white'),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    ),
                    width=120,
                    height=25,
                    bgcolor='#1A69E8',
                    alignment=ft.alignment.center
                )
            )
            room_row[int(hs_room.room_number) - 1].controls.append(reservation_row[int(hs_room.room_number) - 1])
            table_lines[int(hs_room.room_number) - 1].controls.append(room_row[int(hs_room.room_number) - 1])
    for hs_room in hotel_rooms:
        if hs_room.room_type == 'pfit5otmnsqxxoz':
            room_row[int(hs_room.room_number) - 1].controls.append(
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Container(
                                content=ft.Text(value='P', color='black', font_family='Arial', size=10, weight=ft.FontWeight.BOLD),
                                shape=ft.BoxShape.CIRCLE,
                                width=20,
                                height=20,
                                border=ft.border.all(2, color='black'),
                                alignment=ft.alignment.center
                            ),
                            ft.Text(value=f'Room {hs_room.room_number}', size=12, color='black'),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND
                    ),
                    width=120,
                    height=25,
                    bgcolor='#FFD700',
                    alignment=ft.alignment.center
                )
            )
            room_row[int(hs_room.room_number) - 1].controls.append(reservation_row[int(hs_room.room_number) - 1])
            table_lines[int(hs_room.room_number) - 1].controls.append(room_row[int(hs_room.room_number) - 1])

    # Function to handle the confirm button click event
    def confirm_edit(reservation_id, id_field,first_name,last_name,email,contact):
        pb.collection('reservation_list').update(id_field.value, {
            'last_name': last_name.value,
            'first_name': first_name.value,
            'contact_number': int(contact.value),
            'email': email.value,
        })
        show_reservations()
        updated_records()
    def checkOut(reservation_id, id_field, room_id):
        reservations = get_reservations()
        count = 0
        for r in reservations:
            if r.room == room_id.value:
                count = count + 1
        if count <= 1:
            pb.collection('rooms').update(f'{room_id.value}', {'status': True})
        count = 0
        pb.collection('reservation_list').delete(id_field.value)
        show_reservations()
        updated_records()
    def edit_field(reservation_id, container):
        container.visible = not container.visible
        rooms_display.update()
    def cancel_button_method(reservation_id, id_field,first_name,last_name,email,contact,room_id):
        reservations = get_reservations()
        count = 0
        for r in reservations:
            if r.room == room_id.value:
                count = count + 1
        if count <= 1:
            pb.collection('rooms').update(f'{room_id.value}', {'status': True})
        count = 0
        pb.collection('cancelled_reservation').create({
            'cancelled_date': f'{now}',
            'user': f'{userIDField.value}',
            'customer': f'{last_name.value}, {first_name.value}',
            'reservation_id': f'{id_field.value}',
            'email': f'{email.value}',
            'contact': f'{contact.value}'
        })
        pb.collection('reservation_list').delete(id_field.value)
        show_reservations()
        updated_records()
    def change_state(reservation_id, name_tag, color, id_field):
        name_tag.bgcolor = color.value
        if color.value == '#3EC7F1':
            pb.collection('reservation_list').update(id_field.value,{'state': 'Arrived'})
        elif color.value == '#D33434':
            pb.collection('reservation_list').update(id_field.value,{'state': 'Cancelled'})
        elif color.value == '#90C440':
            pb.collection('reservation_list').update(id_field.value,{'state': 'Confirmed'})
        rooms_display.update()
    def open_name_tag_buttons(reservation_id, name_tag_button, container):
        name_tag_button.visible = not name_tag_button.visible
        if name_tag_button.visible == False:
            container.visible = False
        rooms_display.update()
    def open_confirm_cancel(reservation_id, cancel_confirm):
        cancel_confirm.visible = not cancel_confirm.visible
        rooms_display.update()
    for res in reservations:
        for h in hotel_rooms:
            if res.room == h.id:
                if h.room_type == 'v54ixd0f7vlu3kq':
                    s_num += 1
                    standard_num.value = f'{s_num}'
                    standard_num.update()
                    number_for_standard.update()
                if h.room_type == '4yjezbow65i8fy6':
                        f_num += 1
                        family_num.value = f'{f_num}'
                        family_num.update()
                        number_for_family.update()
                if h.room_type == 'pfit5otmnsqxxoz':
                        p_num += 1
                        premium_num.value = f'{p_num}'
                        premium_num.update()
                        number_for_premium.update() 
    
    # we check if the collection of reservation is empty or not
    if len(reservations) != 0:
        for r_room in reservations:
            for i in hotel_rooms:
                name_tag=ft.Container
                if r_room.room == i.id:
                    roomType = ''
                    for e in list_of_types:
                        if e.id == i.room_type:
                            roomType = e.type
                    room_number = int(i.room_number)
                    if room_number not in room_count:
                        room_count[room_number] = 1
                    else:
                        room_count[room_number] += 1

                    num = room_count[room_number]

                    roomID = ft.Text(value=f'{r_room.room_id}', visible=False)
                    id_field = ft.TextField(value=f'{r_room.id}', visible=False)
                    first_name =  ft.TextField(value=f'{r_room.first_name}', width=125, height=30,bgcolor='white', color='black', text_size=12, max_lines=1,content_padding=2)
                    last_name =  ft.TextField(value=f'{r_room.last_name}', width=125, height=30,bgcolor='white', color='black', text_size=12, max_lines=1,content_padding=2)
                    email =  ft.TextField(value=f'{r_room.email}', width=125, height=30,bgcolor='white', color='black', text_size=12, max_lines=1,content_padding=2)
                    contact =  ft.TextField(value=f'{r_room.contact_number}', width=125, height=30,bgcolor='white', color='black', text_size=12, max_lines=1,content_padding=2)
                    confirm_button = ft.Container(
                        on_click=lambda reservation_id=r_room.id,id_field=id_field,first_name=first_name,last_name=last_name,email=email,contact=contact: confirm_edit(reservation_id,id_field,first_name,last_name,email,contact),
                        content=ft.Text(value='CONFIRM', size=15, color='white'),
                        width=100,
                        height=30,
                        border_radius=ft.border_radius.all(5),
                        alignment=ft.alignment.center,
                        bgcolor='#91C540',
                        tooltip='confirm edit'
                    )
                    cc = ft.Column([])
                    cancel_confirm = ft.Container(
                        content=cc,
                        bgcolor='white',
                        visible=False
                    )
                    cc.controls.append(ft.Row([ft.Text('Cancel this reservation?', color='red', weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.CENTER))
                    cc.controls.append(ft.Row([
                                ft.TextButton(text='Yes',on_click=lambda reservation_id=r_room.id,id_field=id_field,first_name=first_name,last_name=last_name,email=email,contact=contact, room_id=roomID: cancel_button_method(reservation_id, id_field,first_name,last_name,email,contact,room_id)),
                                ft.TextButton(text='No', on_click= lambda reservation_id=r_room.id, cancel_confirm=cancel_confirm:open_confirm_cancel(reservation_id, cancel_confirm))
                            ], alignment=ft.MainAxisAlignment.SPACE_AROUND))
                    cancel_button = ft.Container(
                        on_click= lambda reservation_id=r_room.id, cancel_confirm=cancel_confirm:open_confirm_cancel(reservation_id, cancel_confirm),
                        content=ft.Text(value='CANCEL', size=15, color='white'),
                        width=100,
                        height=30,
                        border_radius=ft.border_radius.all(5),
                        alignment=ft.alignment.center,
                        bgcolor='#E51568',
                        tooltip='cancel reservation'
                    )

                    container = ft.Container(
                        ft.Column(
                            [
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            # customer complete name
                                            ft.Row(
                                                [   
                                                
                                                    ft.Column(
                                                        [
                                                            ft.Text(value='First Name', size=12, color='white'),
                                                            first_name
                                                        ]
                                                    ),
                                                    ft.Column(
                                                        [
                                                            ft.Text(value='Last Name', size=12, color='white'),
                                                            last_name
                                                        ]
                                                    ),
                                                ],
                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY
                                            ),

                                            # customer email
                                            ft.Container(
                                                content=ft.Column(
                                                    [
                                                        ft.Text(value='Email', size=12, color='white'),
                                                        email
                                                    ]
                                                ),
                                                padding=ft.padding.only(left=22)
                                            ),

                                            # customers phone number
                                            ft.Container(
                                                content=ft.Column(
                                                    [
                                                        ft.Text(value='Phone Number', size=12, color='white'),
                                                        contact
                                                    ]
                                                ),
                                                padding=ft.padding.only(left=22)
                                            ),

                                            # check in date field
                                            ft.Container(
                                                content=ft.Column(
                                                    [
                                                        ft.Text(value='Check-In', size=12, color='white'),
                                                        ft.Text(value=f'{r_room.check_in}', size=12, color='red'),

                                                    ]
                                                ),
                                                padding=ft.padding.only(left=22)
                                            ),

                                            # check out date field
                                            ft.Container(
                                                content=ft.Column(
                                                    [
                                                        ft.Text(value='Check-Out', size=12, color='white'),
                                                        ft.Text(value=f'{r_room.check_out}', size=12, color='red'),

                                                    ]
                                                ),
                                                padding=ft.padding.only(left=22)
                                            ),

                                            ft.Row(
                                                [
                                                    ft.Column(
                                                        [
                                                            ft.Text(value='Room Type', size=12, color='white'),
                                                            ft.Text(value=f'{roomType}', size=12, color='red')
                                                        ]
                                                    ),
                                                    ft.Column(
                                                        [
                                                            ft.Text(value='Room Number', size=12, color='white'),
                                                            ft.Text(value=f'{i.room_number}', size=12, color='red')
                                                        ]
                                                    ),
                                                    ft.Column(
                                                        [
                                                            ft.Text(value='Number of Guest', size=12, color='white'),
                                                            ft.Text(value=f'{r_room.guest}', size=12, color='red')
                                                        ]
                                                    )
                                                ],
                                                alignment=ft.MainAxisAlignment.SPACE_AROUND
                                            ),
                                            #
                                            ft.Container(
                                                content=ft.Container(width=400, border=ft.border.all(2, color='white'),
                                                                    border_radius=ft.border_radius.all(50)),
                                                width=300,
                                                alignment=ft.alignment.center,
                                                padding=ft.padding.only(top=15)
                                            ),
                                            # confirm button and cancel
                                            cancel_confirm,
                                            ft.Container(
                                                content=ft.Row(
                                                    [
                                                        cancel_button,
                                                        confirm_button
                                                    ],
                                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY
                                                ),
                                                width=420,
                                                height=50,
                                                alignment=ft.alignment.center
                                            )
                                        ],
                                        scroll=ft.ScrollMode.AUTO
                                    ),
                                    width=300,
                                    height=400,
                                    alignment=ft.alignment.center
                                )
                            ]
                        ),
                        bgcolor='#474747',
                        visible=False
                    )

                    if r_room.id in reserved_containers:
                        # If it exists, append the container to the existing list
                        reserved_containers[r_room.id].append(container)
                    else:
                        # If it doesn't exist, create a new list with the container
                        reserved_containers[r_room.id] = [container]
                    if r_room.id in reserved_reservation_ids:
                        # If it exists, append the container to the existing list
                        reserved_reservation_ids[r_room.id].append(id_field)
                    else:
                        # If it doesn't exist, create a new list with the container
                        reserved_reservation_ids[r_room.id] = [id_field]
                    if r_room.id in cancel_confirmations:
                        cancel_confirmations[r_room.id].append(cancel_confirm)
                    else:
                        cancel_confirmations[r_room.id] = [cancel_confirm]
            
                    f_name[r_room.id]=(first_name)
                    l_name[r_room.id]=(last_name)
                    e_mail[r_room.id]=(email)
                    c_num[r_room.id]=(contact)
                    
                    edit_button = ft.Container(
                        content=ft.Icon(name=ft.icons.EDIT, size=20, color='#E51568', tooltip='edit data'),
                        on_click=lambda reservation_id=r_room.id, container=container: edit_field(reservation_id, container)
                    )

                    check_out_button = ft.Container(
                        content=ft.Icon(name=ft.icons.CHECK_BOX_ROUNDED, size=20, color='#79933A', tooltip='check out'),
                        on_click=lambda reservation_id=r_room.id, id_field=id_field, room_id=roomID: checkOut(reservation_id, id_field, room_id)
                    )

                    name_tag_button = ft.Container(visible=False)

                    name_tag_options = ft.Container(
                        content=ft.Icon(name=ft.icons.ARROW_DROP_DOWN, size=20, color='black', tooltip='change state'),
                        on_click= lambda reservation_id=r_room.id, name_tag_button=name_tag_button, container=container: open_name_tag_buttons(reservation_id, name_tag_button, container)
                    )

                    name_tag=ft.Container(
                        height=22,
                        width=300,
                        alignment=ft.alignment.center_left,
                        padding=ft.padding.only(left=5),
                        border=ft.border.only(
                            left=ft.BorderSide(5, color='black'),
                            top=ft.BorderSide(1, color='black'),
                            right=ft.BorderSide(1, color='black'),
                            bottom=ft.BorderSide(1, color='black')
                        ),
                        border_radius=ft.border_radius.all(4),
                        content=ft.Row(
                            [
                                ft.Row(
                                    [
                                        ft.Container(content=ft.Text(f'{num}', color='white', size=10), width=20,
                                                    height=20, bgcolor='#C84061', alignment=ft.alignment.center),
                                        ft.Text(value=f'{r_room.last_name}, {r_room.first_name}', size=12,
                                                color='black',
                                                weight=ft.FontWeight.BOLD),
                                    ]
                                ),
                                name_tag_options
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )
                    )
                    if r_room.state == 'New':
                        name_tag.bgcolor = '#FFA510'
                    elif r_room.state == 'Arrived':
                        name_tag.bgcolor = '#3EC7F1'
                    elif r_room.state == 'Cancelled':
                        name_tag.bgcolor = '#D33434'
                    elif r_room.state == 'Confirmed':
                        name_tag.bgcolor = '#90C440'
                    arrived_value = ft.Text(value='#3EC7F1', visible=False)
                    confirmed_value = ft.Text(value='#90C440', visible=False)
                    cancelled_value = ft.Text(value='#D33434', visible=False)
                    states = ft.Row([
                        ft.Container(
                            content=ft.Row(
                                [
                                    arrived_value,
                                    ft.Container(width=10, height=10, bgcolor='blue', border=ft.border.all(1, 'black')),
                                    ft.Text('Arrived', color='black', size=12)
                                ]
                            ),
                            tooltip='click to change color',
                            on_click= lambda reservation_id=r_room.id, name_tag=name_tag, color=arrived_value, id_field=id_field : change_state(reservation_id, name_tag, color, id_field)
                        ),
                        
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Container(width=10, height=10, bgcolor='green', border=ft.border.all(1, 'black')),
                                    ft.Text('Confirmed', color='black', size=12)
                                ]
                            ),
                            tooltip='click to change color',
                            on_click= lambda reservation_id=r_room.id, name_tag=name_tag, color=confirmed_value, id_field=id_field : change_state(reservation_id, name_tag, color, id_field)
                        ),

                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Container(width=10, height=10, bgcolor='red', border=ft.border.all(1, 'black')),
                                    ft.Text('Cancelled', color='black', size=12)
                                ]
                            ),
                            tooltip='click to change color',
                            on_click= lambda reservation_id=r_room.id, name_tag=name_tag, color=cancelled_value, id_field=id_field : change_state(reservation_id, name_tag, color, id_field)
                        )
                    ])

                    name_tag_button.content=(ft.Container(
                            content=ft.Row(
                                [
                                    states,
                                    edit_button,
                                    check_out_button,
                                ],
                                alignment=ft.MainAxisAlignment.END
                            ),
                            bgcolor='#F4F4F4',
                            width=300,
                            alignment=ft.alignment.center_right
                        )
                    )
                    if r_room.id in name_tag_buttons:
                        name_tag_buttons[r_room.id].append(name_tag_button)
                    else:
                        name_tag_buttons[r_room.id] = [name_tag_button]
                    if r_room.id in name_tags:
                        name_tags[r_room.id].append(name_tag)
                    else:
                        name_tags[r_room.id] = [name_tag]
                    reservation_row[room_number - 1].controls.append(
                        ft.Column(
                            [
                                name_tag,
                                name_tag_button,
                                container,
                                id_field
                            ]
                        )
                    ) 

    for roomm_row in table_lines:
        rooms_display.controls.append(roomm_row)
    

    rooms_display.update()

Time_container=ft.Text(value='',
        color='white',
        size=12,
        font_family='Arial'
)
def close_error(_):
    error_msg.visible = False
    room.visible = True
    room.update()
    error_msg.update()
def close_error_empty(_):
    error_emptyField_msg.visible = False
    error_emptyField_msg.update()
error_msg = ft.Container(
    content=ft.Column(
            [
               ft.Text(value='Room Already Booked that Day!', color='red', size=15, weight=ft.FontWeight.BOLD),
               ft.Container(
                   content=ft.Text('CONFIRM', size=12, color='black'),
                   border=ft.border.all(1, color='red'),
                   border_radius=ft.border_radius.all(3),
                   alignment=ft.alignment.center,
                   on_click=close_error,
                   bgcolor='white'
               )     
            ]
    ),
    width=200,
    height=100,
    bgcolor='#91C540',
    border=ft.border.all(1, color='black'),
    border_radius=ft.border_radius.all(3),
    alignment=ft.alignment.center,
    visible=False
)
error_emptyField_msg = ft.Container(
    content=ft.Column(
            [
               ft.Text(value='Please fill in all the Information needed', color='red', size=15, weight=ft.FontWeight.BOLD),
               ft.Container(
                   content=ft.Text('CONFIRM', size=12, color='black'),
                   border=ft.border.all(1, color='red'),
                   border_radius=ft.border_radius.all(3),
                   alignment=ft.alignment.center,
                   on_click=close_error_empty,
                   bgcolor='white'
               )     
            ]
    ),
    width=400,
    height=100,
    bgcolor='#91C540',
    border=ft.border.all(1, color='black'),
    border_radius=ft.border_radius.all(3),
    alignment=ft.alignment.center,
    visible=False
)
Date_Container=ft.Text(value='',
        color='white',
        size=12,
        font_family='Arial'
)
#function for dateime always running
def clock():
    while True:
        if run_clock == True:
            date_time = datetime.datetime.now().strftime("%A,%B-%d-%Y %H:%M:%S/%p")
            date,time1 = date_time.split()
            time2,time3 = time1.split('/')
            hour,minutes,seconds =  time2.split(':')

            if int(hour) > 12 and int(hour) < 24:
                    t = str(int(hour) - 12) + ':' + minutes + ':' + seconds + ' ' + time3
            else:
                    t = time2 + ' ' + time3
            time.sleep(1)
            Date_Container.value = f'{date}'
            Time_container.value = f'{t} '
            Time_container.update()
            Date_Container.update()
            if run_clock == False:
                break
#function for opening date picker container
def open_CheckIn_date_picker(_):
    if checkIn_date_picker.visible == False:
        checkIn_date_picker.visible = True
    else:
        checkIn_date_picker.visible = False
    checkIn_date_picker.update()
def open_CheckOut_date_picker(_):
    if checkOut_date_picker.visible == False:
        checkOut_date_picker.visible = True
    else:
        checkOut_date_picker.visible = False
    checkOut_date_picker.update()
#function for getting the values of months and days
#appending them to Date field
def get_check_in_date(_):
    check_in_date.value = f'{month_and_day.months.value} - {month_and_day.days.value} - {now.strftime("%Y")}'
    checkIn_date_picker.visible = False
    checkIn_date_picker.update()
    check_in_date.update()
def get_check_out_date(_):
    check_out_date.value = f'{month_and_day.months.value} - {month_and_day.days.value} - {now.strftime("%Y")}'
    checkOut_date_picker.visible = False
    checkOut_date_picker.update()
    check_out_date.update()

#this FUNCTION() will append all the data from 
#our reservation form to the pocket_base
#collection reservation_list
def refresh_data():
    global room_list
    global list_of_types
    #function for updating the data and files:
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

container_length = 0

def confirm_reservation(_):
    global check_out_value
    global check_in_value
    global reservations
    global container_length
    check_in = check_in_date.value.split(' - ')
    check_in_month = datetime.datetime.strptime(check_in[0], '%B').date()
    check_in_value = f'{int(check_in[2])}-{check_in_month.month:02d}-{int(check_in[1]):02d} 12:00:00.000Z'

    check_out = check_out_date.value.split(' - ')
    check_out_month = datetime.datetime.strptime(check_out[0], '%B').date()
    check_out_value = f'{int(check_out[2])}-{check_out_month.month:02d}-{int(check_out[1]):02d} 12:00:00.000Z'
    reservations = get_reservations()
    if (
        last_name_field.value == '' or
        first_name_field.value == '' or
        phone_number_field.value == '' or
        email_field.value == '' or
        guest.value == '' or
        check_in_date.value == '' or
        check_out_date.value == '' or
        room_numbers.value == '' or
        room_types.value == ''
    ):
        error_emptyField_msg.visible = True
        error_emptyField_msg.update()
    else:
        error_msg.visible = False  # Reset the error message visibility
        room.visible = True  # Reset the room visibility
        room.update()
        for reserved_room in reservations:
            for i in hotel_rooms:
                if reserved_room.room == i.id and i.status == False:
                    if reserved_room.check_in == check_in_value or reserved_room.check_out == check_out_value:
                        error_msg.visible = True
                        room.visible = False
                        room.update()
                        error_msg.update()
                        return  # Stop execution if error condition is met
        # If the loop completes without encountering an error condition, proceed with the reservation
        appending_to_reservations()
        open_success_msg()
        show_reservations()
        updated_records()
        
def appending_to_reservations():
    room_id = ''
    global check_out_value
    global check_in_value
    global reservations
    global customers
    for rlist in room_list:
        if int(room_numbers.value) == rlist.room_number:
            room_id = rlist.id

    try:
        pb.collection('rooms').update(f'{room_id}', {'status': False})
        pb.collection('reservation_list').create({
            'user': f'{userIDField.value}',
            'last_name': last_name_field.value,
            'first_name': first_name_field.value,
            'contact_number': int(phone_number_field.value),
            'email': email_field.value,
            'guest': int(guest.value),
            'check_in': check_in_value,
            'check_out': check_out_value,
            'room_id': room_id,
            'state': 'New',
            'room': room_id
        })

        pb.collection('customers').create({
            'last_name': last_name_field.value,
            'first_name': first_name_field.value,
            'email': email_field.value,
            'contact': phone_number_field.value,
            'check_in': check_in_value,
            'check_out': check_out_value,
            'room': room_id
        })
        last_name_field.value = ''
        first_name_field.value = ''
        phone_number_field.value = ''
        email_field.value = ''
        guest.value = ''
        check_in_date.value = ''
        check_out_date.value = ''
        room_id = ''
        room_numbers.value = ''
        room_types.value = ''
        last_name_field.update()
        first_name_field.update()
        phone_number_field.update()
        email_field.update()
        guest.update()
        check_in_date.update()
        check_out_date.update()
        room_numbers.update()
        room_types.update()
        rooms_display.update()
        refresh_data()

    except pocketbase.utils.ClientResponseError as e:
        # Handle the error here
        print(f"An error occurred during reservation: {e}")
        
def cancel_reservation(_):
    last_name_field.value = ''
    first_name_field.value = ''
    phone_number_field.value = ''
    email_field.value = ''
    guest.value = ''
    check_in_date.value = ''
    check_out_date.value = ''
    room_numbers.value = ''
    room_types.value = ''
    last_name_field.update()
    first_name_field.update()
    phone_number_field.update()
    email_field.update()
    guest.update()
    check_in_date.update()
    check_out_date.update()
    room_numbers.update()
    room_types.update()
    reservation_form.visible = False
    reservation_form.update()
#all reservation details text field variables
first_name_field = ft.TextField(width=180, height=30, bgcolor='white', color='black', text_size=12, max_lines=1, content_padding=2)
last_name_field = ft.TextField(width=180, height=30, bgcolor='white', color='black', text_size=12, max_lines=1, content_padding=2)
email_field = ft.TextField(width=385, height=30, bgcolor='white', color='black', text_size=12, max_lines=1, content_padding=2)
phone_number_field = ft.TextField(width=300, height=30, bgcolor='white', color='black', text_size=12, max_lines=1, content_padding=2)
checkIn_date_picker = ft.Container(content=ft.Row([month_and_day, ft.TextButton(content=ft.Text(value='OK', color='black', size=14), on_click=get_check_in_date)]),
                           width=300, height=50,
                           alignment=ft.alignment.center,
                           bgcolor='#91C540', padding=ft.padding.only(left=5),
                           visible=False, border=ft.border.all(1, color='black'),
                           border_radius=ft.border_radius.all(5))
checkOut_date_picker = ft.Container(content=ft.Row([month_and_day, ft.TextButton(content=ft.Text(value='OK', color='black', size=14), on_click=get_check_out_date)]),
                           width=300, height=50,
                           alignment=ft.alignment.center,
                           bgcolor='#91C540', padding=ft.padding.only(left=5),
                           visible=False, border=ft.border.all(1, color='black'),
                           border_radius=ft.border_radius.all(5))
check_in_date = ft.Text(value='', color='black', size=12)
check_out_date = ft.Text(value='', color='black', size=12)
check_in_date_field = ft.Container(width=200, height=30, border=ft.border.all(1, color='black'), border_radius=ft.border_radius.all(5), bgcolor='white',
                                   content=ft.Row(
                                        [
                                             check_in_date,
                                             ft.IconButton(icon=ft.icons.CALENDAR_MONTH_OUTLINED, icon_size=12, icon_color='#91C540', tooltip='date picker', on_click=open_CheckIn_date_picker)
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                   ),
                                   padding=ft.padding.only(left=10),
                                   alignment=ft.alignment.center
                                   )

check_out_date_field = ft.Container(width=200, height=30, border=ft.border.all(1, color='black'), border_radius=ft.border_radius.all(5), bgcolor='white',
                                   content=ft.Row(
                                        [
                                             check_out_date,
                                             ft.IconButton(icon=ft.icons.CALENDAR_MONTH_OUTLINED, icon_size=12, icon_color='#91C540', tooltip='date picker', on_click=open_CheckOut_date_picker)
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                   ),
                                   padding=ft.padding.only(left=10),
                                   alignment=ft.alignment.center
                                   )

#container or alert dialog for adding reservations
reservation_form = ft.Container(
content=ft.Column(
    [
            ft.Container(
                content=ft.Text(value='Reservation Details', color='white', size=20, weight=ft.FontWeight.BOLD),
                width=430,
                height=50,
                bgcolor='#3D5D52',
                padding=ft.padding.only(left=10, top=10)
            ),

            ft.Container(
                content=ft.Column(
                    [
                        #customer complete name
                        ft.Row(
                            [
                                    ft.Column(
                                        [
                                            ft.Text(value='First Name', size=12, color='white'),
                                            first_name_field,
                                        ]
                                    ),
                                    ft.Column(
                                        [
                                            ft.Text(value='Last Name', size=12, color='white'),
                                            last_name_field,
                                        ]
                                    ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY
                        ),

                        #customer email
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text(value='Email', size=12, color='white'),
                                    email_field
                                ]
                            ),
                            padding=ft.padding.only(left=22)
                        ),

                        #customers phone number
                        ft.Container(
                                content=ft.Column(
                                [
                                    ft.Text(value='Phone Number', size=12, color='white'),
                                    phone_number_field
                                ]
                            ),
                            padding=ft.padding.only(left=22)
                        ),

                        #check in date field
                        ft.Container(
                                content=ft.Column(
                                [
                                    ft.Text(value='Check-In', size=12, color='white'),
                                    check_in_date_field
                                ]
                            ),
                            padding=ft.padding.only(left=22)
                        ),
                        ft.Container(content=checkIn_date_picker, padding=ft.padding.only(left=22)),

                        #check out date field
                        ft.Container(
                                content=ft.Column(
                                [
                                    ft.Text(value='Check-Out', size=12, color='white'),
                                    check_out_date_field
                                ]
                            ),
                            padding=ft.padding.only(left=22)
                        ),
                        ft.Container(content=checkOut_date_picker, padding=ft.padding.only(left=22)),

                        ft.Container(content=error_msg, padding=ft.padding.only(left=22)),
                        ft.Container(content=error_emptyField_msg, padding=ft.padding.only(left=22)),
                        #drop down menu for room type and room number
                        room,
                        
                        #
                        ft.Container(
                            content=ft.Container(width=400, border=ft.border.all(2, color='white'), border_radius=ft.border_radius.all(50)),
                            width=430,
                            alignment=ft.alignment.center,
                            padding=ft.padding.only(top=15)
                        ),
                        #confirm button and cancel
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Container(
                                        on_click=cancel_reservation,
                                        content=ft.Text(value='CANCEL', size=15, color='white'),
                                        width=100,
                                        height=30,
                                        border_radius=ft.border_radius.all(5),
                                        alignment=ft.alignment.center,
                                        border=ft.border.all(3, color='white')
                                    ),

                                    ft.Container(
                                        on_click=confirm_reservation,
                                        content=ft.Text(value='CONFIRM', size=15, color='white'),
                                        width=100,
                                        height=30,
                                        border_radius=ft.border_radius.all(5),
                                        alignment=ft.alignment.center,
                                        bgcolor='#91C540'
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY
                            ),
                            width=420,
                            height=100,
                            alignment=ft.alignment.center
                        )
                    ],
                    scroll=ft.ScrollMode.AUTO 
                ),
                width=430,
                height=520,
                alignment=ft.alignment.center
            )
    ]
),
width=430,
height=600,
bgcolor='#474747',
visible=False
)

#function for opening reservation dialog
def open_reservation_form(_):
    success_mesg.visible = False
    success_mesg.update()
    if reservation_form.visible == True:
        reservation_form.visible = False
    else:
        reservation_form.visible = True
    reservation_form.update()

def open_calendar(_):
    all_reservation_cont.visible = not all_reservation_cont.visible
    all_reservation_cont.update()

def open_success_msg():
    success_mesg.visible = True
    success_mesg.update()
def close_success_msg(_):
    success_mesg.visible = False
    success_mesg.update()

#list of listview
standard_listView = ft.ListView()
family_listView = ft.ListView()
premium_listView = ft.ListView()

#list of container inside the view
standard_list_container = ft.Container(content=standard_listView, width=1138, height=925)
family_list_container = ft.Container(content=family_listView, width=1138, height=925)
premium_list_container = ft.Container(content=premium_listView, width=1138, height=925)

standard_num = ft.Text(value=f'{s_num}', color='white', size=10)
family_num = ft.Text(value=f'{s_num}', color='white', size=10)
premium_num = ft.Text(value=f'{s_num}', color='white', size=10)
    

# numbers of reservation per type
number_for_standard = ft.Container(
    content=standard_num,
    width=15,
    height=15,
    bgcolor='red',
    shape=ft.BoxShape.CIRCLE,
    alignment=ft.alignment.center
)
number_for_family = ft.Container(
    content=family_num,
    width=15,
    height=15,
    bgcolor='red',
    shape=ft.BoxShape.CIRCLE,
    alignment=ft.alignment.center
)
number_for_premium = ft.Container(
    content=premium_num,
    width=15,
    height=15,
    bgcolor='red',
    shape=ft.BoxShape.CIRCLE,
    alignment=ft.alignment.center
)

success_mesg = ft.Container(
        content=ft.Column(
            [   
                ft.Row([ft.Container(content=ft.Icon(name=ft.icons.HIGHLIGHT_REMOVE_ROUNDED, size=50, color='#E51568'), on_click=close_success_msg)], alignment=ft.MainAxisAlignment.END),
                ft.Row([ft.Icon(name=ft.icons.CHECK_CIRCLE_OUTLINE_ROUNDED, color='#87D185', size=350)],alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([ft.Text('Success!', color='#262C57', size=50, weight=ft.FontWeight.BOLD)],alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([ft.Text('New reservation has been added.', color='#262C57', size=25)], alignment=ft.MainAxisAlignment.CENTER)
            ]
        ),
        width=700,
        height=600,
        bgcolor='white',
        border_radius=ft.border_radius.all(5),
        border=ft.border.all(2, 'black'),
        alignment=ft.alignment.center,
        visible=False
    )
    
class view_reservation_container(ft.UserControl):
    def build(self):
        return ft.Container(
            content=ft.Container(
                content=ft.Column(
                    [
                         #header
                        ft.Row(
                            [
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Container(
                                                content=ft.Column(
                                                    [
                                                        Time_container,
                                                        Date_Container
                                                    ]
                                                ),
                                                padding=ft.padding.only(left=5, top=10),
                                                border=ft.border.only(left=ft.BorderSide(2, color='white'))
                                            ),

                                            #room type buttons
                                            ft.Row(
                                                [
                                                    #room type buttons
                                                    ft.Container(
                                                        ft.Row(
                                                            [
                                                                ft.Container(
                                                                    content=ft.Row(
                                                                        [
                                                                            ft.Container(
                                                                                content=ft.Text(value='S', color='white', font_family='Arial', size=10, weight=ft.FontWeight.BOLD),
                                                                                shape=ft.BoxShape.CIRCLE,
                                                                                width=20,
                                                                                height=20,
                                                                                border=ft.border.all(2, color='white'),
                                                                                alignment=ft.alignment.center
                                                                            ),
                                                                            ft.Text(value='STANDARD', color='white', font_family='Arial', size=10),
                                                                            number_for_standard
                                                                        ],
                                                                        alignment=ft.MainAxisAlignment.CENTER
                                                                    ),
                                                                    border_radius=ft.border_radius.all(5),
                                                                    bgcolor='#323232',
                                                                    padding=ft.padding.all(5)
                                                                ),
                                                                ft.Container(
                                                                    content=ft.Row(
                                                                        [
                                                                            ft.Container(
                                                                                content=ft.Text(value='F', color='white', font_family='Arial', size=10, weight=ft.FontWeight.BOLD),
                                                                                shape=ft.BoxShape.CIRCLE,
                                                                                width=20,
                                                                                height=20,
                                                                                border=ft.border.all(2, color='white'),
                                                                                alignment=ft.alignment.center
                                                                            ),
                                                                            ft.Text(value='FAMILY', color='white', font_family='Arial', size=10),
                                                                            number_for_family
                                                                        ],
                                                                        alignment=ft.MainAxisAlignment.CENTER
                                                                    ),
                                                                    border_radius=ft.border_radius.all(5),
                                                                    bgcolor='#1A69E8',
                                                                    padding=ft.padding.all(5)
                                                                ),
                                                                ft.Container(
                                                                    content=ft.Row(
                                                                        [
                                                                            ft.Container(
                                                                                content=ft.Text(value='P', color='black', font_family='Arial', size=10, weight=ft.FontWeight.BOLD),
                                                                                shape=ft.BoxShape.CIRCLE,
                                                                                width=20,
                                                                                height=20,
                                                                                border=ft.border.all(2, color='black'),
                                                                                alignment=ft.alignment.center
                                                                            ),
                                                                            ft.Text(value='PREMIUM', color='black', font_family='Arial', size=10),
                                                                            number_for_premium
                                                                        ],
                                                                        alignment=ft.MainAxisAlignment.CENTER
                                                                    ),
                                                                    border_radius=ft.border_radius.all(5),
                                                                    bgcolor='#FFD700',
                                                                    padding=ft.padding.all(5)
                                                                ),
                                                            ]
                                                        )
                                                    )

                                                ]
                                            )
                                        ]
                                    ),
                                    width=400,
                                    height=90
                                ),

                                #labels
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Row([
                                                ft.Container(
                                                    content=ft.Row(
                                                        [
                                                            ft.Container(width=10, height=10, bgcolor='orange', border=ft.border.all(1, 'black')),
                                                            ft.Text('New Reservation', color='white', size=15, weight=ft.FontWeight.BOLD)
                                                        ]
                                                    ),
                                                    
                                                ),

                                                ft.Container(
                                                    content=ft.Row(
                                                        [
                                                            ft.Container(width=10, height=10, bgcolor='blue', border=ft.border.all(1, 'black')),
                                                            ft.Text('Arrived', color='white', size=15, weight=ft.FontWeight.BOLD)
                                                        ]
                                                    ),
                                                    
                                                ),
                                            ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                                            
                                            ft.Row([
                                                ft.Container(
                                                    content=ft.Row(
                                                        [
                                                            ft.Container(width=10, height=10, bgcolor='green', border=ft.border.all(1, 'black')),
                                                            ft.Text('Confirmed', color='white', size=15, weight=ft.FontWeight.BOLD)
                                                        ]
                                                    ),
                                                
                                                ),

                                                ft.Container(
                                                    content=ft.Row(
                                                        [
                                                            ft.Container(width=10, height=10, bgcolor='red', border=ft.border.all(1, 'black')),
                                                            ft.Text('Cancelled', color='white', size=15, weight=ft.FontWeight.BOLD)
                                                        ]
                                                    ),
                                                
                                                )
                                            ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                                            
                                        ]
                                    ),
                                    alignment=ft.alignment.center,
                                    width=250
                                ),
                                
                                #reservation buttons
                                ft.Container(
                                    content=ft.Row(
                                        [
                                             ft.Container(
                                                content=ft.Row(
                                                    [
                                                    ft.Icon(name=ft.icons.TABLE_ROWS_ROUNDED, color='white', size=30,),
                                                    ft.Text(value='ALL RESERVATION', size=18, color='white', weight=ft.FontWeight.BOLD)
                                                    ],
                                                    alignment=ft.MainAxisAlignment.CENTER
                                                ),
                                                width=225,
                                                height=50,
                                                border=ft.border.all(4, color='white'),
                                                border_radius=ft.border_radius.all(5),
                                                alignment=ft.alignment.center,
                                                padding=ft.padding.all(5),
                                                on_click=open_calendar
                                             ),
                                             ft.Container(
                                                content=ft.Row(
                                                    [
                                                    ft.Icon(name=ft.icons.ADD_CIRCLE_OUTLINE, color='#FFFFFF', size=30,),
                                                    ft.Text(value='ADD RESERVATION', size=18, color='#FFFFFF', weight=ft.FontWeight.BOLD)
                                                    ],
                                                    alignment=ft.MainAxisAlignment.CENTER
                                                ),
                                                width=220,
                                                height=50,
                                                bgcolor='#3D5D52',
                                                border_radius=ft.border_radius.all(5),
                                                alignment=ft.alignment.center,
                                                padding=ft.padding.all(5),
                                                on_click=open_reservation_form
                                             )
                                        ],
                                        alignment=ft.MainAxisAlignment.START
                                    ),
                                    width=500,
                                    height=90,
                                    alignment=ft.alignment.center_right,
                                    padding=ft.padding.only(left=20),
                                )
                            ]
                        ),
                        #end of header!!

                        #body-list view
                        #list of list or containers
                        #----
                        #reservation container or form set visible to False
                        #True when function click (open_reservation(_))
                        ft.Stack([
                            ft.Row([all_reservation_cont], width=1138,),
                            ft.Row(
                                [
                                    success_mesg,
                                    reservation_form,
                                ],
                                width=1138,
                                alignment=ft.MainAxisAlignment.END,
                                spacing=5
                            ),
                        ]),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Column(
                                        [
                                            ft.Container(
                                                content=ft.Row([
                                                    ft.Container(content=ft.Text('LIST OF ROOMS', color='white', size=12, weight=ft.FontWeight.BOLD),
                                                                 width=120, height=25, alignment=ft.alignment.center,
                                                                 border=ft.border.only(right=ft.BorderSide(2, color='black'))),
                                                    ft.Container(content=ft.Text('RESERVATION LIST', color='white', size=12, weight=ft.FontWeight.BOLD), width=1018, height=25, alignment=ft.alignment.center)
                                                    
                                                ]),
                                                width=1138,
                                                height=25,
                                                bgcolor='#D79551'
                                            ),
                                            rooms_display
                                        ]
                                    )
                                ],
                                scroll=ft.ScrollMode.ALWAYS,
                                auto_scroll = True
                            ),
                            width=1138,
                            height=780,
                            bgcolor='#EEECE1',
                            border=ft.border.all(4, color='white'),
                            border_radius=ft.border_radius.all(3)
                        )

                    ],
                    scroll=ft.ScrollMode.ALWAYS
                ),
            ),
            width=1138,
            height=850,
            alignment=ft.alignment.top_center,
        )