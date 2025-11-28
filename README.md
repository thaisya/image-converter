<div align="center">
  <img src="img/icon.png" alt="Image Converter Icon" width="100" height="100">
  <h1>Image Converter</h1>
</div>

A modern, user-friendly image conversion application built with Python and Flet.

## Features

-   **Wide Format Support**: Convert between PNG, JPEG, BMP, GIF, TIFF, ICO, WEBP, and many more.
-   **Intuitive Interface**: Easily select files for conversion.
-   **Theme Support**: Switch between Light and Dark modes for a comfortable viewing experience.
-   **Responsive Design**: Clean and intuitive UI that adapts to your workflow.
-   **Secure**: All conversions happen locally on your machine.

## Installation & Usage

### Windows (Executable)
The application is available as a standalone executable for Windows.
1.  Navigate to the `dist` folder.
2.  Run `ImageConverter.exe`.
   
   *No Python installation required.*

### Python (Cross-Platform)
To run the application from source on Windows, macOS, or Linux:

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd Converter
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python main.py
    ```

## Building from Source (macOS / Linux)
If you wish to build a standalone executable for macOS or Linux, you can use `flet pack`.

1.  **Install development dependencies:**
    ```bash
    pip install flet pyinstaller
    ```

2.  **Build the application:**
    ```bash
    flet pack main.py --name "Image Converter" --icon "img/icon.png" --add-data "img;img"
    ```
    *Note: On non-Windows systems, the icon format and separator in `--add-data` might vary (use `:` instead of `;` on Unix-like systems).*

## Usage Guide

1.  **Convert an image:**
    -   Click "Choose File" to select an image.
    -   Select your desired output format from the dropdown menu.
    -   Click "Convert Now".
    -   Choose where to save the converted file.
    -   Buttons "Reset" and "Light/Dark" theme toggle are self-explanatory.

## Requirements

-   Python 3.7+
-   Flet
-   Pillow

## License

[MIT License](LICENSE)
