# Image Converter

A modern, user-friendly image conversion application built with Python and Flet.

## Features

-   **Wide Format Support**: Convert between PNG, JPEG, BMP, GIF, TIFF, ICO, WEBP, and many more.
-   **Intuitive Interface**: Easily select files for conversion.
-   **Theme Support**: Switch between Light and Dark modes for a comfortable viewing experience.
-   **Responsive Design**: Clean and intuitive UI that adapts to your workflow.
-   **Secure**: All conversions happen locally on your machine.

## Installation

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

## Usage

1.  **Run the application:**
    ```bash
    python main.py
    ```

2.  **Convert an image:**
    -   Click "Choose File" to select an image.
    -   Select your desired output format from the dropdown menu.
    -   Click "Convert Now".
    -   Choose where to save the converted file.

## Requirements

-   Python 3.7+
-   Flet
-   Pillow

## License

[MIT License](LICENSE)
