import flet as ft
from model.Host import HOST
from model.room_images import room_images
from controller.room_type_image_controller import get_Proom_images
from controller.room_type_controller import get_room_types


proom_Images: list[room_images] = get_Proom_images()
types = get_room_types()
price = 0
Room_Type = ''
room_status:list=[]
room_gallery: list = []
counter:list=[]
index = 0
image_num = 0


for i in proom_Images:
    room_gallery.append(f'{HOST}api/files/obbhx5i2333jgko/{proom_Images[index].id}/{proom_Images[index].room_image}?token=')
    index += 1
for e in types:
    if e.type == 'Premium':
        price = e.price
        Room_Type = e.type

gallery = ft.Image(src=f'{room_gallery[image_num]}', fit=ft.ImageFit.COVER)
small_image_gallery = ft.Row([])
premium_rooms_list = ft.Row([], wrap=True, alignment=ft.MainAxisAlignment.SPACE_EVENLY)
available_room_label = ft.Text(value='', size=10, color='#525252')

def append_Proom_to_row(l):
    Proom_list = l
    counter.clear()
    room_status.clear()
    premium_rooms_list.controls.clear()
    for proom in Proom_list:
        if proom.status == False and proom.room_type == 'pfit5otmnsqxxoz':
            premium_rooms_list.controls.append(
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text(value=f'Room {proom.room_number}', color='black'),
                                    ft.Container(
                                        content=ft.Text(value='P', color='white', font_family='Arial', size=12, weight=ft.FontWeight.BOLD),
                                        shape=ft.BoxShape.CIRCLE,
                                        width=20,
                                        height=20,
                                        bgcolor='#FFD700',
                                        alignment=ft.alignment.center,
                                        padding=ft.padding.all(2)

                                    )
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                            ),
                            ft.Container(
                                content=ft.Text(value='Reserved', color='white', size=10),
                                border_radius=ft.border_radius.all(50),
                                padding=ft.padding.only(left=3, right=3),
                                bgcolor='purple'
                            ),
                            ft.Container(
                                content= ft.Text(value=f'{Room_Type} - {price}', color='#FFFFFF', size=12),
                                bgcolor='#FFA510',
                                border_radius=ft.border_radius.all(50),
                                padding=ft.padding.only(left=5, right=5)
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    width=250,
                    height=120,
                    border=ft.border.only(left=ft.border.BorderSide(3, color='#FFD700'),
                                            right=ft.border.BorderSide(1, color='#F4F4F4'),
                                            top=ft.border.BorderSide(1, color='#F4F4F4'),
                                            bottom=ft.border.BorderSide(1, color='#F4F4F4')
                                            ),
                    border_radius=ft.border_radius.all(5),
                    padding=ft.padding.all(5)
                )
            )
            counter.append(proom.room_type)

        elif proom.status == True and proom.room_type == 'pfit5otmnsqxxoz':
            premium_rooms_list.controls.append(
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text(value=f'Room {proom.room_number}', color='black'),
                                    ft.Container(
                                        content=ft.Text(value='P', color='white', font_family='Arial', size=12, weight=ft.FontWeight.BOLD),
                                        shape=ft.BoxShape.CIRCLE,
                                        width=20,
                                        height=20,
                                        bgcolor='#FFD700',
                                        alignment=ft.alignment.center,
                                        padding=ft.padding.all(2)

                                    )
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                            ),
                            ft.Container(
                                content=ft.Text(value='Available', color='white', size=10),
                                border_radius=ft.border_radius.all(50),
                                padding=ft.padding.only(left=3, right=3),
                                bgcolor='green'
                            ),
                            ft.Container(
                                content= ft.Text(value=f'{Room_Type} - {price}', color='#FFFFFF', size=12),
                                bgcolor='#FFA510',
                                border_radius=ft.border_radius.all(50),
                                padding=ft.padding.only(left=5, right=5)
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    width=250,
                    height=120,
                    border=ft.border.only(left=ft.border.BorderSide(3, color='#FFD700'),
                                            right=ft.border.BorderSide(1, color='#F4F4F4'),
                                            top=ft.border.BorderSide(1, color='#F4F4F4'),
                                            bottom=ft.border.BorderSide(1, color='#F4F4F4')
                                            ),
                    border_radius=ft.border_radius.all(5),
                    padding=ft.padding.all(5)
                )
            )
            counter.append(proom.room_type)
            room_status.append(proom.status)
        
    available_room_label.value = f'Available {len(room_status)}/{len(counter)}'
    available_room_label.update()
    premium_rooms_list.update()

