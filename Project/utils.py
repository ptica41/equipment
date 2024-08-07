import base64
import os
import string
from openpyxl.drawing.image import Image as ExcelImage
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.cell import MergedCell, Cell


class SheetImageLoader:
    """Loads all images in a sheet"""
    _images: dict[str, ExcelImage] = {}

    def __init__(self, sheet: Worksheet):
        """Loads all sheet images"""
        sheet_images = sheet._images
        for image in sheet_images:
            row = image.anchor._from.row + 1
            col = string.ascii_uppercase[image.anchor._from.col]
            self._images[f'{col}{row}'] = image

    def image_in(self, cell):
        """Checks if there's an image in specified cell"""
        return cell in self._images

    def get(self, cell):
        """Retrieves image data from a cell"""
        if cell not in self._images:
            raise ValueError("Cell {} doesn't contain an image".format(cell))
        else:
            image = self._images[cell]
            return f"data:{image.format.lower()};base64," + base64.b64encode(image.ref.getvalue()).decode()


def get_value_from_merged_cell(ws: Worksheet, cell: MergedCell | Cell) -> str:
    """Получить значение с объединенной ячейки"""
    if not isinstance(cell, MergedCell):
        return cell.value

    for cell_range in ws.merged_cells.ranges:
        if cell.coordinate in cell_range:
            return cell_range.start_cell.value


def get_value_from_merged_image(
    ws: Worksheet,
    image_loader: SheetImageLoader,
    cell: MergedCell | Cell
) -> str:
    """Получить изображение с объединенной ячейки"""
    if not isinstance(cell, MergedCell):
        return image_loader.get(cell.coordinate)

    for cell_range in ws.merged_cells.ranges:
        if cell.coordinate in cell_range:
            return image_loader.get(cell_range.start_cell.coordinate)


def get_xlsx_file(folder: str) -> str | None:
    for file in os.listdir(folder):
        if file.endswith('.xlsx'):
            return f"{folder}/{file}"
