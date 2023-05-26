import flet as ft

def login_page(page: ft.Page, view: ft.View) -> ft.View:

    #login_page settings
    view.padding = 0
    view.bgcolor = "#1A1C2D"

    #reference to our control username and password field
    username = ft.Ref[ft.TextField]()
    password = ft.Ref[ft.TextField]()

    def printt(_):
        print("hi")

    #login_page controls(view)
    view.controls=[(
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
                                                ref=username,
                                                label="Username",
                                                width=470,
                                                prefix_icon=ft.icons.PERSON,
                                                color="#7967FF",
                                                bgcolor="#EBEAF1",
                                            ),
                                            ft.TextField(
                                                ref=password,
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
                                            on_click=printt
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
    )]

    #we then return this view
    return view 