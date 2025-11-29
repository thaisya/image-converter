import flet as ft
from typing import Optional, List, Tuple
from .utils import filename_format_separator, convert, resource_path


class App:
    """
    Main application class for the Image Converter.
    Handles UI initialization, event handling, and theme management.
    """

    def __init__(self, page: ft.Page):
        """
        Initialize the App with the given Flet page.

        Args:
            page (ft.Page): The main Flet page instance.
        """
        self.page = page
        self.page.title = "Image Converter"
        self.page.window_resizable = True
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # Window dimensions
        self.page.window_width = 1000
        self.page.window_height = 800

        self.is_dark_theme: bool = False

        # Set window icon
        self.icon_path: str = resource_path("img", "icon.ico")
        self.page.window.icon = self.icon_path
        
        # Theme Colors (Initialized with Light Theme defaults)
        self.primary_color: str = "#5DADE2"
        self.text_color: str = "#2C3E50"
        self.button_color: str = "white"
        self.button_bg_color: str = "#5DADE2"
        self.dropdown_fill_color: str = "white"
        self.dropdown_border_color: str = "#5DADE2"
        self.dropdown_text_color: str = "#2C3E50"
        self.header_bg_color: str = "white"
        self.main_card_bg_color: str = "white"
        self.container_bg_color: str = ft.Colors.BLUE_50
        self.container_border_color: str = "#5DADE2"
        self.icon_color: str = "#5DADE2"
        self.shadow_color: str = ft.Colors.with_opacity(0.1, ft.Colors.BLACK)
        
        # Supported Formats
        self.to_formats: List[str] = [
            "PNG", "JPEG", "JPG", "BMP", "GIF", "TIFF", "ICO", "ICNS", "WEBP", "PPM",
            "PGM", "PBM", "PNM", "TGA", "DDS", "PCX", "IM", "MPO", "PFM", "SGI", "PDF",
        ]

        # State
        self.input_file: Optional[Tuple[str, Optional[str], str]] = None

        # UI Components Initialization
        self.selected_file_text = ft.Text(
            "No file selected", 
            color=self.text_color, 
            size=16, 
            text_align=ft.TextAlign.CENTER
        )
        
        self.txt_from = ft.Text(
            "FROM: NAN", 
            size=40, 
            weight=ft.FontWeight.BOLD, 
            color=self.primary_color
        )
        self.txt_to = ft.Text(
            "TO: PNG", 
            size=40, 
            weight=ft.FontWeight.BOLD, 
            color=self.primary_color
        )

        self.dd = ft.Dropdown(
            editable=True,
            options=self.get_options(),
            width=180,
            value="PNG",
            on_change=self.on_format_change,
            border_color=self.dropdown_border_color,
            text_style=ft.TextStyle(color=self.dropdown_text_color, size=16),
            focused_border_color=self.dropdown_border_color,
            border_radius=10,
            content_padding=15,
            filled=True,
            fill_color=self.dropdown_fill_color,
            enable_search=True,
            menu_height=200,
            enable_filter=True,
        )
        
        self.file_picker = ft.FilePicker(on_result=self.on_file_result)
        self.save_file_picker = ft.FilePicker(on_result=self.on_save_result)
        
        self.file_picker_button = ft.ElevatedButton(
            "Choose File",
            icon=ft.Icons.UPLOAD_FILE,
            on_click=lambda _: self.file_picker.pick_files(allow_multiple=False),
            bgcolor=self.button_bg_color,
            color=self.button_color,
            width=180,
            height=50,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                elevation=0,
                text_style=ft.TextStyle(size=16)
            )
        )
        
        self.convert_button = ft.ElevatedButton(
            "Convert Now",
            icon=ft.Icons.TRANSFORM,
            on_click=self.on_convert,
            bgcolor=self.button_bg_color,
            color=self.button_color,
            width=410,
            height=80,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                elevation=2,
                text_style=ft.TextStyle(size=18)
            )
        )
        
        self.reset_button = ft.IconButton(
            icon=ft.Icons.REFRESH,
            icon_color=self.icon_color,
            icon_size=50,
            tooltip="Reset",
            on_click=self.reset_state
        )
        
        self.theme_button = ft.IconButton(
            icon=ft.Icons.LIGHT_MODE,
            icon_color=self.icon_color,
            icon_size=50,
            tooltip="Dark theme",
            on_click=self.theme_switch
        )
        
        # Containers (Initialized in start())
        self.header_container: Optional[ft.Container] = None
        self.main_card_container: Optional[ft.Container] = None
        self.from_container: Optional[ft.Container] = None
        self.to_container: Optional[ft.Container] = None
        self.arrow_icon: Optional[ft.Icon] = None
        self.header_title: Optional[ft.Text] = None
        self.target_format_label: Optional[ft.Text] = None

    def reset_state(self, e: ft.ControlEvent) -> None:
        """
        Resets the application state to default values.
        """
        self.input_file = None
        self.selected_file_text.value = "No file selected"
        self.txt_from.value = "FROM: NAN"
        self.dd.value = "PNG"
        self.txt_to.value = "TO: PNG"
        
        self.selected_file_text.update()
        self.txt_from.update()
        self.dd.update()
        self.txt_to.update()

    def theme_switch(self, e: ft.ControlEvent) -> None:
        """
        Toggles between Light and Dark themes and updates UI colors.
        """
        self.is_dark_theme = not self.is_dark_theme
        self.theme_button.icon = ft.Icons.DARK_MODE if self.is_dark_theme else ft.Icons.LIGHT_MODE
        self.theme_button.tooltip = "Light theme" if self.is_dark_theme else "Dark theme"

        if self.is_dark_theme:
            self.primary_color = "#7CB9E8"
            self.text_color = "#E0E0E0"
            self.button_color = "#1E1E1E"
            self.button_bg_color = "#7CB9E8"
            self.dropdown_fill_color = "#2C2C2C"
            self.dropdown_border_color = "#7CB9E8"
            self.dropdown_text_color = "#E0E0E0"
            self.header_bg_color = "#2C2C2C"
            self.main_card_bg_color = "#2C2C2C"
            self.container_bg_color = "#3A3A3A"
            self.container_border_color = "#7CB9E8"
            self.icon_color = "#7CB9E8"
            self.shadow_color = ft.Colors.with_opacity(0.3, ft.Colors.BLACK)
        else:
            self.primary_color = "#5DADE2"
            self.text_color = "#2C3E50"
            self.button_color = "white"
            self.button_bg_color = "#5DADE2"
            self.dropdown_fill_color = "white"
            self.dropdown_border_color = "#5DADE2"
            self.dropdown_text_color = "#2C3E50"
            self.header_bg_color = "white"
            self.main_card_bg_color = "white"
            self.container_bg_color = ft.Colors.BLUE_50
            self.container_border_color = "#5DADE2"
            self.icon_color = "#5DADE2"
            self.shadow_color = ft.Colors.with_opacity(0.1, ft.Colors.BLACK)

        # Update UI Elements
        self.theme_button.icon_color = self.icon_color
        self.reset_button.icon_color = self.icon_color
        self.txt_from.color = self.primary_color
        self.txt_to.color = self.primary_color
        self.selected_file_text.color = self.text_color
        
        self.dd.border_color = self.dropdown_border_color
        self.dd.focused_border_color = self.dropdown_border_color
        self.dd.fill_color = self.dropdown_fill_color
        self.dd.text_style = ft.TextStyle(color=self.dropdown_text_color, size=16)
        
        self.file_picker_button.bgcolor = self.button_bg_color
        self.file_picker_button.color = self.button_color
        self.convert_button.bgcolor = self.button_bg_color
        self.convert_button.color = self.button_color
        
        if self.header_container:
            self.header_container.bgcolor = self.header_bg_color
        
        if self.main_card_container:
            self.main_card_container.bgcolor = self.main_card_bg_color
            self.main_card_container.shadow = ft.BoxShadow(
                spread_radius=0,
                blur_radius=20,
                color=self.shadow_color,
                offset=ft.Offset(0, 10),
            )
        
        if self.from_container:
            self.from_container.bgcolor = self.container_bg_color
            self.from_container.border = ft.border.all(2, self.container_border_color)
        
        if self.to_container:
            self.to_container.bgcolor = self.container_bg_color
            self.to_container.border = ft.border.all(2, self.container_border_color)
        
        if self.arrow_icon:
            self.arrow_icon.color = self.icon_color
        
        if self.header_title:
            self.header_title.color = self.primary_color
        
        if self.target_format_label:
            self.target_format_label.color = self.text_color
        
        self.page.update()

    def on_format_change(self, e: ft.ControlEvent) -> None:
        """
        Updates the 'TO' text when the dropdown selection changes.
        """
        self.txt_to.value = f"TO: {self.dd.value}"
        self.txt_to.update()

    def on_file_result(self, e: ft.FilePickerResultEvent) -> None:
        """
        Handles the result of the file picker dialog.
        """
        if e.files:
            file = e.files[0]
            name, ext = filename_format_separator(file.name)
            path = file.path
            self.input_file = (name, ext, path)
            
            # Truncate filename if too long
            display_name = file.name if len(file.name) < 20 else file.name[:17] + "..."
            self.selected_file_text.value = f"Selected: {display_name}"
            
            if ext:
                self.txt_from.value = f"FROM: {ext.upper()}"
            else:
                self.txt_from.value = "FROM: NAN"
            
            self.selected_file_text.update()
            self.txt_from.update()
        else:
            self.input_file = None
            self.selected_file_text.value = "No file selected"
            self.txt_from.value = "FROM: NAN"
            self.selected_file_text.update()
            self.txt_from.update()

    def on_convert(self, e: ft.ControlEvent) -> None:
        """
        Initiates the conversion process.
        """
        if not self.input_file:
            snack_bar = ft.SnackBar(content=ft.Text("Please select a file first!"))
            self.page.overlay.append(snack_bar)
            snack_bar.open = True
            self.page.update()
            return
        
        target_format = self.dd.value
        name, ext, path = self.input_file
        
        # Open save dialog
        self.save_file_picker.save_file(
            dialog_title="Save Converted File",
            file_name=f"{name}.{target_format.lower()}",
            allowed_extensions=[target_format.lower()]
        )

    def on_save_result(self, e: ft.FilePickerResultEvent) -> None:
        """
        Handles the result of the save file dialog and performs the conversion.
        """
        if e.path:
            name, ext, path = self.input_file
            try:
                img = convert(name, ext, path)
                img.save(e.path)
                
                snack_bar = ft.SnackBar(
                    content=ft.Text(f"Success! Saved to {e.path}"),
                    bgcolor="green"
                )
                self.page.overlay.append(snack_bar)
                snack_bar.open = True
                self.page.update()

            except Exception as ex:
                snack_bar = ft.SnackBar(
                    content=ft.Text(f"Error: {ex}"),
                    bgcolor="red"
                )
                self.page.overlay.append(snack_bar)
                snack_bar.open = True
                self.page.update()

    def get_options(self) -> List[ft.DropdownOption]:
        """
        Returns a list of dropdown options for supported formats.
        """
        return [ft.DropdownOption(fmt) for fmt in self.to_formats]

    def start(self) -> None:
        """
        Builds and displays the main UI.
        """
        self.page.overlay.extend([self.file_picker, self.save_file_picker])
 
        self.header_title = ft.Text(
            "Image Converter", 
            size=45, 
            weight=ft.FontWeight.BOLD, 
            color=self.primary_color
        )
        
        self.header_container = ft.Container(
            content=ft.Row([
                ft.Row([
                    ft.Container(
                        content=ft.Image(
                            src=self.icon_path,
                            width=50,
                            height=50,
                            fit=ft.ImageFit.CONTAIN,
                        ),
                        margin=ft.Margin(top=8, bottom=0, left=0, right=0),
                    ),
                    self.header_title,
                ], spacing=30, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                ft.Container(
                    content=ft.Row(
                        [
                          self.reset_button,
                          self.theme_button
                        ],
                        spacing=30,
                    )
                )
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            bgcolor=self.header_bg_color
        )
        
        self.from_container = ft.Container(
            content=self.txt_from,
            padding=50,
            bgcolor=self.container_bg_color,
            border_radius=15,
            border=ft.border.all(2, self.container_border_color),
        )
        
        self.arrow_icon = ft.Icon(ft.Icons.ARROW_FORWARD, color=self.icon_color, size=70)
        
        self.to_container = ft.Container(
            content=self.txt_to,
            padding=50,
            bgcolor=self.container_bg_color,
            border_radius=15,
            border=ft.border.all(2, self.container_border_color),
        )
        
        self.target_format_label = ft.Text("Target Format", size=16, color=self.text_color)
        
        self.main_card_container = ft.Container(
            expand=True,
            content=ft.Column(
                [
                    ft.Container(
                        expand=False,
                        content=ft.Row(
                            [
                                self.from_container,
                                ft.Container(
                                    content=self.arrow_icon,
                                    alignment=ft.alignment.center,
                                ),
                                self.to_container,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=30
                        ),
                        padding=ft.Padding(left=0, top=0, right=60, bottom=0),
                    ),
                    
                    ft.Divider(height=50, color="transparent"),

                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.Column([
                                            self.file_picker_button,
                                            self.selected_file_text
                                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),

                                        ft.Column([
                                            self.dd,
                                            self.target_format_label
                                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=50
                                ),

                                ft.Row(
                                    [
                                        self.convert_button,
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=10
                                )
                            ],
                            spacing=70,
                        )
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO,
            ),
            padding=ft.Padding(left=0, top=40, right=0, bottom=0),
            bgcolor=self.main_card_bg_color,
            alignment=ft.alignment.center,
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=20,
                color=self.shadow_color,
                offset=ft.Offset(0, 10),
            )
        )
        
        self.page.add(
            ft.Column([
                self.header_container,
                self.main_card_container
            ], spacing=0, expand=True)
        )
