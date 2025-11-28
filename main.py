from src.app import App
import flet as ft

# For more information regarding this app please refer to src/ folder or README.md file


def main(page: ft.Page) -> None:
    """
    Main entry point of the application.

    Initializes the Flet page, creates the App instance
    and starts the user interface.
    """
    app = App(page)
    app.start()


if __name__ == "__main__":
    ft.app(target=main)
