import flet as ft
from controller.cancelled_list_controller import get_cancelled_list


# this variable is used for counting the length of the cancelled list!
cancellations = get_cancelled_list()
counter = ft.Text(value=f'Showing {len(cancellations)} of {len(cancellations)}', color='black')
#variable for data_table
cancelled_data=ft.DataTable(
    columns=[
        ft.DataColumn(label=ft.Text('Cancelled Date', color='black')),
        ft.DataColumn(label=ft.Text('User_ID', color='black')),
        ft.DataColumn(label=ft.Text('Customer', color='black')),
        ft.DataColumn(label=ft.Text('Reservation ID', color='black')),
        ft.DataColumn(label=ft.Text('Email', color='black')),
        ft.DataColumn(label=ft.Text('Contact', color='black')),
        ft.DataColumn(label=ft.Text('Created', color='black')),
    ],
    rows=[],
    width=1150
)

cancelled_column_container = ft.Column(
    [
        #header
        ft.Container(
            content=ft.Row(
                [
                    ft.Row([ft.Icon(name=ft.icons.TABLE_ROWS_ROUNDED, size=25, color='white'),
                    ft.Text('Cancelled Reservation List', color='white', weight=ft.FontWeight.BOLD, size=25),]),
                    counter
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            height=60,
            width=1150,
            bgcolor='#A5B2AB',
            padding=ft.padding.only(left=20),
            border=ft.border.only(bottom=ft.BorderSide(10, 'white'))
        ),
        #end of header------------------------------------------------------------------------------------------#

        #headers for the data table-----------------------------------------------------------------------------#
        ft.Container(
            content=ft.Column(
                [
                    cancelled_data
                ],
                scroll=ft.ScrollMode.ALWAYS
            ),
            width=1150,
            height=780,
            bgcolor='#f5f5f5'
        )

    ]
)

# append all the data in pocket_base collection (cancelled_reservations)
# loop to get the data in list
# we first check if the list is empty
# if it is empty we display something?

def append_cancelled_list():
    global cancellations
    Cancelled_List = get_cancelled_list()
    cancellations = Cancelled_List
    counter.value = f'Showing {len(cancellations)} of {len(cancellations)}'
    cancelled_data.rows.clear()
    for x in Cancelled_List:
        cancelled_data.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(f'{x.cancelled_date}', color='black')),
                    ft.DataCell(ft.Container(content=ft.Text(f'{x.user}', color='black'), bgcolor='#A5B2AB', border_radius=ft.border_radius.all(50), padding=ft.padding.only(left=5, right=5))),
                    ft.DataCell(ft.Text(f'{x.customer}', color='black')),
                    ft.DataCell(ft.Container(content=ft.Text(f'{x.reservation_id}', color='black'), bgcolor='#A5B2AB', border_radius=ft.border_radius.all(50), padding=ft.padding.only(left=5, right=5))),
                    ft.DataCell(ft.Text(f'{x.email}', color='black')),
                    ft.DataCell(ft.Text(f'{x.contact}', color='black')),
                    ft.DataCell(ft.Text(f'{x.created}', color='black')),
                ]
            )
        )

append_cancelled_list()

class view_cancelled_container(ft.UserControl):
    def build(self):
        return ft.Container(
            content=cancelled_column_container,
            width=1150,
            height=850,
            alignment=ft.alignment.top_center,
            border=ft.border.only(left=ft.BorderSide(2, 'white'), right=ft.BorderSide(2, 'white'))
        )