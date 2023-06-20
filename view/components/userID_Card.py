import flet as ft

usernameField = ft.Text(value="", font_family="Arial", weight=ft.FontWeight.BOLD, color='black')
userIDField = ft.Text(value="", font_family="Arial", weight=ft.FontWeight.NORMAL, size=8, color='black')
user_avatar = ft.Image(src="", fit=ft.ImageFit.COVER)

userID_Card = ft.Container(content=ft.Container(
content=ft.Stack(
    [
        ft.Container(
            width=244,
            height=51,
            bgcolor="#D79551",
            border_radius=ft.border_radius.only(5, 5, 0, 0)
        ),
        ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        content=user_avatar,
                        width=120, 
                        height=120,
                        #bgcolor="#7967FF",
                        border=ft.border.all(5, color="white"),
                        border_radius=ft.border_radius.all(5)
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Container(
                                    content=ft.Text(value='USERNAME:', font_family="Arial", size=8),
                                    bgcolor="#434343",
                                    border_radius=ft.border_radius.all(50),
                                    padding=ft.padding.only(right=5, left=5)
                                ),
                                usernameField,
                                ft.Container(
                                    content=ft.Text(value='USER_ID:', font_family="Arial", size=8),
                                    bgcolor="#434343",
                                    border_radius=ft.border_radius.all(50),
                                    padding=ft.padding.only(right=5, left=5)
                                ),
                                userIDField
                            ],
                            spacing=2
                        ),
                        padding=ft.padding.only(top=50)
                    )   
                ]
            ),
            padding=ft.padding.only(top=10, left=12)
        )
    ]
),
width=224,
height=150,
border_radius=ft.border_radius.all(5),
border=ft.border.all(1, color="black")
),
padding=ft.padding.only(top=10)
)