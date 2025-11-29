<div align="center">
  <img src="img/icon.png" alt="Image Converter Icon" width="100" height="100">
  <h1>Image Converter</h1>
</div>

A modern, user-friendly image conversion application built with Python and Flet.
Conversion is powered by the Pillow library.

## Features

-   **Wide Format Support**: Convert between a vast array of image formats.
-   **Intuitive Interface**: Easily select files for conversion.
-   **Theme Support**: Switch between Light and Dark modes for a comfortable viewing experience.
-   **Responsive Design**: Clean and intuitive UI that adapts to your workflow.
-   **Secure**: All conversions happen locally on your machine.

## Supported Formats

The application supports conversion **FROM** and **TO** the following formats:

`PNG`, `JPEG`, `JPG`, `BMP`, `GIF`, `TIFF`, `ICO`, `ICNS`, `WEBP`, `PPM`, `PGM`, `PBM`, `PNM`, `TGA`, `DDS`, `PCX`, `IM`, `MPO`, `PFM`, `SGI`

> [!NOTE]
> **PDF** format is supported as an **output** format only (TO PDF).

## Installation

You can run Image Converter using the standalone executable or by running the source code manually.

### Option 1: Windows Executable (Recommended)
The easiest way to run the application on Windows.

1.  Navigate to the `dist` folder.
2.  Run `ImageConverter.exe`.
   
   *No Python installation required.*

### Option 2: Manual Installation
For developers or users on other platforms (macOS, Linux), or if you prefer running from source.

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

## Building from Source
If you wish to build a standalone executable yourself:

1.  **Install development dependencies:**
    ```bash
    pip install flet pyinstaller
    ```

2.  **Build the application:**
    ```bash
    pyinstaller ImageConverter.spec --clean --noconfirm
    ```

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
