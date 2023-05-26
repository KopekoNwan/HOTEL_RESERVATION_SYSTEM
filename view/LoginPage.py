import flet as ft
from controller.loginControler import login
from view.AppPage import AppPage
from pocketbase.utils import ClientResponseError


class LoginPage (AppPage):
    username = ft.Ref[ft.TextField]()
    password = ft.Ref[ft.TextField]()

    def __init__(self, root, route):
        super().__init__(root=root, route=route)
        self.page.padding = 0
        self.page.bgcolor = "#1A1C2D"
        self.page.did_mount = self.did_mount

    def did_mount(self):
        self.username.current.value = 'klintjosh'
        self.password.current.value = '1234567890'

    def get_page(self,) -> ft.View:
        self.page.controls = [
            ft.Row(
            controls=[
                ft.Container(
                    #container settings
                    bgcolor="#7967FF",
                    width=556,
                    height=1070,
                    border_radius=ft.border_radius.only(50, 0, 50, 0),
                    alignment = ft.alignment.center,

                    #container's content
                    content=ft.Column(  
                        [
                            #login textfield
                            ft.Row(
                                [
                                    ft.Column(
                                        [
                                            ft.TextField(
                                                ref=self.username,
                                                label="Username",
                                                width=470,
                                                prefix_icon=ft.icons.PERSON,
                                                color="#7967FF",
                                                bgcolor="#EBEAF1",
                                            ),
                                            ft.TextField(
                                                ref=self.password,
                                                password=True,
                                                can_reveal_password=True,
                                                label="Password",
                                                width=470,
                                                color="#7967FF",
                                                prefix_icon=ft.icons.PASSWORD,
                                                bgcolor="#EBEAF1"
                                            ),
                                        ],
                                        spacing=100
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            
                            #login button
                            ft.Container(
                                content=ft.ElevatedButton(
                                            content=ft.Row(
                                                [
                                                    ft.Container(
                                                        content=ft.Text(value="LOG IN", color="#FFFFFF", size=18),
                                                        padding=ft.padding.only(left=40)
                                                    ),
                                                    ft.Container(
                                                        content=ft.Container(
                                                                    content=ft.Icon(name=ft.icons.LOGIN, color="#62CECA"),
                                                                    shape=ft.BoxShape.CIRCLE,
                                                                    bgcolor="white",
                                                                    width=55,
                                                                    height=55,
                                                        ),
                                                        padding=ft.padding.only(left=20)
                                                    
                                                    )
                                                ],
                                                alignment=ft.MainAxisAlignment.CENTER,
                                            ),
                                            bgcolor="#62CECA",
                                            width=200,
                                            height=55,
                                            on_click=self.on_login
                                        ),
                                width=556,
                                height=100,
                                alignment=ft.alignment.center,
                            )
                        ],
                        #Column settings:
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=100
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.END,
        )
        ]

        return self.page

    def on_login(self, _):
        try:
            login(username=self.username.current.value,
                  password=self.password.current.value)
            print("hi user")
        except ClientResponseError:
            ok = ft.Ref[ft.TextButton]()
            dialog = ft.AlertDialog(
                modal=True, content=ft.Text('Username or password not found'),
                actions=[
                    ft.TextButton('OK', ref=ok)
                ]
            )

            def on_close(_):
                dialog.open = False
                self.root.update()
            ok.current.on_click = on_close

            self.root.dialog = dialog
            dialog.open = True
            self.root.update()
