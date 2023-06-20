import flet as ft
from model.room_images import room_images
from controller.room_image_controller import get_room_images
from model.Host import HOST
from view.components.standard_room_view import standard_room_view
from view.components.family_room_view import family_room_view
from view.components.premium_room_view import premium_room_view
from threading import Timer

images_of_room: list[room_images] = []
images_of_room = get_room_images()
image_room_sources: list = []
classification: list = []
counter = 0

standard = standard_room_view()
family = family_room_view()
premium = premium_room_view()

index = 0
for i in images_of_room:
    image_room_sources.append(f'{HOST}api/files/obbhx5i2333jgko/{images_of_room[index].id}/{images_of_room[index].room_image}?token=')
    classification.append(images_of_room[index].classification)
    index += 1

image_container = ft.Image(src=f'{image_room_sources[counter]}', fit=ft.ImageFit.COVER, border_radius=ft.border_radius.all(5), width=395)
image_container_label = ft.Text(value=f'{classification[counter]}', font_family='Arial', weight=ft.FontWeight.BOLD, color="white", size=15)

#types of room container:
standard_page=ft.Container(
    content=standard,
    width=908,
    height=871,
    bgcolor="white",
    border_radius=ft.border_radius.all(5),
    visible=True
)

family_page=ft.Container(
    content=family,
    width=908,
    height=871,
    bgcolor="white",
    border_radius=ft.border_radius.all(5),
    visible=False
)

premium_page=ft.Container(
    content=premium,
    width=908,
    height=871,
    bgcolor="white",
    border_radius=ft.border_radius.all(5),
    visible=False
)

def open_standard_page(_):
    standard_page.visible = True
    family_page.visible = False
    premium_page.visible = False

    premium_page.update()
    standard_page.update()
    family_page.update()

def open_premium_page(_):
    standard_page.visible = False
    family_page.visible = False
    premium_page.visible = True

    premium_page.update()
    standard_page.update()
    family_page.update()

def open_family_page(_):
    standard_page.visible = False
    family_page.visible = True
    premium_page.visible = False

    premium_page.update()
    standard_page.update()
    family_page.update()

def next_image(_):
    global counter
    if counter == len(image_room_sources)-1:
        new_counter = 0
        counter = new_counter
        image_container.src = f'{image_room_sources[counter]}'
        image_container_label.value = f'{classification[counter]}'
        
    else:
        new_counter = counter + 1
        counter = new_counter
        image_container.src = f'{image_room_sources[counter]}'
        image_container_label.value = f'{classification[counter]}'
    
    image_container.update()
    image_container_label.update()

def auto_next():
    global counter
    if counter == len(image_room_sources)-1:
        new_counter = 0
        counter = new_counter
        image_container.src = f'{image_room_sources[counter]}'
        image_container_label.value = f'{classification[counter]}'
        
    else:
        new_counter = counter + 1
        counter = new_counter
        image_container.src = f'{image_room_sources[counter]}'
        image_container_label.value = f'{classification[counter]}'
    
    Timer(5, auto_next).start()
    image_container.update()
    image_container_label.update()

def prev_image(_):
    global counter
    if counter == 0:
        new_counter = len(image_room_sources)-1
        counter = new_counter
        image_container.src = f'{image_room_sources[counter]}'
        image_container_label.value = f'{classification[counter]}'
        
    else:
        new_counter = counter - 1
        counter = new_counter
        image_container.src = f'{image_room_sources[counter]}'
        image_container_label.value = f'{classification[counter]}'
    
    image_container.update()
    image_container_label.update()

class view_room_container(ft.UserControl):
    def build(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Container(
                                                content=ft.Text(value='ROOM TYPE:', color='white', font_family='Arial', size=12, weight=ft.FontWeight.BOLD),
                                                padding=ft.padding.only(left=10, top=5)
                                            ),

                                            ft.Row(
                                                [
                                                    ft.ElevatedButton(
                                                        text='STANDARD',
                                                        style=ft.ButtonStyle(
                                                            color="white",
                                                            shape={ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=5)},
                                                            bgcolor="#323232"
                                                        ),
                                                        on_click=open_standard_page
                                                    ),

                                                    ft.ElevatedButton(
                                                        text='FAMILY',
                                                        style=ft.ButtonStyle(
                                                            color="white",
                                                            shape={ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=5)},
                                                            bgcolor="#1A69E8"
                                                        ),
                                                        on_click=open_family_page
                                                    ),

                                                    ft.ElevatedButton(
                                                        text='PREMIUM',
                                                        style=ft.ButtonStyle(
                                                            color="BLACK",
                                                            shape={ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=5)},
                                                            bgcolor="#FFD700"
                                                        ),
                                                        on_click=open_premium_page
                                                    )
                                                ],
                                                alignment=ft.MainAxisAlignment.SPACE_AROUND
                                            ),

                                            ft.Container(
                                                content=ft.Container(
                                                    width=479,
                                                    border=ft.border.all(2, color="white"),
                                                    border_radius=ft.border_radius.all(50)
                                                ),
                                                alignment=ft.alignment.center
                                            )
                                            
                                        ]
                                    ),
                                    width=500,
                                    height=98,
                                    bgcolor="#2A4158",
                                    border_radius=ft.border_radius.all(5)
                                ),
                                ft.Container(
                                    content=ft.Stack(
                                        [
                                            image_container,
                                            ft.Container(
                                                content=ft.Container(
                                                    content=image_container_label,
                                                    bgcolor='#2A4158',
                                                    width=90,
                                                    height=20,
                                                    alignment=ft.alignment.center,
                                                    border_radius=ft.border_radius.all(5)
                                                ),
                                                width=395,
                                                height=120,
                                                alignment=ft.alignment.bottom_center,
                                                padding=ft.padding.only(bottom=5),
                                                opacity=0.6
                                            ),

                                            ft.Container(
                                                content=ft.Row(
                                                    [
                                                        ft.IconButton(icon=ft.icons.NAVIGATE_BEFORE_ROUNDED, icon_size=50, icon_color="#FFD700", on_click=prev_image),
                                                        ft.IconButton(icon=ft.icons.NAVIGATE_NEXT_ROUNDED, icon_size=50, icon_color="#FFD700", on_click=next_image)
                                                    ],
                                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                                ),
                                                width=395,
                                                height=120
                                            )
                                        ]
                                    ),
                                    width=395,
                                    height=120,
                                    bgcolor="#F1F1F1",
                                    border_radius=ft.border_radius.all(5),
                                    border=ft.border.all(2, color="white")
                                ),
                            ]
                        ),
                        height=132,
                        width=908,
                        # border=ft.border.all(1, color="red")
                    ),
                    #list of rooms
                    standard_page,
                    family_page,
                    premium_page
                ]
            ),
            width=1197,
            height=1024,    
            alignment=ft.alignment.center
        )