def append_premium_images():
    small_image_gallery.controls.clear()
    for e in room_gallery:
        small_image_gallery.controls.append(
            ft.Container(
            content=ft.Image(src=e, fit=ft.ImageFit.COVER),
            width=200,
            height=150,
            )
        )
    small_image_gallery.update()

d_text = ft.Text('ROOM DESCRIPTION', color='white')
p_text = ft.Text('ROOM POLICIES', color='#000000')
o_text = ft.Text('ROOM SPECIAL OFFERS', color='#000000')

def room_description_clicked(_):
    d_container.visible = True
    p_container.visible = False
    o_container.visible = False
    room_description.bgcolor = '#FFA510'
    room_offers.bgcolor = 'white'
    room_policies.bgcolor = 'white'
    d_text.color = 'white'
    p_text.color = '#000000'
    o_text.color = '#000000'

    d_text.update()
    p_text.update()
    o_text.update()
    room_offers.update()
    room_policies.update()
    room_description.update()
    d_container.update()
    p_container.update()
    o_container.update()

def room_policies_clicked(_):
    d_container.visible = False
    p_container.visible = True
    o_container.visible = False
    room_description.bgcolor = 'white'
    room_offers.bgcolor = 'white'
    room_policies.bgcolor = '#FFA510'
    d_text.color = '#000000'
    p_text.color = 'white'
    o_text.color = '#000000'

    d_text.update()
    p_text.update()
    o_text.update()
    room_offers.update()
    room_policies.update()
    room_description.update()
    d_container.update()
    p_container.update()
    o_container.update()

def room_offers_clicked(_):
    d_container.visible = False
    p_container.visible = False
    o_container.visible = True
    room_description.bgcolor = 'white'
    room_offers.bgcolor = '#FFA510'
    room_policies.bgcolor = 'white'
    d_text.color = '#000000'
    p_text.color = '#000000'
    o_text.color = 'white'

    d_text.update()
    p_text.update()
    o_text.update()
    room_offers.update()
    room_policies.update()
    room_description.update()
    d_container.update()
    p_container.update()
    o_container.update()
    


room_description = ft.Container(
    on_click=room_description_clicked,
    content=d_text,
    width=200,
    height=40,
    bgcolor='#FFA510',
    border=ft.border.all(1, color='#F4F4F4'),
    alignment=ft.alignment.center
)

room_policies = ft.Container(
    on_click=room_policies_clicked,
    content=p_text,
    width=200,
    height=40,
    bgcolor='white',
    border=ft.border.all(1, color='#F4F4F4'),
    alignment=ft.alignment.center
)

room_offers = ft.Container(
    on_click=room_offers_clicked,
    content=o_text,
    width=200,
    height=40,
    bgcolor='white',
    border=ft.border.all(1, color='#F4F4F4'),
    alignment=ft.alignment.center
)

description_text = """
    The Premium Room comprises of a Queen Size Bed, 2 Bedside Tables, a Desk & Chair.
    This room is furnished with wall to wall carpeting, trendy furnishings and a large private
    Patio equipped with Patio Furniture and Sun Beds and offers a side sea view. Our ultramodern
    glass bathroom is equipped with hairdryer, magnifying shaving and make up mirror as well as
    all the amenities you could possible need during your stay. A Complimentary Bottle of Wine,
    Fresh Fruit and Mineral Water, are provided on arrival. Electric current: 220 Volts.
    Smoking rooms are also available.
"""

policies = """
    MEALS
    Breakfast is included in the room rate
    CANCELLATION
    If cancelled 48 hours before date of arrival, no fee will be charged.
    If cancelled later the equivalent of 1 night’s stay will be charged. In case of no-show, the total price of the reservation
    will be charged.
    PREPAYMENT
    No deposit will be charged, however in order to validate your Credit Card, the amount equivalent to 1 Night Stay
    will be blocked in your account for approximately 1 week.
"""

offers_text = """
    We are sorry, no offers are available at the moment.
"""

d_container = ft.Container(
    content=ft.Text(value=description_text, color='#727272', size=12),
    width=700,
    border=ft.border.only(left=ft.border.BorderSide(5, color='#FFA510')),
    padding=ft.padding.all(5),
    visible=True
)

p_container = ft.Container(
    content=ft.Text(value=policies, color='#727272', size=12),
    width=700,
    border=ft.border.only(left=ft.border.BorderSide(5, color='#FFA510')),
    padding=ft.padding.all(5),
    visible=False
)

o_container = ft.Container(
    content=ft.Text(value=offers_text, color='#727272', size=12),
    width=700,
    border=ft.border.only(left=ft.border.BorderSide(5, color='#FFA510')),
    padding=ft.padding.all(5),
    visible=False
)

