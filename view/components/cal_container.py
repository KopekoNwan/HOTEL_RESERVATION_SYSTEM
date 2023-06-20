import datetime
import calendar
import flet as ft
from controller.reservation_list_controller import get_reservations

# Get the current year
now = datetime.datetime.now()
current_year = now.year

# Create the calendar
calendar_container = ft.Column([], width='1150', height='400', scroll=ft.ScrollMode.AUTO)

def mark_day_reservations():
    calendar_container.controls.clear()
    reservations = get_reservations()
    # Iterate over each month
    for month_index in range(1, 13):
        # Get the month name
        month_name = calendar.month_name[month_index]

        # Create the row for the month
        month_row = ft.Row([], width='100%')

        # Create the container for the month name
        month_name_container = ft.Container(
            content=ft.Text(value=month_name, color='white', size=16),
            width=80,  # Adjusted to take all available width
            height='10%',  # Adjust the height for a smaller month name container
            bgcolor='#205B64',
            alignment=ft.alignment.center
        )

        # Add the month name container to the beginning of the month row
        month_row.controls.append(month_name_container)

        # Get the number of days in the month
        num_days = calendar.monthrange(current_year, month_index)[1]

        # Iterate over each day in the month
        for day in range(1, num_days + 1):
            # Create the day container
            day_container = ft.Container(
                content=ft.Text(value=str(day), color='black', size=14),
                width=24,  # Adjusted to take all available width
                height=24,  # Adjust the height for a smaller day container
                alignment=ft.alignment.center,
                border=ft.border.all(1, 'black')
            )

            # Check if the current date falls within any of the reservations
            current_date = datetime.date(current_year, month_index, day)
            for reserved_date in reservations:

                check_in_complete = reserved_date.check_in.split(' ')
                check_in = check_in_complete[0].split('-')
                check_out_complete = reserved_date.check_out.split(' ')
                check_out = check_out_complete[0].split('-')

                check_in_year = int(check_in[0])
                check_out_year = int(check_out[0])

                check_in_date = datetime.datetime.strptime(check_in[1], '%m').date()
                check_out_date = datetime.datetime.strptime(check_out[1], '%m').date()

                check_in_day = int(check_in[2])
                check_out_day = int(check_out[2])

                # Check-in and check-out dates
                check_in_date = datetime.date(check_in_year, check_in_date.month, check_in_day)
                check_out_date = datetime.date(check_out_year, check_out_date.month, check_out_day)

                if check_in_date <= current_date <= check_out_date:
                    day_container.bgcolor = 'purple'  # Highlighted color for the selected days
                    break

            # Add the day container to the month row
            month_row.controls.append(day_container)

        # Create the month container
        month_container = ft.Container(
            content=month_row,
            width='100%',  # Adjust the width based on the number of days
            height='15%',  # Adjust the height for a smaller month container
        )

        # Add the month container to the calendar
        calendar_container.controls.append(month_container)


class cal_container(ft.UserControl):
    def build(self):
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Container(width=80, height='10%', content=ft.Text(value='MONTH', size=16, color='white', weight=ft.FontWeight.BOLD), alignment=ft.alignment.center, bgcolor='#B85C3C'),
                    ft.Container(width=1058, height='10%', content=ft.Text(value='DAYS', size=16, color='white',  weight=ft.FontWeight.BOLD), alignment=ft.alignment.center, bgcolor='#B85C3C')
                ]),
                calendar_container,
            ]),
            width=1138,
            height=450,
            bgcolor='white',
            border=ft.border.all(1, '#205B64'),
        )
