import flet as ft

class date_picker_container(ft.UserControl):
    day = 1
    days = ft.Dropdown(width=50, height=30, content_padding=2, text_size=12, color='white', alignment=ft.alignment.center)
    months = ft.Dropdown(
                        alignment=ft.alignment.center,
                        color='white',
                        height=30,
                        width=150,
                        text_size=12,
                        content_padding=2,
                        options=[
                            ft.dropdown.Option('January'),
                            ft.dropdown.Option('February'),
                            ft.dropdown.Option('March'),
                            ft.dropdown.Option('April'),
                            ft.dropdown.Option('May'),
                            ft.dropdown.Option('June'),
                            ft.dropdown.Option('July'),
                            ft.dropdown.Option('August'),
                            ft.dropdown.Option('September'),
                            ft.dropdown.Option('October'),
                            ft.dropdown.Option('November'),
                            ft.dropdown.Option('December'),
                        ]
    )
    while day != 32:
        days.options.append(ft.dropdown.Option(f'{day}'))
        day = day + 1

    def build(self):
        return ft.Container(
            content=ft.Row(
                [
                    self.months,
                    self.days
                ]
            )
        )