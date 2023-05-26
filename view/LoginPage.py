import flet as ft

def login_page(page: ft.Page, view: ft.View) -> ft.View:

    view.controls=[(
        ft.Row(
            controls=[
                ft.Container(
                    bgcolor="red",
                    width=556,
                    height=1024
                )
            ]
        )
    )]

    return view 