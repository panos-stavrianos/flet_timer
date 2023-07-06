from datetime import datetime
import flet as ft
from flet_timer.flet_timer import Timer


def main(page: ft.Page):
    page.title = "Flet Timer example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    txt_time = ft.Text(value="None")

    def refresh():
        txt_time.value = datetime.now().strftime("%H:%M:%S")
        page.update()

    timer = Timer(name="timer", interval_s=1, callback=refresh)

    page.add(
        timer,
        txt_time
    )


ft.app(main)
