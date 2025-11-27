from src.app import App
import flet as ft


def main(page: ft.Page):
    app = App(page)
    app.start()

if __name__ == "__main__":
    ft.app(target=main)