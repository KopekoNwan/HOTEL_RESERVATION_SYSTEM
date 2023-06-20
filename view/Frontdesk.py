import flet as ft
from view.AppPage import AppPage
from view.components.userID_Card import userID_Card
from view.components.calendar_Card import calendar_Card
from view.components.view_room_container import view_room_container
from view.components.view_reservation_container import view_reservation_container
from view.components.view_cancelled_container import view_cancelled_container
from view.components.view_customers_container import view_customers_container
from view.components.view_room_container import auto_next
from view.components.standard_room_view import append_standard_images
from view.components.family_room_view import append_family_images
from view.components.premium_room_view import append_premium_images
from model.updated_records import updated_records
from view.components.view_reservation_container import run_clock
from view.components.view_reservation_container import clock
from view.components.view_reservation_container import show_reservations



class Frontdesk(AppPage):
    #Instance of pages or containers stored in a variable
    #And its view Container
    #View Room COntainer instance
    room_container = view_room_container()
    reservation_container = view_reservation_container()
    cancelled_container = view_cancelled_container()
    customers_container = view_customers_container()
    room_page = ft.Container(content=room_container, visible=False)
    reservation_page = ft.Container(content=reservation_container, visible=True)
    cancelled_page = ft.Container(content=cancelled_container, visible=False)
    customers_page = ft.Container(content=customers_container, visible=False)
            
    #View Room Function for Room Button
    def open_room_page(self, _):
        self.customers_page.visible = False
        self.cancelled_page.visible = False
        self.reservation_page.visible = False
        self.room_page.visible = True
        self.customers_page.update()
        self.cancelled_page.update()
        self.reservation_page.update()
        self.room_page.update()
        self.page.update()
    def open_reservation_page(self, _):
        self.customers_page.visible = False
        self.cancelled_page.visible = False
        self.reservation_page.visible = True
        self.room_page.visible = False
        self.customers_page.update()
        self.cancelled_page.update()
        self.reservation_page.update()
        self.room_page.update()
        self.page.update()
    def open_cancelled_page(self, _):
        self.customers_page.visible = False
        self.cancelled_page.visible = True
        self.reservation_page.visible = False
        self.room_page.visible = False
        self.customers_page.update()
        self.cancelled_page.update()
        self.reservation_page.update()
        self.room_page.update()
        self.page.update()
    def open_customer_page(self, _):
        self.customers_page.visible = True
        self.cancelled_page.visible = False
        self.reservation_page.visible = False
        self.room_page.visible = False
        self.customers_page.update()
        self.cancelled_page.update()
        self.reservation_page.update()
        self.room_page.update()
        self.page.update()

    def __init__(self, root, route):
        super().__init__(root=root, route=route)
        self.page.padding = 0
        self.page.bgcolor = "#1A1C2D"
        self.page.did_mount = self.did_mount

    def did_mount(self,):
        show_reservations()
        self.run_clock = True
        auto_next()
        append_standard_images()
        append_family_images()
        append_premium_images()
        updated_records()
        clock()

    def on_logout(self, _):
        self.run_clock = False
        self.root.go(route='/')
        

    #function for returing all the View Controls
    def get_page(self,) -> ft.View:
        self.page.controls = [
            ft.Row(
                [
                    #side navigation components
                    ft.Container(
                        content=ft.Container(
                            content=ft.Column(
                                [
                                    #user Id container
                                    userID_Card,
                                    #minimalist calendar
                                    calendar_Card,
                                    #line
                                    ft.Container(width=222, border=ft.border.all(3, color="#D79551"), border_radius=ft.border_radius.all(50)),
                                    
                                    #side navigation buttons
                                    ft.Container(
                                        content=ft.Column(
                                            [
                                                ft.Container(
                                                    content=ft.ElevatedButton(
                                                                content=ft.Row(
                                                                    [
                                                                        ft.Container(
                                                                            content=ft.Text(value="RESERVATIONS", color="#FFFFFF", size=18),
                                                                            alignment=ft.alignment.center
                                                                        ),
                                                                        ft.Container(
                                                                            content=ft.Container(
                                                                                        content=ft.Icon(name=ft.icons.CALENDAR_MONTH, color="#D3B8A5"),
                                                                                        shape=ft.BoxShape.CIRCLE,
                                                                                        bgcolor="white",
                                                                                        width=55,
                                                                                        height=55,
                                                                            )
                                                                        
                                                                        )
                                                                    ],
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                ),
                                                                bgcolor="#D3B8A5",
                                                                width=200,
                                                                height=55,
                                                                on_click=self.open_reservation_page
                                                            ),
                                                    width=556,
                                                    height=100,
                                                    alignment=ft.alignment.center,
                                                ),

                                                ft.Container(
                                                    content=ft.ElevatedButton(
                                                                content=ft.Row(
                                                                    [
                                                                        ft.Container(
                                                                            content=ft.Text(value="CANCELLED", color="#FFFFFF", size=18),
                                                                            padding=ft.padding.only(right=25),
                                                                            alignment=ft.alignment.center
                                                                        ),
                                                                        ft.Container(
                                                                            content=ft.Container(
                                                                                        content=ft.Icon(name=ft.icons.CANCEL_PRESENTATION, color="#A5B2AB"),
                                                                                        shape=ft.BoxShape.CIRCLE,
                                                                                        bgcolor="white",
                                                                                        width=55,
                                                                                        height=55,
                                                                            )
                                                                        )
                                                                    ],
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                ),
                                                                bgcolor="#A5B2AB",
                                                                width=200,
                                                                height=55,
                                                                on_click=self.open_cancelled_page
                                                            ),
                                                    width=556,
                                                    height=100,
                                                    alignment=ft.alignment.center,
                                                ),

                                                ft.Container(
                                                    content=ft.ElevatedButton(
                                                                content=ft.Row(
                                                                    [
                                                                        ft.Container(
                                                                            content=ft.Text(value="CUSTOMERS", color="#FFFFFF", size=18),
                                                                            padding=ft.padding.only(right=20),
                                                                            alignment=ft.alignment.center
                                                                        ),
                                                                        ft.Container(
                                                                            content=ft.Container(
                                                                                        content=ft.Icon(name=ft.icons.PERSON, color="#C98F61"),
                                                                                        shape=ft.BoxShape.CIRCLE,
                                                                                        bgcolor="white",
                                                                                        width=55,
                                                                                        height=55,
                                                                            )
                                                                        )
                                                                    ],
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                ),
                                                                bgcolor="#C98F61",
                                                                width=200,
                                                                height=55,
                                                                on_click=self.open_customer_page
                                                            ),
                                                    width=556,
                                                    height=100,
                                                    alignment=ft.alignment.center,
                                                ),

                                                ft.Container(
                                                    content=ft.ElevatedButton(
                                                                content=ft.Row(
                                                                    [
                                                                        ft.Container(
                                                                            content = ft.Text(value="ROOMS", color="#FFFFFF", size=18),
                                                                            padding=ft.padding.only(right=60),
                                                                            alignment=ft.alignment.center
                                                                        ),
                                                                        ft.Container(
                                                                            content=ft.Container(
                                                                                        content=ft.Icon(name=ft.icons.BED, color="#3D5D52"),
                                                                                        shape=ft.BoxShape.CIRCLE,
                                                                                        bgcolor="white",
                                                                                        width=55,
                                                                                        height=55,
                                                                            ),
                                                                        )
                                                                    ],
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                ),
                                                                bgcolor="#3D5D52",
                                                                width=200,
                                                                height=55,
                                                                on_click=self.open_room_page
                                                            ),
                                                    width=556,
                                                    height=100,
                                                    alignment=ft.alignment.center,
                                                ),

                                                ft.Container(width=222, border=ft.border.all(3, color="#D79551"), border_radius=ft.border_radius.all(50)),
                                            ],
                                            spacing=1
                                        ),
                                        width=243
                                    ),

                                    #logout button
                                    ft.Container(
                                        content=ft.ElevatedButton(
                                            content=ft.Row(
                                                [
                                                    ft.Container(
                                                        content=ft.Text(value="LOG OUT", color="#FFFFFF", size=18),
                                                        padding=ft.padding.only(right=60),
                                                        alignment=ft.alignment.center
                                                    ),
                                                    ft.Container(
                                                        content=ft.Container(
                                                                    content=ft.Icon(name=ft.icons.LOGOUT, color="#352E28", rotate=ft.Rotate(angle=15.7, alignment=ft.alignment.center)),
                                                                    shape=ft.BoxShape.CIRCLE,
                                                                    bgcolor="white",
                                                                    width=55,
                                                                    height=55,
                                                        ),
                                                    )
                                                ],
                                                alignment=ft.MainAxisAlignment.CENTER,
                                            ),
                                            bgcolor="#352E28",
                                            width=209,
                                            height=55,
                                            on_click=self.on_logout,
                                            
                                        ),
                                        margin=ft.margin.only(top=5),
                                    )
                                ],
                                spacing=2
                            ),
                            width=243,
                            height=860,
                            bgcolor="#f5f5f5",
                            border_radius=ft.border_radius.only(0, 20, 0, 20),
                            alignment=ft.alignment.center,
                            padding=ft.padding.only(left=10)
                        ),
                        width=243,
                        height=1000,
                        alignment=ft.alignment.top_left
                    ),
                    
                    ft.Container(
                        content=ft.Row(
                            [
                                #View Room Container invoked
                                self.room_page,
                                self.reservation_page,
                                self.cancelled_page,
                                self.customers_page
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            width=1197                 
                        ),
                        height=1000,
                        alignment=ft.alignment.top_center
                    )
                    
                ],
            )
        ]

        return self.page