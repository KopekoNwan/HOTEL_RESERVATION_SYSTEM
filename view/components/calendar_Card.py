import flet as ft
import datetime

month = datetime.datetime.now()
month_field = ft.Text(value=f'{month.strftime("%B")}', color="white", font_family="Arial", size=20, weight=ft.FontWeight.BOLD)
day_field = ft.Text(value=f'{month.strftime("%d")}', color="#D79551", font_family="Arial", size=100, weight=ft.FontWeight.BOLD)
week_field = ft.Text(value=f'{month.strftime("%A")}', color="#D79551", font_family="Arial", size=20, weight=ft.FontWeight.BOLD)

calendar_Card = ft.Container(
    content=ft.Container(
        content=ft.Stack(
            [
                ft.Container(
                    content=month_field,
                    width=200,
                    height=50,
                    bgcolor="#D79551",
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(top=10)
                ),
                ft.Row(
                    [
                        ft.Container(
                            shape=ft.BoxShape.CIRCLE,
                            width=15,
                            height=15,
                            bgcolor="white"
                        ),
                        ft.Container(
                            shape=ft.BoxShape.CIRCLE,
                            width=15,
                            height=15,
                            bgcolor="white"
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                ),
                ft.Row(
                    [
                        ft.Container(
                            width=8,
                            height=20,
                            bgcolor="#4A4A4A",
                            border_radius=ft.border_radius.all(50)
                        ),
                        ft.Container(
                            width=8,
                            height=20,
                            bgcolor="#4A4A4A",
                            border_radius=ft.border_radius.all(50)
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                ),
                ft.Container(
                    content=day_field,
                    width=200,
                    height=200,
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(top=30)
                ),
                ft.Container(
                    content=week_field,
                    width=200,
                    height=200,
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(top=150)
                )
            ],
            width=200,
            height=500,
        ),
    width=180,
    height=180,
    bgcolor="white",
    border_radius=ft.border_radius.all(10),
    margin=ft.margin.only(top=10, bottom=10)
    ),
width=224,
alignment=ft.alignment.center,
)