from PIL import Image
from typing import Tuple, Optional

def filename_format_separator(filename: str) -> Tuple[str, Optional[str]]:
    """
    Separates the filename from its extension.

    Args:
        filename (str): The full name of the file.

    Returns:
        Tuple[str, Optional[str]]: A tuple containing the filename and the extension (uppercase).
                                   If no extension is found, returns (filename, None).
    """
    if "." in filename:
        name, ext = filename.rsplit(".", 1)
        ext = ext.upper()
    else:
        name, ext = filename, None
    return name, ext

def convert(name: str, ext: str, path: str) -> Image.Image:
    """
    Opens an image file and prepares it for conversion.

    Args:
        name (str): The name of the file.
        ext (str): The extension of the file.
        path (str): The absolute path to the file.

    Returns:
        Image.Image: The PIL Image object.
    """
    img = Image.open(path)
    if ext and ext.lower() in ["jpg", "jpeg"]:
        img = img.convert("RGB")
    return img

