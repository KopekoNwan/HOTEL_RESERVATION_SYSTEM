import flet as ft
from view.LoginPage import login_page

#main function
#where run file is calling the main function
def main(page: ft.Page):

    #all available page
    #running first the login_page in LoginPage file
    page_list:list[ft.View] = [
        login_page(page, ft.View('/'))
    ]

    def route_change(route):
        page.views.clear()
        print(route)

        #note learn how this works
        sel = tuple(filter(lambda x: x.route == page.route, page_list))
        page.views.append(sel[0])
        page.go(sel[0].route)

    page.on_route_change = route_change
    page.go(page.route)