class premium_room_view(ft.UserControl):
    def build(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Container(
                        content=ft.Text(value='Premium-Room Gallery', color='black',font_family='Consolas', size=30),
                        width=908,
                        height=70,
                        bgcolor="#F4F4F4",
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        #container of the images
                        content=ft.Container(
                            content=gallery,
                            width=880,
                            height=420,
                        ),
                    width=908,
                    height=420,
                    alignment=ft.alignment.center
                    ),
                    ft.Container(
                        #container for small images
                        content=ft.Container(
                            content=small_image_gallery,
                            width=880,
                            height=150,
                        ),
                        width=908,
                        height=150,
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Container(
                                    content=ft.Text(value='PREMIUM ROOM AMENITIES', color='black',font_family='Consolas', size=20),
                                    alignment=ft.alignment.center,
                                    bgcolor='#F4F4F4'
                                ),
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.Container(
                                                content=ft.Column(
                                                    [
                                                        ft.Row([ft.Icon(name=ft.icons.BED, color='#FFA510'),ft.Text(value='1 Double or 2 Single Beds', color='black')]),
                                                        ft.Row([ft.Icon(name=ft.icons.TV, color='#FFA510'),ft.Text(value='Flat Screen TV', color='black')]),
                                                        ft.Row([ft.Icon(name=ft.icons.PHONE, color='#FFA510'),ft.Text(value='Telephone', color='black')]),
                                                        ft.Row([ft.Icon(name=ft.icons.NETWORK_WIFI, color='#FFA510'),ft.Text(value='Wifi and Internet Access', color='black')])
                                                    ]
                                                ),
                                                alignment=ft.alignment.center,
                                                padding=ft.padding.only(left=20)
                                            ),

                                            ft.Container(
                                                content=ft.Column(
                                                    [
                                                        ft.Row([ft.Icon(name=ft.icons.AC_UNIT, color='#FFA510'),ft.Text(value='Individually Controlled A/C', color='black')]),
                                                        ft.Row([ft.Icon(name=ft.icons.ALL_INBOX, color='#FFA510'),ft.Text(value='Electronic Safe Deposit Box', color='black')]),
                                                        ft.Row([ft.Icon(name=ft.icons.LOCK_OUTLINE, color='#FFA510'),ft.Text(value='Electronic Lock Key System', color='black')]),
                                                        ft.Row([ft.Icon(name=ft.icons.LOCAL_CAFE_SHARP, color='#FFA510'),ft.Text(value='Mini Bar', color='black')])
                                                    ]
                                                ),
                                                alignment=ft.alignment.center,
                                                padding=ft.padding.only(left=20)
                                            ),

                                            ft.Container(
                                                content=ft.Column(
                                                    [
                                                        ft.Row([ft.Icon(name=ft.icons.COFFEE, color='#FFA510'),ft.Text(value='Tea & Coffee Facilities', color='black')]),
                                                        ft.Row([ft.Icon(name=ft.icons.BALCONY_SHARP, color='#FFA510'),ft.Text(value='Balcony', color='black')]),
                                                    ]
                                                ),
                                                alignment=ft.alignment.top_center,
                                                padding=ft.padding.only(left=20)
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_AROUND
                                    ),
                                    alignment=ft.alignment.center,
                                    width=880
                                ),

                                ft.Container(
                                    content=ft.Row(
                                        [
                                            room_description,
                                            room_policies,
                                            room_offers
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER
                                    ),
                                    width=880,
                                    height=80,
                                    alignment=ft.alignment.center
                                ),

                                ft.Container(
                                    content=ft.Stack(
                                        [
                                            d_container,
                                            p_container,
                                            o_container
                                        ]
                                    ),
                                    width=880,
                                    height = 200,
                                    alignment=ft.alignment.center
                                ),

                                ft.Container(
                                    content=ft.Container(width=800, border=ft.border.all(2, color='#525252'), border_radius=ft.border_radius.all(50)),
                                    alignment=ft.alignment.center
                                ),

                                ft.Container(
                                    content=ft.Container(
                                        content=available_room_label,
                                        width=800
                                    ),
                                    alignment=ft.alignment.center,
                                    width=908
                                ),

                                ft.Container(
                                    content=ft.Container(
                                        content=premium_rooms_list,
                                        width=800
                                    ),
                                    width=908,
                                    padding=ft.padding.all(10),
                                    alignment=ft.alignment.center
                                ),

                                ft.Container(
                                    width=908,
                                    height=50,
                                    bgcolor='#525252',
                                    border_radius=ft.border_radius.only(topLeft=5, topRight=5)
                                )
                                
                            ]
                        ),
                        width=908,
                        alignment=ft.alignment.center
                    )
                ],
                scroll=ft.ScrollMode.ALWAYS
            ),
            width=908,
            height=730,
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(5)
        )