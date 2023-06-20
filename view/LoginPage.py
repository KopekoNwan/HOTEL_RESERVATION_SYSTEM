import flet as ft
from controller.loginControler import login
from view.AppPage import AppPage
from pocketbase.utils import ClientResponseError
from view.components.userID_Card import usernameField
from view.components.userID_Card import userIDField
from view.components.userID_Card import user_avatar
from model.Host import HOST
from model.Host import pb
from model.User import User



username = ft.Ref[ft.TextField]()
password = ft.Ref[ft.TextField]()
user_information:list[User] = []

class LoginPage (AppPage):

    def __init__(self, root, route):
        super().__init__(root=root, route=route)
        self.page.padding = 0
        self.page.bgcolor = "#EDE9E3"
        self.page.did_mount = self.did_mount

    def did_mount(self):
        username.current.value = 'klintjosh'
        password.current.value = '1234567890'

    def get_page(self,) -> ft.View:
        self.page.controls = [
            ft.Stack(
                [
                    ft.Image(src='room_imgs/hotel_bgimg.jpg', height=900),
                    ft.Container(content=ft.Image(src='room_imgs/logo.png', height=50), width=250, padding=ft.padding.only(top=20)),
                    ft.Row(
                    controls=[
                        ft.Container(
                            #container settings
                            bgcolor="#f5f5f5",
                            width=500,
                            height=865,
                            border_radius=ft.border_radius.only(30, 0, 30, 0),
                            alignment = ft.alignment.center,

                            #container's content
                            content=ft.Column(  
                                [
                                    #welcome text
                                    ft.Container(content=ft.Column(
                                            [
                                                ft.Text(value='Welcome Back!', color='#443D2A', weight=ft.FontWeight.BOLD, size=30),
                                                ft.Text(value='Login to continue', size=18, color='#BEBEBE')
                                            ]
                                        ),
                                        width=500,
                                        padding=ft.padding.only(left=50)
                                    ),
                                    #login textfield
                                    ft.Row(
                                        [
                                            ft.Column(
                                                [
                                                    ft.TextField(
                                                        ref=username,
                                                        label="Username",
                                                        width=400,
                                                        prefix_icon=ft.icons.PERSON,
                                                        color="#443D2A",
                                                        bgcolor="#EBEAF1",
                                                    ),
                                                    ft.TextField(
                                                        ref=password,
                                                        password=True,
                                                        can_reveal_password=True,
                                                        label="Password",
                                                        width=400,
                                                        color="#443D2A",
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
                                                                            content=ft.Icon(name=ft.icons.LOGIN, color="#D79551"),
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
                                                    bgcolor="#D79551",
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
                                spacing=50
                            )
                        )
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    )
                ]
            )
        ]

        return self.page
    

    def on_login(self, _):
        try:
            login(username=username.current.value,
                password=password.current.value)
            results = pb.collection('users').auth_with_password(username.current.value, password.current.value)
            user = results.record.__dict__['collection_id']
            usernameField.value = username.current.value
            userIDField.value = user['id']
            avatar = user['avatar']
            user_avatar.src = f'{HOST}api/files/_pb_users_auth_/{userIDField.value}/{avatar}?token='
            self.root.go(route='/front_desk')
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