import flet as ft
from src.app import App

# For more information regarding this app please refer to src/ folder or README.md file


def main(page: ft.Page) -> None:
    """
    Main entry point of the application.

    Initializes the Flet page, creates the App instance
    and starts the user interface. Also provides safe exits
    for both cases (window close and crash/other).
    """
    app = App(page)

    def on_window_event(e: ft.WindowEvent):
        """
        Catches close event and handles app exit correctly.
        """
        if e.data == "close":
            page.window.prevent_close = False
            page.window.close()

    page.window.prevent_close = True
    page.window.on_event = on_window_event

    try:
        app.start()
    except Exception as e:
        import sys
        sys.exit(1)

if __name__ == "__main__":
    ft.app(target=main)
