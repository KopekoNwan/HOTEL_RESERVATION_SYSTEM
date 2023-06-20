import flet as ft
from controller.customers_controller import get_customers


customers = get_customers()
counter_customer = ft.Text(value=f'Showing {len(customers)} of {len(customers)}', color='black')
#variable for data_table
customer_data=ft.DataTable(
    columns=[
        ft.DataColumn(label=ft.Text('Num.', color='black')),
        ft.DataColumn(label=ft.Text('Last Name', color='black')),
        ft.DataColumn(label=ft.Text('First Name', color='black')),
        ft.DataColumn(label=ft.Text('Email', color='black')),
        ft.DataColumn(label=ft.Text('Contact', color='black')),
        ft.DataColumn(label=ft.Text('Check In', color='black')),
        ft.DataColumn(label=ft.Text('Check Out', color='black')),
        ft.DataColumn(label=ft.Text('Room ID', color='black')),
    ],
    rows=[],
    width=1200
)

customer_column_container = ft.Column(
    [
        #header
        ft.Container(
            content=ft.Row(
                [
                    ft.Row([ft.Icon(name=ft.icons.TABLE_ROWS_ROUNDED, size=25, color='white'),
                    ft.Text('Customer List', color='white', weight=ft.FontWeight.BOLD, size=25),]),
                    counter_customer
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            height=60,
            width=1200,
            bgcolor='#C98F61',
            padding=ft.padding.only(left=20),
            border=ft.border.only(bottom=ft.BorderSide(10, 'white'))
        ),
        #end of header------------------------------------------------------------------------------------------#

        #headers for the data table-----------------------------------------------------------------------------#
        ft.Container(
            content=ft.Column(
                [
                    customer_data
                ],
                scroll=ft.ScrollMode.ALWAYS
            ),
            width=1200,
            height=780,
            bgcolor='#f5f5f5'
        )

    ]
)

def append_customer_list():
    global customers
    Customers_list = get_customers()
    customers = Customers_list
    counter_customer.value = f'Showing {len(customers)} of {len(customers)}'
    customer_data.rows.clear()
    for i, x in enumerate(Customers_list):
        i += 1
        customer_data.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(f'{i}', color='black')),
                    ft.DataCell(ft.Text(f'{x.last_name}', color='black')),
                    ft.DataCell(ft.Text(f'{x.first_name}', color='black')),
                    ft.DataCell(ft.Text(f'{x.email}', color='black')),
                    ft.DataCell(ft.Text(f'{x.contact}', color='black')),
                    ft.DataCell(ft.Text(f'{x.check_in}', color='black')),
                    ft.DataCell(ft.Text(f'{x.check_out}', color='black')),
                    ft.DataCell(ft.Container(content=ft.Text(f'{x.room}', color='black'), bgcolor='#C98F61', border_radius=ft.border_radius.all(50), padding=ft.padding.only(left=5, right=5))),
                ]
            )
        )

append_customer_list()
class view_customers_container(ft.UserControl):
    def build(self):
        return ft.Container(
            content=customer_column_container,
            width=1200,
            height=850,
            alignment=ft.alignment.top_center,
            border=ft.border.only(left=ft.BorderSide(2, 'white'), right=ft.BorderSide(2, 'white'))
        )