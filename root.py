import flet as ft
from view.AppPage import AppPage
from view.LoginPage import LoginPage

#main function
#where run file is calling the main function
def main(page: ft.Page):

    #all available page
    #running first the login_page in LoginPage file
    page_list:list[AppPage] = [
        LoginPage(root=page, route='/')
    ]

    def route_change(_):
        page.views.clear()
        print(page_list[0].page.route)

        sel = tuple(filter(lambda x: x.page.route == page.route, page_list))
        page.views.append(sel[0].get_page())
        page.go(sel[0].page.route)

    page.on_route_change = route_change
    page.go(page.route)
